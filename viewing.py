import pandas as pd

df = pd.read_csv('ViewingActivity.csv')

def choose_user():
    name = input('Which user would you look at?')
    if name == ('Tyler' or 'Bobby'):
        df_user = df[df['Profile Name'].str.contains(name)]
        return(df_user)
    else:
        print('There is not a user by that name.')

