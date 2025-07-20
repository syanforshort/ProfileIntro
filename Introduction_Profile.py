from datetime import datetime, date

# Ask for user's basic information
first_name = input("What is your complete first name? ")
surname = input("What is your surname? ")
birthdate_str = input("When is your birthdate? (YYYY-MM-DD) ")

# Calculate user's age
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year

    # If birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -=1

    return age

try:
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date() # Note to self: The strptime() method creates a datetime object from the given string
    age = calculate_age(birthdate)
    print(f"Hello, {first_name}. You are {age} years old.")

except ValueError:
    print("Invalid date format. Please enter the date as YYYY-MM-DD.")

