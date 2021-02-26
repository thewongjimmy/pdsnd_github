#Bikehare Project for Udacity Programming for Data Science Nanodegree
#by Jimmy Wong

import time
import pandas as pd
import numpy as np

# define aliases for csv file names
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
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Please enter a city (chicago, new york city, washington):  ").lower())
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print(city, "is not a valid city.")
        except:
            print("Please enter a valid city (chicago, new york city, washington).")

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Please enter a month (all, january, february, ... , june):  ").lower())
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print(month, "is not a valid month option.")
        except:
            print("Please enter a valid month (all, january, february, ... , june).")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("Please enter the day of the week (all, monday, tuesday, ... sunday):  ").lower())
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print(day, "is not a valid day option.")
        except:
            print("Please enter a valid day of the week (all, monday, tuesday, ... sunday).")

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # let user know that the function is running
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most popular month
    popular_month = df['month'].mode()[0]
    # display the most common month
    print('Most Popular Start Month:', popular_month)

    # find the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    # display the most common day of week
    print('Most Popular Start Day of Week:', popular_day)

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # display the most common start hour
    print('Most Popular Start Hour:', popular_hour)

    # let user know how long the function took to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # let user know that the function is running
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    # display most commonly used start station
    print('Most Popular Starting Station:', popular_start_station)

    # find the most popular end station
    popular_end_station = df['End Station'].mode()[0]
    # display most commonly used end station
    print('Most Popular Ending Station:', popular_end_station)

    # create column for combination of start station and end station trip
    df['Station Combo'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    # find the most frequent combination of start station and end station trip
    popular_station_combo = df['Station Combo'].mode()[0]
    # display most frequent combination of start station and end station trip
    print('Most Popular Station Combo:', popular_station_combo)

    # let user know how long the function took to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # let user know that the function is running
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # determine total travel time
    total_duration = df['Trip Duration'].sum()
    # display total travel time
    print('Total Travel Time (seconds):', total_duration)

    # determine mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # display mean travel time
    print('Mean Travel Time (seconds):', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # determine counts of user types
    user_types = df['User Type'].value_counts()
    # display counts of user types
    print(user_types)

    try:
        # determine counts of gender
        gender = df['Gender'].value_counts()
        # display counts of gender
        print(gender)
    except:
        print("\nNo Gender data available.")

    try:
        # determine earliest, most recent, and most common year of birth
        earliest_byear = int(df['Birth Year'].min())
        recent_byear = int(df['Birth Year'].max())
        common_byear = int(df['Birth Year'].mode())
        # display earliest, most recent, and most common year of birth
        print("\nEarliest Birth Year:", earliest_byear)
        print("\nMost Recent Birth Year;", recent_byear)
        print("\nMost Common Birth Year", common_byear)
    except:
        print("\nNo Birth Year data available.")

    # display earliest, most recent, and most common year of birth
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw(df):
    """Displays raw data 5 lines at a time."""

    # ask user if they want to show raw data
    raw_data = input('\nShow raw data? (yes or no)\n').lower()
    if raw_data.lower() == 'yes':
        print(df.head())
        raw_line = 5

    # ask user if they want to show more raw data
    while raw_data.lower() == 'yes':
        raw_data = input('\nShow more raw data?').lower()
        if raw_data.lower() == 'yes':
            print(df[raw_line:raw_line+5])
            raw_line+=5

    print('-'*40)

def main():
    """Main function including user input for raw data or restart option."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw(df)

        #ask user if they'd like to restart
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
