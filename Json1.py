import json

data={"name" : "Narender", "age" :35}

json_string=json.dumps(data)
print(type(json_string))
print(json_string)

json_string["name"]="Xyz"       #It will give error as It is a string and not dictonary data
print(json_string)