from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    try:
# extract
        data=extract_data()
    #transformed
        Transformed_data= transform_data(data)
    #load
        load_data(Transformed_data)
        print("ETL process completed successfully!")
    except ValueError:
        print("ETL process not completed!")

if __name__ == "__main__":
    main()