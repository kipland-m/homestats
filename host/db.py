# db.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from databases import Database
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"  

database = Database(DATABASE_URL)
metadata = MetaData()

agent_stats = Table(
    "agent_stats",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("timestamp", DateTime, default=datetime.now()),
    Column("cpu_cores", Integer),
    Column("cpu_percent", Integer),
    Column("cpu_threads", Integer),
    Column("memory_gb", Float),
    Column("disk_gb", Float),
    Column("ip_address", String),
    Column("mac_address", String),
    Column("bytes_sent", Integer),
    Column("bytes_recv", Integer)
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

