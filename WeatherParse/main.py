import csv
import io
from datetime import datetime
from collections import Counter


def readCSV(data):
    csv_file = io.StringIO(data)

    return csv.reader(csv_file, delimiter=',')

class Weather():
    def __init__(self, date, temperature, precipitation, windspeed, conditions):
        #datetime_object = datetime.strptime(date_string, format_string)
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.temperature = int(temperature)
        self.precipitation = float(precipitation)
        self.windspeed = int(windspeed)
        self.conditions = conditions
        
def weatherData():
    return """Date,Temperature,Precipitation,WindSpeed,Conditions 
    2023-01-01,30,0,5,Sunny 
    2023-01-02,32,0,7,Cloudy 
    2023-01-03,28,0.2,4,Rainy 
    2023-02-01,40,0,10,Sunny 
    2023-02-02,42,0,12,Sunny 
    2023-02-03,38,20.5,8,Rainy 
    2023-03-01,50,0,15,Sunny 
    2023-03-02,48,90,9,Cloudy 
    2023-03-03,52,6,20,Sunny
    """
    
def get_temperature(weather_obj):
    return weather_obj.temperature

def main():
    """
     - Parses the CSV file and converts dates to `datetime` objects and numeric fields to appropriate types.
     - Computes the average temperature for each month.
     - Computes the total precipitation for each month.
     - Identifies the day with the highest temperature.
     - Determines the most common weather condition for each month.
    """

    # Creates a reader object
    csv_reader = readCSV(weatherData())
    
    # Always skip the header
    header = next(csv_reader)

    weather = {}

    # Loop through the csv to build a dict of weather objects
    for row in csv_reader:
        row = [x.strip() for x in row]
        if not any(row):
            continue
        
        w = Weather(date=row[0], temperature=row[1], precipitation=row[2], windspeed=row[3], conditions=row[4])
        
        month = w.date.strftime("%Y-%m")

        if month not in weather:
            weather[month] = []
        weather[month].append(w)

    print(weather)
        
    # Compute the average temperature for each month
    for month, weather_list in weather.items():
        average_temp = sum(x.temperature for x in weather_list) / len(weather_list)
        print(f"Month: {month} - Average: {average_temp}")

    # Computes the total precipitation for each month.
    for month, weather_list in weather.items():
        total_precip = sum(x.precipitation for x in weather_list)
        print(f"Month: {month} - Total Precipitation: {total_precip}")

    # Identifies the month with the highest temperature.
    for month, weather_list in weather.items():
        days = [x.temperature for x in weather_list]
        days = sorted(days)
        print(f"Month: {month} - highest temp: {days[2]}")

    # Identifies the day with the highest temperature.

    # Flatten. This gives a list of all the weather objects
    all_weather = []
    for month in weather.values():
        for day in month:
            all_weather.append(day)
    # Flatten the Dictionary, list comprehension 
    # all_weather = [w for month_list in weather.values() for w in month_list]

    # Longer form way without lambda
    highest_day = max(all_weather, key=get_temperature)
    
    # Use max() on the Combined List, with lambda
    # highest_day = max(all_weather, key=lambda x: x.temperature)
    
    print(f"The day with the highest temperature is {highest_day.date.strftime('%Y-%m-%d')} with {highest_day.temperature}°F.")

    # Determine the most common weather condition for each month.
    # Use the Collections Counter 
    for month, weather_list in weather.items():
        # Build a list of all conditions for the month
        # ['Sunny', 'Cloudy', 'Rainy']
        conditions = [x.conditions for x in weather_list]

        # Counter({'Sunny': 1, 'Cloudy': 1, 'Rainy': 1})
        condition_counts = Counter(conditions)
    
        # ('Sunny', 1)
        most_common = condition_counts.most_common(1)[0]
       
       
        print(f"Month: {month} - Most Common Condition: {most_common[0]} (occurs {most_common[1]} times)")
if __name__ == "__main__":
    main()
