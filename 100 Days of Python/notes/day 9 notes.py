#day 9 notes


'''
dictionary = {"bob": 55,
              "ron": 33,
              "sam": 79,
}
print(dictionary)
dictionary["jim"] = 26

dictionary["bob"] = 00
print(dictionary])
'''


'''
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])
'''


'''
nested_list = ["a","b",["c","d"]]

print(nested_list[2][0])
'''

travel_log = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    "Germany":{
    "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
    "total_visits": 5
    },
}

print (travel_log["Germany"]["cities_visited"][2])