from sqlalchemy import create_engine
from data_preprocessing import final_df

engine = create_engine(
    "postgresql://postgres:Jack1776!!!@localhost:5432/network_analytics"
)

final_df.to_sql(
    "network_flows",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL")
