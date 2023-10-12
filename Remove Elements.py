def day_of_week():
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    num = int(input("Please enter a number between 1 and 7: "))
    
    if num < 1 or num > 7:
        print("Invalid number. Please enter a number between 1 and 7.")
    else:
        print("The day corresponding to the number is:", days[num])

day_of_week()
