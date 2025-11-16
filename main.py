import requests
import csv

def fetch_invoices(url):
    """
    Fetches all invoices from the paginated API.
    """
    invoices = []
    page = 1
    while True:
        try:
            response = requests.get(f"{url}?page={page}")
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            page_invoices = data.get('data')
            if not page_invoices:
                break # No more data to fetch
            for i, invoice in enumerate(page_invoices): # adds extra info for tracing
                invoice['page_id'] = page
                invoice['item_id'] = i
                invoices.append(invoice)
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Request failed with error: {e}")
            break
    return invoices

def save_to_csv(invoices, filename="invoices.csv"):
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
        save_to_csv(all_invoices)
        print(f"Invoices saved to invoices.csv")

