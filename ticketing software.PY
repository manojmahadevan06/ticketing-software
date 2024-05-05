from numpy import random
otp = random.randint(9, size=(4))
ticket = []
value = ["Date", "Destination", "Time", "Seat"]
print("welcome to MM travels")
print("This summer special!!")
print('''1.15/4/2024''')
print('''2.16/4/2024''')
print('''3.17/4/2024''')
date = int(input('choose the date:'))
if date == 1:
    print("the bus available on 15/4/2024")
    ticket.append("15/4/2024")
elif date == 2:
    print("the bus available on 16/4/2024")
    ticket.append("16/4/2024")
elif date == 3:
    print("the bus available on 17/4/2024")
    ticket.append("17/4/2024")
else:
    print("Enter the date correctly")
print('''1.MAYILAADUTHURAI''')
print('''2.MADURAI''')
print('''3.TIRUCHI''')
place = float(input('choose the place:'))
if place == 1:
    print("the bus can travel to mayilaaduthurai")
    ticket.append("MAYILAADUTHURAI")
elif place == 2:
    print("the bus can travel to madurai")
    ticket.append("MADURAI")
elif place == 3:
    print(" the bus can travel to tiruchi")
    ticket.append("TIRUCHI")
else:
    print("Enter the place correctly")
print('''1.6:00am to 7:00am''')
print('''2.1:00pm to 3:00pm''')
print('''3.10:00pm to 12:00pm''')
time = float(input('choose the time:'))    
if time == 1:
    print("the bus will start at mornimg")
    ticket.append("6:00AM TO 7:00AM")
elif time == 2:
    print("the bus will start at after noon")
    ticket.append("1:00PM TO 3:00PM")
elif time == 3:
    print("the bus will start at mid night")
    ticket.append("10:00PM TO 12:00PM")
else:
    print("Enter the time correctly")
print('''1.MIDDLE SEAT''')
print('''2.WINDOW SEAT''')
print('''3.LAST SEAT''')
seat = float(input('choose your seat:'))
if seat == 1:
    ticket.append("MIDDLE SEAT")
elif seat == 2:
    ticket.append("WINDOW SEAT")
elif seat == 3:
    ticket.append("LAST SEAT")
print("select your payment mode")
print("1.net cash payment")
print("2.online payment")
pay = float(input('choose your payment:'))
if pay == 1:
    print("your seat was booked")
    print("Your Tracking ID is: ",otp)
elif pay == 2:
    acc = int(input("Enter your Wallet Account Number: "))
    pin = int(input("Enter your PIN number: "))
    if pin == 1234:
        print("Your Ticket is Booked!")
        print("Your Tracking ID is: ",otp)
    else:
        print("Enter the correct details")
else:
    print("Invalid")
status = int(input("To check your Ticket Status press 1: "))
if status == 1:
    check = input("Enter your Tracking ID: ")
    if check.isalpha:
        print(value)
        print(ticket)
    else:
        print("Enter the cottect OTP")
else:
    print("Invalid")
