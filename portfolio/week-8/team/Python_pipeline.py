# Müügiraporti pipeline

import sys
import logging

from extract import fetch_sales, fetch_customers, fetch_products

from transform import (
    clean_data,
    calculate_weekly_aggregates,
    calculate_kpis,
    merge_datasets
)

from export import (
    create_weekly_chart,
    create_kpi_summary,
    export_results
)

# Logging seadistus
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# Notify import on eraldi try/except sees,
# et pipeline töötaks ka siis, kui notify.py pole veel valmis
try:
    from notify import (
        send_pipeline_success_notification,
        send_pipeline_failure_notification
    )
except ImportError:
    send_pipeline_success_notification = None
    send_pipeline_failure_notification = None
    logger.warning("[NOTIFY] notify.py puudub või import ebaõnnestus. Teavitusi ei saadeta.")


def main():
    logger.info("Pipeline käivitus")
    logger.info(f"Command line arguments: {sys.argv}")

    # Vaikimisi kuupäevavahemik
    start_date = "2023-01-01"
    end_date = "2025-03-31"

    # Kui käivitad näiteks:
    # python Python_pipeline.py --start 2025-03-01 --end 2025-03-31
    if "--start" in sys.argv:
        start_index = sys.argv.index("--start")
        start_date = sys.argv[start_index + 1]

    if "--end" in sys.argv:
        end_index = sys.argv.index("--end")
        end_date = sys.argv[end_index + 1]

    logger.info(f"Laen müügiandmeid perioodil {start_date} kuni {end_date}")

    # ============================================================
    # EXTRACT
    # ============================================================

    logger.info("[EXTRACT] Alustan andmete laadimist")

    df_sales = fetch_sales(
        start_date=start_date,
        end_date=end_date
    )

    df_customers = fetch_customers()
    df_products = fetch_products()

    logger.info(f"[EXTRACT] Sales shape: {df_sales.shape}")
    logger.info(f"[EXTRACT] Customers shape: {df_customers.shape}")
    logger.info(f"[EXTRACT] Products shape: {df_products.shape}")

    if df_sales.empty:
        message = "Sales tabel on tühi valitud perioodis. Kontrolli kuupäevavahemikku."
        logger.warning(f"[EXTRACT] {message}")
        print("\nSales andmeid valitud perioodis ei leitud.")
        return

    # ============================================================
    # TRANSFORM
    # ============================================================

    logger.info("[TRANSFORM] Alustan andmete puhastamist")

    df_sales_clean = clean_data(df_sales)
    df_customers_clean = clean_data(df_customers)
    df_products_clean = clean_data(df_products)

    logger.info(f"[TRANSFORM] Sales clean shape: {df_sales_clean.shape}")
    logger.info(f"[TRANSFORM] Customers clean shape: {df_customers_clean.shape}")
    logger.info(f"[TRANSFORM] Products clean shape: {df_products_clean.shape}")

    logger.info("[TRANSFORM] Liidan müügi- ja kliendiandmed")

    df_merged = merge_datasets(
        df_sales_clean,
        df_customers_clean
    )

    logger.info(f"[TRANSFORM] Merged shape: {df_merged.shape}")

    logger.info("[TRANSFORM] Arvutan nädalased koondnäitajad")

    weekly_report = calculate_weekly_aggregates(df_sales_clean)

    logger.info(f"[TRANSFORM] Weekly report shape: {weekly_report.shape}")

    logger.info("[TRANSFORM] Arvutan KPI-d")

    kpis = calculate_kpis(df_sales_clean)

    logger.info(f"[TRANSFORM] KPI-d arvutatud: {kpis}")

    # ============================================================
    # VISUALIZE + EXPORT
    # ============================================================

    logger.info("[EXPORT] Loon diagrammid")

    weekly_fig = create_weekly_chart(weekly_report)
    kpi_fig = create_kpi_summary(kpis)

    logger.info("[EXPORT] Ekspordin tulemused output kausta")

    exported_files = export_results(
        df=weekly_report,
        output_dir="output",
        file_prefix="weekly_report",
        figures={
            "weekly_revenue_chart": weekly_fig,
            "kpi_summary": kpi_fig
        }
    )

    logger.info(f"[EXPORT] Failid loodud: {exported_files}")

    # ============================================================
    # NOTIFY
    # ============================================================

    if send_pipeline_success_notification is not None:
        logger.info("[NOTIFY] Saadan pipeline'i õnnestumise teavituse")

        send_pipeline_success_notification(
            pipeline_name="Iganädalane müügiraport",
            start_date=start_date,
            end_date=end_date,
            kpis=kpis,
            weekly_report=weekly_report,
            exported_files=exported_files
        )
    else:
        logger.info("[NOTIFY] Teavitust ei saadetud, sest notify.py import puudub.")

    # ============================================================
    # CONSOLE OUTPUT
    # ============================================================

    logger.info("[LOAD] Kuvan tulemused")

    print("\n" + "=" * 50)
    print("PIPELINE TULEMUSED")
    print("=" * 50)

    print("\nSALES CLEAN")
    print("Ridade arv:", len(df_sales_clean))
    print(df_sales_clean.head())

    print("\nMERGED DATA")
    print("Ridade arv:", len(df_merged))
    print(df_merged.head())

    print("\nNÄDALANE RAPORT")
    print(weekly_report.head(10))

    print("\nKPI-D")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    print("\nPRODUCTS")
    print("Ridade arv:", len(df_products_clean))
    print(df_products_clean.head())

    print("\nEKSPORDITUD FAILID")
    for name, path in exported_files.items():
        print(f"{name}: {path}")

    logger.info("Pipeline lõpetatud edukalt")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        logger.error(f"Pipeline ebaõnnestus: {e}", exc_info=True)

        if send_pipeline_failure_notification is not None:
            send_pipeline_failure_notification(
                pipeline_name="Iganädalane müügiraport",
                error_message=str(e)
            )

        raise