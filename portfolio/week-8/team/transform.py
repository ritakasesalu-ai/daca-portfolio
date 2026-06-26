import pandas as pd

# 1. Andmete puhastamine
def clean_data(df):
    """
    Puhastab DataFrame'i:
    - eemaldab duplikaadid
    - käsitleb olulisi NULL väärtusi
    - teisendab kuupäevad datetime formaati
    - eemaldab negatiivsed või null total_price väärtused
    """

    df_clean = df.copy()

    print("Esialgne shape:", df_clean.shape)

    # Duplikaadid
    duplicate_count = df_clean.duplicated().sum()
    print("Duplikaadid:", duplicate_count)

    df_clean = df_clean.drop_duplicates()

    # Kuupäevaveergude teisendamine
    date_columns = ["sale_date", "registration_date", "created_at"]

    for col in date_columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(
                df_clean[col],
                dayfirst=True,
                errors="coerce"
            )

    # Müügiandmete puhul on need kriitilised veerud
    critical_columns = [
        col for col in ["customer_id", "sale_date", "total_price"]
        if col in df_clean.columns
    ]

    if critical_columns:
        print("NULL-id enne puhastust:")
        print(df_clean[critical_columns].isnull().sum())

        df_clean = df_clean.dropna(subset=critical_columns)

    # total_price numbriks ja vigased väärtused välja
    if "total_price" in df_clean.columns:
        df_clean["total_price"] = pd.to_numeric(
            df_clean["total_price"],
            errors="coerce"
        )

        df_clean = df_clean.dropna(subset=["total_price"])

        negative_or_zero = (df_clean["total_price"] <= 0).sum()
        print("Negatiivsed või null total_price väärtused:", negative_or_zero)

        df_clean = df_clean[df_clean["total_price"] > 0]

    # quantity numbriks, kui see on olemas
    if "quantity" in df_clean.columns:
        df_clean["quantity"] = pd.to_numeric(
            df_clean["quantity"],
            errors="coerce"
        )

    print("\nPUHASTUSRAPORT")
    print("-" * 30)
    print("Lõplik shape:", df_clean.shape)

    if "customer_id" in df_clean.columns:
        print("Unikaalseid kliente:", df_clean["customer_id"].nunique())

    if "sale_date" in df_clean.columns:
        print(
            "Kuupäevavahemik:",
            df_clean["sale_date"].min(),
            "kuni",
            df_clean["sale_date"].max()
        )

    return df_clean


# 2. Nädalased koondnäitajad
def calculate_weekly_aggregates(df):
    """
    Arvutab nädalased müüginäitajad:
    - kogukäive
    - tellimuste arv
    - unikaalsete klientide arv
    - keskmine tellimus
    - müüdud kogus, kui quantity veerg on olemas
    """

    df_weekly = df.copy()

    if "sale_date" not in df_weekly.columns:
        raise ValueError("DataFrame'is puudub sale_date veerg.")

    if "total_price" not in df_weekly.columns:
        raise ValueError("DataFrame'is puudub total_price veerg.")

    df_weekly["sale_date"] = pd.to_datetime(
        df_weekly["sale_date"],
        errors="coerce"
    )

    df_weekly["total_price"] = pd.to_numeric(
        df_weekly["total_price"],
        errors="coerce"
    )

    df_weekly = df_weekly.dropna(
        subset=["sale_date", "total_price"]
    )

    # Nädala algus, et raportis oleks selge nädal
    df_weekly["week_start"] = (
        df_weekly["sale_date"]
        .dt.to_period("W")
        .apply(lambda period: period.start_time)
    )

    agg_rules = {
        "total_revenue": ("total_price", "sum"),
        "avg_order_value": ("total_price", "mean")
    }

    if "sale_id" in df_weekly.columns:
        agg_rules["order_count"] = ("sale_id", "nunique")
    else:
        agg_rules["order_count"] = ("total_price", "count")

    if "customer_id" in df_weekly.columns:
        agg_rules["unique_customers"] = ("customer_id", "nunique")

    if "quantity" in df_weekly.columns:
        agg_rules["quantity_sold"] = ("quantity", "sum")

    weekly = (
        df_weekly
        .groupby("week_start")
        .agg(**agg_rules)
        .reset_index()
        .sort_values("week_start")
    )

    weekly["total_revenue"] = weekly["total_revenue"].round(2)
    weekly["avg_order_value"] = weekly["avg_order_value"].round(2)

    return weekly


# 3. KPI-de arvutamine
def calculate_kpis(df):
    """
    Arvutab põhilised KPI-d:
    - total_revenue
    - unique_customers
    - avg_order_value
    - order_count
    """

    df_kpi = df.copy()

    if df_kpi.empty:
        return {
            "total_revenue": 0,
            "unique_customers": 0,
            "avg_order_value": 0,
            "order_count": 0
        }

    if "total_price" not in df_kpi.columns:
        raise ValueError("DataFrame'is puudub total_price veerg.")

    df_kpi["total_price"] = pd.to_numeric(
        df_kpi["total_price"],
        errors="coerce"
    )

    df_kpi = df_kpi.dropna(subset=["total_price"])

    total_revenue = df_kpi["total_price"].sum()

    if "customer_id" in df_kpi.columns:
        unique_customers = df_kpi["customer_id"].nunique()
    else:
        unique_customers = 0

    if "sale_id" in df_kpi.columns:
        order_count = df_kpi["sale_id"].nunique()
    else:
        order_count = len(df_kpi)

    avg_order_value = (
        total_revenue / order_count
        if order_count > 0
        else 0
    )

    kpis = {
        "total_revenue": round(total_revenue, 2),
        "unique_customers": unique_customers,
        "avg_order_value": round(avg_order_value, 2),
        "order_count": order_count
    }

    return kpis


# 4. Müügi- ja kliendiandmete liitmine
def merge_datasets(df_sales, df_customers):
    """
    Liidab müügi- ja kliendiandmed customer_id järgi.
    Müügitabel jääb põhitabeliks.
    """

    if "customer_id" not in df_sales.columns:
        raise ValueError("df_sales tabelis puudub customer_id veerg.")

    if "customer_id" not in df_customers.columns:
        raise ValueError("df_customers tabelis puudub customer_id veerg.")

    customers_unique = df_customers.drop_duplicates(
        subset=["customer_id"]
    )

    merged = pd.merge(
        df_sales,
        customers_unique,
        on="customer_id",
        how="left"
    )

    print("Sales shape:", df_sales.shape)
    print("Customers shape:", df_customers.shape)
    print("Merged shape:", merged.shape)

    return merged