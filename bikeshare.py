import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("About which city do you need information? Please type New York City, Chicago or Washington.\n")
        city = city.lower()
        if city in ('chicago', 'new york city'):
            print("Your choice is ", city, "\n")
            break
        elif city == 'washington':
            print("Your choice is ", city, " and notice that there is no available gender, birth year data for it. \n")
            break
        else:
            print("Sorry, invalid input. Please enter a valid city name. \n")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Do you need information regarding to one of the first six months? If yes, type month name, else type 'all' \n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Sorry, invalid input. Please enter a valid month name, or type 'all' \n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Do you need information regarding to a specific day? If yes, type day name, else type 'all' \n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Sorry, invalid input. Please enter a valid day name. \n")

    print('-'*40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month: ", most_common_month, "\n")

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day: ", most_common_day, "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour: ", most_common_hour,":00  - ",most_common_hour,":59 \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", most_common_start_station, "\n")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    try:
        popular_combination = df['Start Station'] + " --- " + df['End Station']

        print('the most popular trip is:\n', popular_combination.mode()[0], '\n')
    except Exception as e:
        print('The most frequent combination is N/A because as an error occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() /86400
    total_travel_time = str(round(total_travel_time, 2))
    print("The total travel time: ", total_travel_time, " days \n")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() /60
    mean_travel_time = str(round(mean_travel_time, 2))
    print("The total mean time: ", mean_travel_time, "minutes \n" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types: \n",user_types, "\n")

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('Gender Types: \n',gender_types, "\n")
    except KeyError:
      print("Gender Types: N/A for this city. \n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('Earliest Birth Year: ', earliest_year, "\n")
    except KeyError:
      print("Earliest Birth Year: N/A for this city. \n")

    try:
      most_recent_year = df['Birth Year'].max()
      print('Most Recent Birth Year:', most_recent_year, "\n")
    except KeyError:
      print("Most Recent Birth Year: N/A for this city. \n")

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('Most Common Birth Year:', most_common_year, "\n")
    except KeyError:
      print("Most Common Birth Year: N/A for this city. \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    i = 1
    while True:
        raw = input('\nWould you like to see raw data? Enter yes for first 5 rows.\n')
        if raw.lower() == 'yes':
            print(df[i:i+5])
            i = i+5
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
