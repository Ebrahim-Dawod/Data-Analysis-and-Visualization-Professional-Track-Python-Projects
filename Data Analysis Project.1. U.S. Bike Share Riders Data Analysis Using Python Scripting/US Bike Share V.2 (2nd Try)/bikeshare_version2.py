import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n ')

    cities=['chicago', 'new york city', 'washington']
    months=["january","february","march","april","may","june","all"]
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    x = 0
    while x==0 :
        try :
            city = input(" Choose a City : (chicago, new york city, washington) : ").lower()
            for  everycity in cities :
                if everycity==city :
                  print("\nfetching {} Data ... \n" .format(city))
                  x=1
                  break
            if x==0 :
             print("Please type City Name Correctly ")
             continue

        except:
            print("Oops Error, Please type City Name Correctly ")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    x = 0
    while x==0 :
        try :
            month = input(" Choose a month : (all, january, february,march,april,may, june) : ").lower()
            for everymonth in months :
                if everymonth==month :
                  print("\nfetching {} Data ... \n".format(month))
                  x=1
            if x == 0:
              print("Please type month Name Correctly ")
              continue
        except:
            print("Oops Error, Please type month Name Correctly ")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    x = 0
    while x==0 :
        try :
            day = input(" Choose a day of week : (all,monday,tuesday,wednesday,thursday,friday,saturday,sunday) : ").lower()
            for everyday in days :
                if everyday==day :
                 print("\nfetching {} Data ... \n".format(day))
                 x=1
            if x == 0:
              print("Please type Name of a day of week Correctly ")
              continue
        except:
            print("Oops Error, Please type Name of a day of week Correctly ")
            continue


    print('-'*60,"\n")
    print("fetching data for City: {} ,Month : {}, Day of Week: {} ... \n{}\n ".format(city,month,day,"#"*70))

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df["Start Time"])




    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df["Start Time"].dt.day_name() #################  weekday_name  ############

    df['hour'] = df["Start Time"].dt.hour



    # print("Month :\n",df["month"])
    # print("day of week:\n",df["day_of_week"])


    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        ###df = df["month"][month]

        df = df[df["month"] == month]
        ##print(df)
        # df = df.groupby([month]).value_counts()

        if day != 'all':
            df = df[df["day_of_week"] == day.title()]


    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["month"].mode()[0]
    print("Most Common Month : ",popular_month)
    print("#"*60,"\n")

    # TO DO: display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print("Most Common day of week : ",popular_day)
    print("#" * 60, "\n")

    # TO DO: display the most common start hour
    popular_hour = df["hour"].mode()[0]
    print("Most Common Hour : ", popular_hour)
    print("#" * 60, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 60,"\n",'-' * 60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("Most Common Start Station : ", popular_start_station)
    print("#" * 60, "\n")

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("Most Common End Station : ", popular_end_station)
    print("#" * 60, "\n")

    # TO DO: display most frequent combination of start station and end station trip
    #popular_station_compination = df["Start Station"]["End Station"].mode()[0]
    #popular_station_compination=("\n\nFrom : " + df["Start Station"] + '  >> To >>  ' + df["End Station"]).mode()[0]
    print("Most frequent combination of start station and end station trip :"
          " ", ("\n\nFrom : " + df["Start Station"] + '  >> To >>  ' + df["End Station"]).mode()[0])
    print("#" * 60, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 60,"\n",'-' * 60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_seconds=df["Trip Duration"].sum()


    print("Total Travel Time (in Seconds) =  {} Seconds \n ".format(df["Trip Duration"].sum()))
    print("Total Travel Time (in Days ) =  {}  Days \n ".format(df["Trip Duration"].sum()/(60*60*24)))
    # TO DO: display mean travel time
    print("#" * 60, "\n")
    print("Mean Travel Time (in Seconds) = ",df["Trip Duration"].mean(),"Seconds","\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60,"\n",'-'*60)



def user_stats(df):
    """Displays statistics on bikeshare users."""
    start_time = time.time()
    if 'Gender' in df and "Birth Year" in df :
        # Only access Gender and Birth Year columns in this case

        print('\nCalculating User Stats...\n')


        # TO DO: Display counts of user types
        # user_type_counter=df["User Type"].value_counts()
        user_type_counter = df["User Type"].value_counts()
        print("\nUser Types Counts : \n###############\n", user_type_counter, "\n")

        # TO DO: Display counts of gender
        # gender_counter=df["Gender"].value_counts()
        gender_counter = df["Gender"].value_counts()
        print("\nGender Counts : \n###############\n", gender_counter, "\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        # earliest year of birth = df['Birth Year'].min()
        # most recent year of birth = df['Birth Year'].max()
        # most common year of birth = df["Birth Year"].mode()[0]
        print('-' * 60, "\n")
        print("Earliest Year of Birth = ", df['Birth Year'].min())
        print("#" * 60, "\n")

        print("Most Recent Year of Birth = ", df['Birth Year'].max())
        print("#" * 60, "\n")

        print("Most Common Year of Birth = ", df["Birth Year"].mode()[0])
        print("#" * 60, "\n")

    else:
        print('Gender and Birth Year stats cannot be calculated \n'
              ' because Gender and Birth Year does not appear in the dataframe\n'
              ' (there is no Such Columns in this City file)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60,"\n",'-'*60)







def main():
    while True:
        exit=0
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df1 = load_data(city, "all", "all")
        # to pass it to " time_stats(df1) " function : to calculate Statistics for "all" months and "all" Days always

        while 1:
            try:
                choice = input("What Do you Like to See ? (Choose a Number (1,2,3,4,5,6,7) \n"
                               "1 - Displays statistics on the most frequent times of travel.\n"
                               "2 - Displays statistics on the most popular stations and trip.\n"
                               "3 - Displays statistics on the total and average trip duration.\n"
                               "4 - Displays statistics on bikeshare users.\n"
                               "5 - Display the Raw Data \n"
                               "6 - (Restart) Choose another Data (City,Month,Day)\n"
                               "7 - Exit\n"
                               "Your Answer Is = ").lower()
                if choice == "1":
                    print("Displaying statistics on the most frequent times of travel ...\n")
                    time_stats(df1)
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                        break

                elif choice == "2":
                    print("Displaying statistics on the most popular stations and trip...\n")
                    station_stats(df)
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                        break

                elif choice == "3":
                    print("Displaying statistics on the total and average trip duration...\n")
                    trip_duration_stats(df)
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                        break

                elif choice == "4":
                    print("Displays statistics on bikeshare users... \n")
                    user_stats(df)
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                        break

                elif choice == "5":
                    print("Displaying the Raw Data...\n")
                    y=5
                    print(df.head(y))
                    while True :
                        try:
                            s = input("Do You want to See More ? (yes or no)").lower()
                            if s=="yes":
                                y += 5
                                print(df.head(y))
                            elif s=="no" :
                                break
                            else :
                                print("Please Type a Correct Choice (yes or no)")
                        except:
                            print("Oops Error , Please Type a Correct Choice (yes or no)")
                    y=0

                elif choice == "6":
                    print("Restarting ...")
                    break

                elif choice == "7":
                    print("Exiting ...\n*** Thanks for your Trust ***")
                    exit=1

                    break


                else:
                    print("please Type a correct Number Between 1 and 7 ")

            except:
             print("Oops Error , please Type a correct Number Between 1 and 7 ")
        if exit==1:
         break



if __name__ == "__main__":
 main()
