import pandas

data = pandas.read_csv("weather_data .csv")

# print(data["temp"])
data_dic = data.to_dict()
# print(data_dic)
temp_list = data['temp'].to_list()

# print(data["temp"].mean())
# print(data['temp'].max())
#
# # Get Data in Column
# print(data["condition"])
# print(data.condition)

# Get Data in Row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_F = (monday.temp * 9/5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
