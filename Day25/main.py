import pandas as pd
from numpy.ma.extras import average
from pandas._libs.tslibs import conversion

# data = pd.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Thursday"])

# Get Row with the Highest Temperature
# print(data[data.temp == data.temp.max()])

# Get the Condition of Monday
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = data.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_row = data["Primary Fur Color"]

gray_row = len(data[color_row == "Gray"])
red_row = len(data[color_row == "Cinnamon"])
black_row = len(data[color_row == "Black"])

squirrel_color_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_row, red_row, black_row]
}

squirrel_data = pd.DataFrame(squirrel_color_count)
squirrel_data.to_csv("squirrel_count.csv")



