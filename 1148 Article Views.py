"""
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

import pandas as pd

views = pd.DataFrame(
    {
        "article_id": [1, 1, 2, 2, 4, 3, 3],
        "author_id": [3, 3, 7, 7, 7, 4, 4],
        "viewer_id": [5, 6, 7, 6, 1, 4, 4],
        "view_date": [
            "2019-08-01",
            "2019-08-02",
            "2019-08-01",
            "2019-08-02",
            "2019-07-22",
            "2019-07-21",
            "2019-07-21",
        ],
    }
)
views


def article_view(views: pd.DataFrame) -> pd.DataFrame:
    author_list = list(
        views.loc[views["author_id"] == views["viewer_id"], ["author_id"]]
        .rename(columns={"author_id": "id"})["id"]
        .unique()
    )
    finallist = pd.DataFrame(author_list, columns=["id"])
    return finallist


article_view(views)
