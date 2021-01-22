name = input("What is your name: ")
payrate = int(input("Rate of pay per hour: "))
hofw = int(input("How many hours do you work per week: "))
if hofw <= 40:
    overtime = ("Do you get paid for overtime? (yes/no): ")
    print("{}, your payment this week is {}".format(name, (payrate*hofw)))
else:
    if 'yes' in overtime.lower():
        overtimeHours = hofw - 40
        print("{}, your payment this week is {}".format(name, (payrate*40)+(payrate*1.5*overtimeHours)))
    else:
        print("{}, your payment this week is {}".format(name, (payrate*hofw)))
else: 
