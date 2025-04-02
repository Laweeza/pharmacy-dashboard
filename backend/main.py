from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd
import uvicorn 
import traceback
import logging
import os
import numpy as np
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data")
async def get_data():
  try:
    logger.info("Checking if DB exists...")
    if not os.path.exists("audit.db"):
      logger.error("Database file not found!")
      raise HTTPException(status_code=404, detail="Database file not found")
  
    logger.info("Connecting to database...")
    connectDB = sqlite3.connect("audit.db")
    
   
    df = pd.read_sql_query("SELECT * FROM controlled_substances", connectDB)
    logger.info(f"Query returned {len(df)} rows")
    connectDB.close()
    df = df.replace({np.nan: None}) # Replace NaN values with None (will become null in JSON)

    return df.to_dict(orient="records")
  except sqlite3.Error as e:
    error_msg = f"Database error: {str(e)}"
    logger.error(error_msg)
    logger.error(traceback.format_exc())
    raise HTTPException(status_code=500, detail=error_msg)
  except Exception as e:
     if isinstance(e, HTTPException):
        raise e
     raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)