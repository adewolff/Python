#gives amount of coin wrappers needed per coin type based on weight.

penny = 2.5
nickel = 5.0
dime = 2.268
quarter = 5.670
dollar = 8.1

while True:
    unit = input("Is weight entered in oz, lbs, or g?   ")
    if(unit not in{"oz", "ounces", "lbs", "pounds", "g", "grams"}):
        print("Please input: oz, lbs, or g")
        continue
    elif(unit in({"oz", "ounces"})):
        weight = int(float(input("Enter weight in oz:   "))) * 28.3495231
        break
    elif(unit in({"lbs", "pounds"})):
        weight = int(float(input("Enter weight in lbs:   "))) * 0.0022046226218488
        break
    elif(unit in({"g", "grams"})):
        weight = int(float(input("Enter weight in g:   ")))
        break
print(weight)