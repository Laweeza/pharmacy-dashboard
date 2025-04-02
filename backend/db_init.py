import sqlite3
import pandas as pd

# load excel file
df = pd.read_excel("csar.xlsx")

# Connect to db
connectDB = sqlite3.connect("audit.db")

df.to_sql("controlled_substances", connectDB, if_exists="replace", index=False)

connectDB.close()

print("Database initialized and table created!")