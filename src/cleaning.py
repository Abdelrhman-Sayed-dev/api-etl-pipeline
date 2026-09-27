import pandas as pd
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def clean(df):
        # Quantity must be greater than 0
        df.loc[df['quantity'] <= 0, 'quantity'] = pd.NA

        # Price cannot be negative
        df.loc[df['price'] < 0, 'price'] = pd.NA

        # Discount percentage must be between 0 and 100
        df.loc[
            (df['discount_percentage'] < 0) |
            (df['discount_percentage'] > 100),
            'discount_percentage'
        ] = pd.NA

        # Total cannot be negative
        df.loc[df['total'] < 0, 'total'] = pd.NA

        # Discounted total cannot be negative
        df.loc[df['discounted_total'] < 0, 'discounted_total'] = pd.NA

        # Discount amount cannot be negative
        df.loc[df['discount_amount'] < 0, 'discount_amount'] = pd.NA

        logger.info('Data validation completed')

        # Drop duplicated values
        df = df.drop_duplicates()

        # NAN values

        df = df.dropna(subset=[
            'cart_id',
            'user_id',
            'quantity',
            'price'
        ])



        logger.info('Data cleaning completed successfully')
        logger.info(f'Final rows: {len(df)}')
        logger.info(f'Null values:\n{df.isnull().sum()}')
        logger.info(f'Duplicates: {df.duplicated().sum()}')
        logger.info(f'Data types:\n{df.dtypes}')

        return df