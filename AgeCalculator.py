# from datetime import date

# def calculate_age(birth_date):
#     today = date.today()
#     age_years = today.year - birth_date.year
#     if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
#         age_years -= 1
#     age_days = (today - birth_date).days
#     return age_years, age_days

# # Get the user's date of birth
# year = int(input("Enter your birth year (YYYY): "))
# month = int(input("Enter your birth month (MM): "))
# day = int(input("Enter your birth day (DD): "))
# birth_date = date(year, month, day)

# # Calculate the user's age in years and days
# age_years, age_days = calculate_age(birth_date)

# # Print the user's age
# print("Your age is:", age_years, "years and", age_days, "days")


from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day
    if age_days < 0:
        # Borrow a month from the age in months
        age_months -= 1
        # Add the number of days in the borrowed month to the age in days
        last_month = (today.month - 1) % 12 or 12  # get last month (e.g. December for January)
        days_in_last_month = (date(today.year, today.month, 1) - date(today.year, last_month, 1)).days
        age_days += days_in_last_month
    if age_months < 0:
        # Borrow a year from the age in years
        age_years -= 1
        # Add the number of months in the borrowed year to the age in months
        age_months += 12
    return age_years, age_months, age_days

# Get the user's date of birth
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))
birth_date = date(year, month, day)

# Calculate the user's age in years, months, and days
age_years, age_months, age_days = calculate_age(birth_date)

# Print the user's age
print("Your age is:", age_years, "years,", age_months, "months, and", age_days, "days")
