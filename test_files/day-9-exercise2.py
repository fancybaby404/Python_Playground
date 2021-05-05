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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities_visited):
    travel_log.append([
        {
            "country": str(country),
            "visits": int(visits),
            "cities": [cities_visited],
        }
    ])
    print(f"You've visited {country} {visits} times.")
    print(f"You've been to {cities_visited}")


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Philippines", 100, ["Cavite", "Dasmarinas"])