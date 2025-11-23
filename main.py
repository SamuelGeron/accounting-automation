import requests
import csv
from datetime import datetime, timezone
import os

def fetch_page(url, page):
    try:
        response = requests.get(f"{url}?page={page}")
        response.raise_for_status()  # Check for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
        return None

def fetch_invoices(url):
    """
    Fetches all invoices from the paginated API.
    """
    invoices = []
    first_page = fetch_page(url, 1)
    if first_page:
        first_page_data = first_page.json()
        total_pages = first_page_data.get('total_pages')
        first_page_invoices = first_page_data.get('data')
        invoices.extend(first_page_invoices)
        for page in range(2, total_pages + 1):
            response = fetch_page(url, page)
            if response:
                data = response.json()
                page_invoices = data.get('data')
                invoices.extend(page_invoices)
    return invoices

def save_to_csv(invoices, filename):
    """
    Saves the list to a CSV file.
    """
    keys = invoices[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(invoices)

if __name__ == "__main__":
    API_ENDPOINT = "https://europe-west3-recap-dev-347108.cloudfunctions.net/analytics-challenge-api/invoices"
    all_invoices = fetch_invoices(API_ENDPOINT)
    if all_invoices:
        # Define the data folder and create it if it doesn't exist
        data_folder = "data"
        os.makedirs(data_folder, exist_ok=True)

        # Generate a UTC timestamp
        extraction_time = datetime.now(timezone.utc)
        # Add the timestamp to each invoice record
        for invoice in all_invoices:
            invoice['extraction_timestamp'] = extraction_time.isoformat()

        filename_timestamp = extraction_time.strftime("%Y%m%d_%H%M%S")
        filename = f"invoices_{filename_timestamp}_UTC.csv"
        filepath = os.path.join(data_folder, filename)
        save_to_csv(all_invoices, filepath)
        print(f"Invoices saved to {filepath}")
    else:
        print("No invoices fetched!")
