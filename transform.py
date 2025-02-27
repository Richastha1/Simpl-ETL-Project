import pandas as pd

def transform_data(data):
    # convert the data into dataframe
    df= pd.DataFrame(data)

    df= df[['title', 'body']]

    return df