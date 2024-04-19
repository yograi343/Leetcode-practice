"""
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

customer = pd.DataFrame({"id": [1, 2, 3, 4], "name": ["Joe", "Henry", "Sam", "Max"]})
print(f"Customer Table:\n {customer}")
orders = pd.DataFrame({"id": [1, 2], "customerId": [3, 1]})
print(f"Orders Table:\n {orders}")


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orderedCustomer = list(orders.customerId.unique())
    notorderCustomer = customers.loc[
        customers["id"].apply(lambda x: x not in orderedCustomer), ["name"]
    ]
    return notorderCustomer


final_df = find_customers(customer, orders)
final_df.rename(columns={"name": "Customers"}, inplace=True)

print(f"Name of the customer who didnt ordered: \n{final_df}")
import pandas as pd
