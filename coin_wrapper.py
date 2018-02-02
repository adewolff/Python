#gives amount of coin wrappers needed per coin type based on weight.
import math

def main():
    coinweightgen()
    coincountconv()
    wrapperconv()
    print("You will need", wrapperconv.penny_count, "penny wrappers.")


def coinweightgen():
    # Takes user input to establish weight for each coin in either oz, lbs, or g
    # If weight is given in oz or lbs it's converted to grams.
    while True:
        unit = input("Is weight entered in oz, lbs, or g?   ")
        if unit not in{"oz", "ounces", "lbs", "pounds", "g", "grams"}:
            print("Please input: oz, lbs, or g")
            continue

        #ounces
        elif unit in({"oz", "ounces"}): 

            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in oz:   "))) * 28.3495231
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in oz:   "))) * 28.3495231
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in oz:   "))) * 28.3495231
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in oz:   "))) * 28.3495231
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in oz:   "))) * 28.3495231
            break

        #pounds
        elif unit in({"lbs", "pounds"}):
            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in lbs:   "))) * 453.59237
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in lbs:   "))) * 453.59237
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in lbs:   "))) * 453.59237 
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in lbs:   "))) * 453.59237
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in lbs:   "))) * 453.59237
            break

        #grams
        elif unit in({"g", "grams"}):
            coinweightgen.penny_weight = int(float(input("Enter weight of pennies in g:   ")))
            coinweightgen.nickel_weight = int(float(input("Enter weight of nickels in g:   ")))
            coinweightgen.dime_weight = int(float(input("Enter weight of dimes in g:   ")))
            coinweightgen.quarter_weight = int(float(input("Enter weight of quarters in g:   ")))
            coinweightgen.dollar_weight = int(float(input("Enter weight of dollars in g:   ")))
            break


def coincountconv():
    #Converts coin weight to number of coins by dividing total weight of coin type by weight in grams per coin.
    coincountconv.penny_count = math.ceil(coinweightgen.penny_weight / 2.5)
    coincountconv.nickel_count = math.ceil(coinweightgen.nickel_weight / 5.0)
    coincountconv.dime_count = math.ceil(coinweightgen.dime_weight / 2.268)
    coincountconv.quarter_count = math.ceil(coinweightgen.quarter_weight / 5.670)
    coincountconv.dollar_count = math.ceil(coinweightgen.penny_weight / 8.1)

def wrapperconv():
    #calculates amount of coin wrappers needed for earch coin type based on how many coins there are.
    wrapperconv.penny_count = int(math.ceil(coincountconv.penny_count / 50))
    wrapperconv.nickel_count = int(math.ceil(coincountconv.nickel_count / 40)) 
    wrapperconv.dime_count = int(math.ceil(coincountconv.dime_count / 50))
    wrapperconv.quarter_count = int(math.ceil(coincountconv.quarter_count / 40))
    wrapperconv.dollar_count = int(math.ceil(coincountconv.dollar_count / 25))

main()