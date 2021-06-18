# Whole table (dataframe)
# Whole column (series)

import pandas as pd

# ---------- Converts a csv file to a well formatted data ----------
# data = pd.read_csv("weather-data.csv")

# ---------- Convert the Column `temp` into a list ---------- #
# temp_list = data["temp"].to_list()

# ---------- Get Data in Columns ----------
# print(data["condition"])
# print(data.condition)

# ---------- Get Data in Rows ---------- #
# monday = data[data.day == "Monday"]
# print(monday)

# -------------------EXAMPLES--------------------- #
# Get the average:
# print(data["temp"].mean())
# Get the largest temperature:
# print(max(temp_list))
# Get the row which has the highest temp
# print(data[data.temp == max(data.temp)])
# Get the temp of monday and convert it into fahrenheit
# monday = data[data.day == "Monday"]
# fahrenheit_monday_temp = (monday.temp*9/5) + 32
# print(fahrenheit_monday_temp)
# -------------------EXAMPLES--------------------- #

# ---------- Creating a dataframe from scratch ----------
data_dict = {
    "students": ["Joe", "Julian", "Nicole"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)

# ---------- Creating a dataframe from scratch ----------

# Find out how many grey, cinnamon and black squirrels
# make a new dataframe with the columns `Fur Color` and `Count`
squirrel_data = pd.read_csv("squirrel_data.csv")
colors = squirrel_data["Primary Fur Color"]

gray_count = len(colors == "Gray")
cinnamon_count = len(colors == "Cinnamon")
black_count = len(colors == "Black")

squirrel_data = {
    "Count": [gray_count, cinnamon_count, black_count],
    "Fur Color": ["gray", "cinnamon", "black"],
}
df = pd.DataFrame(squirrel_data)
df.to_csv("squirrel_count.csv")
