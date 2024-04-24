import pandas as pd

employee = pd.DataFrame({"id": [1, 2, 3], "salary": [100, 200, 300]})


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    eployee = employee["salary"].drop_duplicates()
    emp = eployee.sort_values(ascending=False)
    if N > len(eployee):
        return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [None]})
    if N <= 0:
        return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [None]})
    emp = emp.iloc[N - 1]
    return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [emp]})


print(nth_highest_salary(employee, -1))
