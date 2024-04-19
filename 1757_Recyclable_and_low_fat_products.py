"""
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.


Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
"""

import pandas as pd

# create a dataframe for testing
products = pd.DataFrame(
    {
        "product_id": [0, 1, 2, 3, 4],
        "low_fats": ["Y", "Y", "N", "Y", "N"],
        "recyclable": ["N", "Y", "Y", "Y", "N"],
    }
)
print(products)
print("Product Id which are both low fat and recyclable")


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filterdf = products.loc[
        (products["low_fats"] == "Y") & (products["recyclable"] == "Y"), ["product_id"]
    ]
    return filterdf


final_df = find_products(products)

print(final_df)
