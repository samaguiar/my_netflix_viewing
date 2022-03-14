# my_netflix_viewing

**Overview** 

This project focuses on using Netflix data from my account. Based on user input through the program, different graphical representation will be created. 


**The Questions** 
1) Who used the netflix account the most?
2) What are the top ten most watched show for a specific user? 
3) What is the frequency of each episode for the top ten shows?

**Data Source**

My data source was downloaded from my netflix account for 4 users. It is saved as ViewingActivity.csv. 

**Requirements**

All need packages can be installed by the requirements.txt file. The following packages are included:
- pandas
- plotly

**Features Included**

The features included for the Data Anaylsis 1 Project are: 

1) Category 1 - I created master loop where a person can put various inputs and exit program. The master loop will ask the user if they want to look at all users data or individual data. It will also allow the user to quit the program. 

2) Category 1 - The program runs 3 functions in the program: access_by_profile, choose_user, and main. access_by_profile function creates a table based on profile name and number of unique access points. It will then create a pie chart based on the table. choose_user function takes an input based on a specific user and will create a bar chart for the top 10 episodes watched. main runs the master loop and asks two questions. Based on the input, the program will show various graphical representation. 

3) Category 2 - The program reads a csv file from an external source. 

4) Category 3 - The program creates a pie chart and bar graph based on a specific input. 

5) Category 4 - The program utilize a virtual environment and document library dependencies in a requirements.txt file.


**Special Instructions**
1. Run git clone https://github.com/samaguiar/my_netflix_viewing.git to clone repo.

MacOS/Unix
2. Create a virtual environment: python3 -m venv env
2. Activate virtual environment: source env/bin/activate
3. Install requirements: python3 -m pip install -r requirements.txt
4. Run the following code to start the program: python3 viewing.py

Windows
2.  Create a virtual environment: py -m venv env
3. Activate virtual environment: .\env\Scripts\activate
4. Install requirements: py -m pip install -r requirements.txt
5. Run the following code to start the program: py viewing.py

**Next Steps**
- [] Determine top 10 favorite shows based on input
- [] Determine top 10 favorite movies based on input
- [] Ask the program user for movie/tv show and see if a netflix user has watched it
- [] Show user usage over time based on input