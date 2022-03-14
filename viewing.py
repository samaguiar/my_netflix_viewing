import pandas as pd
import plotly.express as px

#meets category 2 - reading data from an extrenal file
df = pd.read_csv('ViewingActivity.csv')

def access_by_profile(data_set):
    """
    input: a data set for Netflix Users

    output: a pie graph showing the profile name and number of times each user accessed the account
    """
    profile_names = data_set['Profile Name'].value_counts()
    profile_names = profile_names.reset_index()
    profile_names = profile_names.rename(columns={'index':'Profile', 'Profile Name':'Number of Times Accessed'})
    
    #meets category 3 - visualize data in graph
    fig = px.pie(profile_names, values = 'Number of Times Accessed', names ='Profile', title='Number of Times Netflix was Accessed by User')
    return(fig.show())

def choose_user(data_set):
    """
    input: data set for Netiflix User

    output: a bar graph for a specific user showing the top 10 watched episodes
    """
    name = input('Which user would you look at (Tyler, Bobby, Donna, Kids)?  ')
    name = name.capitalize()
    
    if name == 'Tyler' or 'Bobby' or 'Donna' or 'Kids':
        df_user = data_set[data_set['Profile Name'].str.contains(name)]
        top10_episodes = df_user['Title'].value_counts().head(10).reset_index()
        fig = px.bar(top10_episodes, x='index', y='Title', title="Top 10 Most Watched Episodes")
        return(fig.show())
    else:
       return('There is not a user by that name.')


#meets category 1 - runs 3 functions (access_by_profile, choose_user, main)
def main():
    #meets category 1 - creates master loop where person can put various inputs and exit program
    determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')
    while determine !='Q':
        if determine == 'A':
            #create graph with all user data by usage
            access_by_profile(df)
            #cycles back to original question to look at different anaylsis or quit
            determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')
        elif determine == 'I':
            #individual users selected; choose_user function will run
            print(choose_user(df))
             #cycles back to original question to look at different anaylsis or quit
            determine = input('Would you like to look at all user data (A) or individiual user (I)? Press Q to Quit.  ')     
    print('You quit the program. Have a good day!')

if __name__ == "__main__":
    main()

