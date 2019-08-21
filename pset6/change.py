from cs50 import get_float

while(True):
    count = 0
    change = get_float("enter amount of change? ")
    if change < 0:
        print("renter amount")
        continue;
    change = round(100*change%(int(change)))
    while(change >= 25):
        count +=1
        change %= 25
    while(change >= 10):
        count +=1
        change %= 10
    while(change >= 5):
        count += 1
        change %= 5
    while(change > 0):
        count += 1
        change -= 1
    print(count)



