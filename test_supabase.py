import os

import pandas as pd
from supabase import create_client

# Prefer using environment variables named SUPABASE_URL and SUPABASE_KEY.
# For quick testing you can place the literal values as the second argument
# to os.getenv() below.
url = os.getenv("SUPABASE_URL", "https://llzinozmlmlispovzjww.supabase.co")
key = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxsemlub3ptbG1saXNwb3Z6and3Iiwicm9zIjo...")

supabase = create_client(url, key)


def get_data(table_name, page_size=1000):
    """Retrieve all rows from a Supabase table using pagination."""
    data = []
    page = 0
    while True:
        start = page * page_size
        end = (page + 1) * page_size - 1
        response = supabase.table(table_name).select("*").range(start, end).execute()
        if getattr(response, "error", None):
            raise Exception(f"Supabase error: {response.error}")
        batch = response.data or []
        data.extend(batch)
        if len(batch) < page_size:
            break
        page += 1
    return pd.DataFrame(data)


if __name__ == "__main__":
    # Replace table name if needed
    df = get_data('customers')
    print(df.shape)
