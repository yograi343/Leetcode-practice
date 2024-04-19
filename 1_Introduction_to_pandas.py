import pandas as pd

lst = [[1, 15], [2, 11], [3, 11], [4, 20]]


# creating a dataframe using the list and providing the names of the columns
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns_list = ["student_id", "age"]
    df = pd.DataFrame(student_data, columns=columns_list)
    return df


df = createDataframe(lst)
print(df)


# creating a function that will return the shape of the dataframe
def sizeDataFrame(df: pd.DataFrame) -> list[int]:
    return list(df.shape)


print("Shape of the DataFrame: ", sizeDataFrame(df))
