#Finds change solution using least amount of coins.

quarter = 25
dime = 10
nickel = 5
penny = 1
coins = 0
quartcount = 0
dimecount = 0
nickelcount = 0
pennycount = 0 
change = -1

while not change > 0:
    change = float(input("Change owed in Dollars: "))
change = int(round(change*100))

#checks for quarter usability and dispenses quarter if possible
while (change % quarter <= quarter) and  (change >= quarter):
    coins += 1
    quartcount += 1
    change -= quarter

#checks for dime usability and dispenses dime if possible
while (change % dime <= dime) and  (change >= dime):
    coins += 1
    dimecount += 1
    change -= dime

#checks for nickel usability and dispenses nickel if possible
while (change % nickel <= nickel) and  (change >= nickel):
    coins += 1
    nickelcount += 1
    change -= nickel

#checks for penny usability and dispenses penny if possible
while (change % penny <= penny) and  (change >= penny):
    coins += 1
    pennycount += 1
    change -= penny

print("change left = ", change)
print("quarters used", quartcount)
print("dimes used", dimecount)
print("nickels used", nickelcount)
print("pennies used", pennycount)
print("coins used", coins)