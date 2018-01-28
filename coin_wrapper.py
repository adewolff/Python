#gives amount of coin wrappers needed per coin type based on weight.

penny = 2.5
nickel = 5.0
dime = 2.268
quarter = 5.670
dollar = 8.1

def main():
    coinweightgen()
    print(coinweightgen.penny_weight)


def coinweightgen():
    # Takes user input to establish weight for each coin in either oz, lbs, or g
    # If weight is given in oz or lbs it's converted to grams.
    while True:
        unit = input("Is weight entered in oz, lbs, or g?   ")
        if(unit not in{"oz", "ounces", "lbs", "pounds", "g", "grams"}):
            print("Please input: oz, lbs, or g")
            continue
        elif(unit in({"oz", "ounces"})):
            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in oz:   "))) * 28.3495231
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in oz:   "))) * 28.3495231
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in oz:   "))) * 28.3495231
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in oz:   "))) * 28.3495231
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in oz:   "))) * 28.3495231
            break
        elif(unit in({"lbs", "pounds"})):
            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in lbs:   "))) * 453.59237
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in lbs:   "))) * 453.59237
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in lbs:   "))) * 453.59237 
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in lbs:   "))) * 453.59237
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in lbs:   "))) * 453.59237
            break
        elif(unit in({"g", "grams"})):
            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in g:   ")))
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in g:   ")))
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in g:   ")))
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in g:   ")))
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in g:   ")))
            break
main()