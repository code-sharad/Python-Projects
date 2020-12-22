# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     if score < 70:
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# Nesting Dictionary to List
# travel_log = {
#     "france": ["paris", "Lille", "Dijon"]
# }

# #Nesting Dictionary to Dictionary
# travel_log = [
#     {
#         "country":"France",
#         "cities_visited":["paris", "Lille", "Dijon"], "total_visits":12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country_visited, times_visits, new_cities):
    new_country = {"country": country_visited,
                   "visits": times_visits, "cities": new_cities}

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Saint Petersburg"])

print(travel_log)
