from src.extraction.extractor import run_extraction
from src.processing.processor import run_processing

if __name__ == "__main__":
   print("Starting accounting automation pipeline...")
   # Step 1: Run the data extraction
   extracted_filepath = run_extraction()
   # Step 2: Run the data processing on the extracted file
   run_processing(extracted_filepath)
   print("\nPipeline finished.")
