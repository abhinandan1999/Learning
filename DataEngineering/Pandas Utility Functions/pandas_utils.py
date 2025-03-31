from typing import List, Dict

import pandas as pd
import numpy as np

from functools import reduce

####################################################################################
                  ### DataFrame Utils ###
####################################################################################

def combine_dfs(dfs: List[pd.DataFrame], join_kw: Dict) -> pd.DataFrame:
    """
    Join the DataFrame on same key columns

    Args:
        dfs (List[pd.DataFrame]): List of DataFrames to be joined
        join_kw (Dict): Key word argument to pd.Merge

    Returns:
        pd.DataFrame: Pandas DataFrame after merging the DataFrames
    """

    combine_dfs = reduce(
        lambda df1, df2: df1.merge(df2, **join_kw),
        dfs
    )

    return combine_dfs




####################################################################################
                  ### Attributes Summaries Utilities ###
####################################################################################
def _get_dtypes(df):
    """
    Helper function to get data types of features

    Args:
        df (pd.DataFrame): Input DataFrame with attributes

    Returns:
        pd.DataFrame: DataFrame with feature names and its data type
    """
    ft_dtype = df.dtypes
    ft_dtype_df = pd.DataFrame({
        'Attribute Name': ft_dtype.index,
        'Data Type': ft_dtype.values
    })

    return ft_dtype_df

def _get_rows_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get total rows count and total unique rows count, unique values count and Null Values count

    Args:
        df (pd.DataFrame): Pandas Dataframe to perform count operations
    Return:
        pd.DataFrame: Total Rows count and unqiue Rows count, unique values count and Null Values count across all attributes.
    """

    # Total Rows and Total unique rows count
    total_rows, total_unique_rows = df.shape[0], df.drop_duplicates().shape[0]

    # Unique Value counts
    counts_df = (
        df.agg(["nunique", lambda x: x.isna().sum()])
        .T.reset_index(names="Attribute Name")
        .rename(columns={"nunique": "# of Unique Values", "<lambda>": "# of Null Values"})
        .assign(
            **{
                "# of Rows": total_rows,
                "# of Unique Rows": total_unique_rows,
                "% Unique Values": lambda x: x["# of Unique Values"]
                / x["# of Unique Rows"],
                "% Null Values": lambda x: x["# of Null Values"] / x["# of Unique Rows"],
            }
        )
    )

    return counts_df


def _get_top_n_values(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """
    Gets Top n most frequent occuring values

    Args:
        df (pd.DataFrame): Pandas DataFrame with attributes to calculate Top n

    Returns:
        pd.DataFrame: DataFrame with attributes and Top n Values
    """

    def _get_top_n_value_count(ser: pd.Series, col_name: str, top_n: int) -> List[Dict]:
        top_n_values = (
            ser.value_counts()
            .reset_index()
            .assign(
                **{
                    f"{col_name}": lambda x: np.where(
                        x.index >= top_n, "Other_Values", x[col_name]
                    )
                }
            )
            .groupby([col_name], as_index=False)
            .agg(**{"# of Occurence": ("count", "sum")})
            .sort_values("# of Occurence", ascending=False)
            .apply(lambda x: {x[col_name]: x["# of Occurence"]}, axis=1)
            .values
        )

        top_n_dict = {}
        for ele in top_n_values:
            top_n_dict.update(ele)

        return top_n_dict

    value_counts_dict = {}
    for col in df.columns:
        top_n_values = _get_top_n_value_count(df[col], col, top_n)
        value_counts_dict.update({col: [top_n_values]})

    value_counts_df = (
        pd.DataFrame.from_dict(value_counts_dict, orient="index")
        .reset_index(names="Attribute Name")
        .rename(columns={0: f"Top {top_n} values with count"})
    )

    value_counts_df[f"Top {top_n} values"] = value_counts_df[f"Top {top_n} values with count"].apply(
        lambda x: [key for key in x.keys()]
    )

    return value_counts_df

def _get_col_order(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a DataFrame indicating the order of columns in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: A DataFrame with two columns:
        - "Attribute Name": Names of the columns in `df`
        - "order": The corresponding column order (starting from 1)
    """
    order_df = pd.DataFrame({
        "Attribute Name": df.columns,
        "order": np.arange(1, len(df.columns) + 1)  # Fixed typo here
    })

    return order_df

def get_df_summary(df:pd.DataFrame, filename: str='filename', top_n: int=5) -> pd.DataFrame:
    """
    Generate the summaries of the attributes in a pandas DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame with attributes to be summarized.
        top_n (int): Number of Top n occuring values in a attribute of DataFrame

    Returns:
        pd.DataFrame: A summary DataFrame containing feature name, data type, unique value count, uniqueness ratio, percentage of null values and top N Values
    """
    # Keep the column order same as Dataframe
    col_order_df = _get_col_order(df)

    # Get Data Types of Columns
    dataType_df = _get_dtypes(df)

    # Get Count total of Columns
    row_total_df = _get_rows_count(df)

    # Get Top n Value counts
    top_n_values_df = _get_top_n_values(df, top_n=top_n)

    # Combine these datasets to create a single dataFrame
    dfs = [
        dataType_df, row_total_df, top_n_values_df
    ]
    join_kw = {
        'on': ['Attribute Name'],
        'how': 'outer'
    }
    attribute_summary_df = combine_dfs(dfs, join_kw=join_kw)
    attribute_summary_df = attribute_summary_df.sort_values(["order"], ascending=True).drop(columns=["order"])

    # Insert filename at starting
    attribute_summary_df.insert(1, "filename", filename)

    return attribute_summary_df

    