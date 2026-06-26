# Andmete laadimine Supabasest

import os
import time
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client
import logging

# Logging seadistus
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# .env laadimine
load_dotenv(r"C:\Users\kasutaja\Documents\DACA-Python\.env")

url = os.getenv("SUPABASE_URL")

key = os.getenv("SUPABASE_KEY") 

print("URL olemas:", url is not None)
print("KEY olemas:", key is not None)

supabase = create_client(url, key)

print("Supabase ühendus loodud")

def execute_with_retry(operation, max_attempts=3, base_delay=1):
    """
    Käivitab API päringu retry loogikaga.
    Kui päring ebaõnnestub, ootab järjest kauem:
    1s, 2s, 4s jne.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()

        except Exception as e:
            if attempt == max_attempts:
                logger.error(f"Päring ebaõnnestus pärast {max_attempts} katset: {e}")
                raise

            delay = base_delay * (2 ** (attempt - 1))

            logger.warning(
                f"Päring ebaõnnestus. Katse {attempt}/{max_attempts}. "
                f"Proovin uuesti {delay} sekundi pärast. Viga: {e}"
            )

            time.sleep(delay)


# Üldine abifunktsioon lehekaupa laadimiseks
def fetch_table(table_name, build_query, page_size=1000):
    data = []
    page = 0

    while True:
        start_row = page * page_size
        end_row = (page + 1) * page_size - 1

        logger.info(
            f"Laen tabelit {table_name}, leht {page}, read {start_row}-{end_row}"
        )

        response = execute_with_retry(
            lambda: (
                build_query()
                .range(start_row, end_row)
                .execute()
            )
        )

        rows = response.data or []

        data.extend(rows)

        print(
            "Tabel:", table_name,
            "| Leht:", page,
            "| Ridu:", len(rows)
        )

        if len(rows) < page_size:
            break

        page += 1

    return pd.DataFrame(data)

# 1. Müügiandmete laadimine kuupäevafiltriga
def fetch_sales(start_date, end_date):
    try:
        logger.info("Laen sales andmeid...")

        def build_query():
            return (
                supabase
                .table("sales")
                .select("*")
                .gte("sale_date", start_date)
                .lte("sale_date", end_date)
            )

        df_sales = fetch_table("sales", build_query)

        logger.info(f"Sales andmeid laetud: {len(df_sales)} rida")

        return df_sales

    except Exception as e:
        logger.error(f"Error fetching sales data: {e}")

        return pd.read_csv("sales.csv")

# 2. Klientide laadimine
def fetch_customers():
    try:
        logger.info("Laen customers andmeid...")

        def build_query():
            return (
                supabase
                .table("customers")
                .select("*")
            )

        df_customers = fetch_table("customers", build_query)

        logger.info(f"Customers andmeid laetud: {len(df_customers)} rida")

        return df_customers

    except Exception as e:
        logger.error(f"Error fetching customers data: {e}")

        return pd.read_csv("customers.csv")


# 3. Toodete laadimine
def fetch_products():
    try:
        logger.info("Laen products andmeid...")

        def build_query():
            return (
                supabase
                .table("products")
                .select("*")
            )

        df_products = fetch_table("products", build_query)

        logger.info(f"Products andmeid laetud: {len(df_products)} rida")

        return df_products

    except Exception as e:
        logger.error(f"Error fetching products data: {e}")

        try:
            return pd.read_csv("products.csv")
        except FileNotFoundError:
            logger.warning("products.csv puudub. Tagastan tühja DataFrame'i.")
            return pd.DataFrame()

# 4. Testimine
if __name__ == "__main__":
    print("Alustan andmete testlaadimist...")

    df_sales = fetch_sales(
        start_date="2023-01-01",
        end_date="2025-03-31"
    )

    df_customers = fetch_customers()

    df_products = fetch_products()

    print("\nSALES")
    print("Ridade arv:", len(df_sales))
    print(df_sales.head())

    print("\nCUSTOMERS")
    print("Ridade arv:", len(df_customers))
    print(df_customers.head())

    print("\nPRODUCTS")
    print("Ridade arv:", len(df_products))
    print(df_products.head())

    

