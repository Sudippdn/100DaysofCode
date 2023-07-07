travel_log = [
    {
        "country" : "Nepal",
        "visits" : 23,
        "cities" : ['kathmandu', 'banepa']
    },
    {
        "country" : "India",
        "visits" : 1,
        
        "cities" : ["banglore","pune"]
    }
    
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_Country = {}
    new_Country["country"] = country_visited
    new_Country["visits"] = times_visited
    new_Country["cities"] = cities_visited
    travel_log.append(new_Country)


add_new_country("Russia", 2, ["Moscow", "Saot Petersburg"])
print(travel_log)