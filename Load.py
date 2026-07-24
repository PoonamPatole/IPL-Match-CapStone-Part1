import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load variables from .env
load_dotenv()

# Read database credentials
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Create MySQL connection
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

# Load CSV files
matches_df = pd.read_csv("matches_cleaned.csv")
deliveries_df = pd.read_csv("deliveries_cleaned.csv")

# Save tables to MySQL
matches_df.to_sql("matches", engine, if_exists="replace", index=False)
deliveries_df.to_sql("deliveries", engine, if_exists="replace", index=False)

print("Both tables loaded successfully!")
print(matches_df.columns)
print(matches_df.head())