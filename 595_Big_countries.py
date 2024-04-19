"""
Table: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
 

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

worlddf = pd.DataFrame(
    {
        "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
        "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
        "area": [652230, 28748, 2381741, 468, 1246700],
        "population": [25500100, 1831741, 37100000, 78115, 202509294],
        "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
    }
)
print(f"Dataframe:\n{worlddf}")


def big_countries(worlddf: pd.DataFrame) -> pd.DataFrame:
    output = worlddf.loc[
        (worlddf["population"] >= 25000000) | (worlddf["area"] >= 3000000),
        ["name", "population", "area"],
    ]
    return output


print("Big Countries \n", big_countries(worlddf))
