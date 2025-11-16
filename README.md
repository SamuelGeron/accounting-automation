# Accounting Automation Scraper

This a small project I developed for using python to fetch invoice data from the endpoint https://europe-west3-recap-dev-347108.cloudfunctions.net/analytics-challenge-api/invoices and store as csv.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper, execute the `main.py` script:

```bash
python main.py
```

This will create an `invoices.csv` file in the root of the project with all the fetched invoice data.
