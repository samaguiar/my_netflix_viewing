import pandas as pd
import plotly.express as px

#meets cateogry 2 - reading data from an extrenal file
df = pd.read_csv('ViewingActivity.csv')

def access_by_profile(data_set):
    profile_names = data_set['Profile Name'].value_counts()
    profile_names = profile_names.reset_index()
    profile_names = profile_names.rename(columns={'index':'Profile', 'Profile Name':'Number of Times Accessed'})
    
    #meets cateogry 3 - visualize data in graph
    fig = px.pie(profile_names, values = 'Number of Times Accessed', names ='Profile', title='Number of Times Netflix was Accessed by User')
    return(fig.show())

def choose_user(df):
    name = input('Which user would you look at?')
    #meets cateogry 1 - Calculate and display data based on an external factor
    if name == ('Tyler' or 'Bobby'):
        df_user = df[df['Profile Name'].str.contains(name)]
        return(df_user)
    else:
       return('There is not a user by that name.')

def main():
    access_by_profile(df)
    print(choose_user(df))

if __name__ == "__main__":
    main()