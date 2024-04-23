import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].str.capitalize()
    return users.sort_values('user_id')

Users = pd.DataFrame(
    {
        'user_id':[1,2],
        'name':['aLice','bOB']
})

print(fix_names(Users))
