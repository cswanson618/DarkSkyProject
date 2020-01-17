import csv, os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings

USER = "root"
PASSWORD = "password"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "dark_sky"
TABLENAME = "CC_and_OZ_Per_Yr_Per_Park"

df = pd.read_csv("Cloud Pollution Merged.csv")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass
engine.execute(f"USE {DATABASE}")
engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")

#Send above DataFrame to SQL
df.to_sql(name = TABLENAME, con = engine)