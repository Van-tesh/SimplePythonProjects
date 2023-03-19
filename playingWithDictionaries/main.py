# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades={}

# for value in student_scores:
#     score= student_scores[value]
#     if score >= 90:
#         student_grades[value]="Outstanding"
#     elif score>= 81:
#         student_grades[value]="Exceeds Expectations"
#     elif score>= 71:
#         student_grades[value]="Acceptable"
#     else:
#         student_grades[value]="Fail"
        
    



# print(student_grades)


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(        country, visits, cities):
    new_country={}
    new_country["country"]= country
    new_country["visits"]=visits
    new_country["cities"]=cities
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)