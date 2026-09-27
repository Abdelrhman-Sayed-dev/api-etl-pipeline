import requests
import pandas as pd
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


# API endpoint
url = 'https://dummyjson.com/carts'


# Extract data from the API
def extract(url):
    try:
        data = requests.get(url, timeout=30).json()['carts']

        # Convert nested products data into a DataFrame
        orders_df = pd.json_normalize(
            data,
            record_path='products',
            meta=['id', 'userId'],
            meta_prefix='order_'
        )

        logger.info("Data extracted successfully")

        return orders_df

    except Exception as e:
        logger.error(f"Failed to extract data: {e}")


