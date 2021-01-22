max_tries = 5
pin = 1234
print ("Enter the pin")
for _ in range(max_tries):
    user_pin = int(input())
    if user_pin == pin:
        print('Access Granted')
        break
    print('Pin is incorrect, try again')
