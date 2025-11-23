from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum as _sum

def run_processing(csv_filepath):
   """
   Initializes a Spark session and processes the extracted invoice data.
   """
   if not csv_filepath:
       print("Processing skipped: No input file provided.")
       return
   print("\nStarting PySpark processing...")
   spark = SparkSession.builder \
       .appName("InvoiceAnalysis") \
       .master("local[*]") \
       .config("spark.driver.bindAddress", "127.0.0.1") \
       .getOrCreate()
   # Read the CSV data
   # inferSchema=True helps automatically detect data types like numbers and dates
   df = spark.read.csv(csv_filepath, header=True, inferSchema=True)
   print("Schema of the extracted data:")
   df.printSchema()
   # Example analysis: Calculate total amount per customer
   print("\nTotal invoice amount per customer:")
   customer_totals = df.groupBy("counter_party").agg(_sum("totalAmount").alias("total_amount"))
   customer_totals.show()
   spark.stop()
   print("PySpark processing finished.")
