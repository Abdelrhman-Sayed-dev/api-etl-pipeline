from extract import extract
from transform import transform
from cleaning import clean
from load import load_data


def main():
    # Extract Data
    df = extract()

    # Transform Data
    df = transform(df)

    # Clean Data
    df = clean(df)

    # Load Data
    load_data(df)


if __name__ == "__main__":
    main()