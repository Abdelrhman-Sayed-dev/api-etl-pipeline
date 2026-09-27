import logging

logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def transform(df):
    logger.info('Data transformation started')

    # Rename columns
    df = df.rename(columns={
        'id': 'cart_id',
        'order_userId': 'user_id',
        'discountPercentage': 'discount_percentage',
        'discountedTotal': 'discounted_total'
    })

    # Add calculated column
    df['discount_amount'] = df['total'] - df['discounted_total']


    # Drop columns
    df = df.drop(columns=['thumbnail'])

    logger.info('Data transformation completed successfully')

    return df

