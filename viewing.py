import pandas as pd
import plotly.express as px

df = pd.read_csv('ViewingActivity.csv')

def access_by_profile(data_set):
    profile_names = data_set['Profile Name'].value_counts()
    profile_names = profile_names.reset_index()
    profile_names = profile_names.rename(columns={'index':'Profile', 'Profile Name':'Number of Times Accessed'})
    fig = px.pie(profile_names, values = 'Number of Times Accessed', names ='Profile', title='Number of Times Netflix was Accessed by User')
    return(fig.show())

def choose_user(data_set):
    name = input('Which user would you look at?')
    if name == ('Tyler' or 'Bobby'):
        df_user = df[df['Profile Name'].str.contains(name)]
        return(df_user)
    else:
        print('There is not a user by that name.')

#access_by_profile(df)