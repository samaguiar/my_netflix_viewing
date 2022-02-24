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

def choose_user(data_set):
    name = input('Which user would you look at?  ')
    name = name.capitalize()
    #meets cateogry 1 - Calculate and display data based on an external factor
    if name == 'Tyler' or 'Bobby' or 'Donna' or 'Kids':
        df_user = data_set[data_set['Profile Name'].str.contains(name)]
        top10_episodes = df_user['Title'].value_counts().head(10).reset_index()
        fig = px.bar(top10_episodes, x='index', y='Title', title="Top 10 Most Watched Episodes")
        return(fig.show())
        
    else:
       return('There is not a user by that name.')

def main():
    determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')
    while determine !='Q':
        if determine == 'A':
            access_by_profile(df)
            determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')
        elif determine == 'I':
            print(choose_user(df))
            determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')     
    print('You quit the program. Have a good day!')

if __name__ == "__main__":
    main()

