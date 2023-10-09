money = 0

while (True):
    print('''Choose the monthly expenses you want calculated.
    1. Rent
    2. Electric
    3. Water
    4. Internet
    5. Personal
    6. Groceries
    7. Exit''')
    
    if input() == '7':
        print("Your monthly expenses are $" + str(money) + ".")
        break
    else:
        money = int(input()) + money