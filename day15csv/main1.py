import pandas

data = pandas.read_csv("data.csv")


gray_color_count = len(data["Primary Fur Color"] == "Gray")
black_color_count = len(data["Primary Fur Color"] == "Black")
Cinnamon_color_count = len(data["Primary Fur Color"] == "Cinnamon")

data_dict = {
    "fur colors": ["Gray", "Black", "Cinnamon"],
    "count": [gray_color_count, black_color_count, Cinnamon_color_count]
}
count_data = pandas.DataFrame(data_dict)
count_data.to_csv("new_data.csv")