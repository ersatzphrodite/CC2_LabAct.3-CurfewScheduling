# BEHOLD THE ERSATZ SYSTEM OR WHATEVZ XD
# Revised Version
# oct/16/2023 12:22
import pandas as pd

districts = [1, 2, 3, 4, 5, 6, 7, 8, 9]

d_colors = {
    'Red': [districts[0], districts[2], districts[4]],
    'Blue': [districts[1], districts[3], districts[5]],
    'Green': [districts[6], districts[7], districts[8]]
}

d_schedules = {
    'Red': ["MarketDays : Mon, Wed. 06:00 - 21:00", "Curfew: Mon, Wed, Sat. 20:00 - 05:00"],
    'Blue': ["MarketDays : Tue, Sat. 06:00 - 19:00", "Curfew: Mon, Tue, Fri. 20:00 - 05:00"],
    'Green': ["MarketDays: Thur, Fri. 06:00 - 19:00", "Curfew: Tue, Fri, Sat. 20:00 - 06:00"]
}

color = pd.DataFrame(d_colors)
schedule = pd.DataFrame(d_schedules)

red_districts = color['Red'].tolist()
blue_districts = color['Blue'].tolist()
green_districts = color['Green'].tolist()

red_schedules = schedule['Red'].tolist()
blue_schedules = schedule['Blue'].tolist()
green_schedules = schedule['Green'].tolist()

def get_name():
    while True:
        print("Please follow this format: ")
        print("<LastName>, <FirstName(s)> <MiddleInitial>.")
        name = input("Enter your name: ")
        if all(char.isalpha() or char.isspace() or char in "., " for char in name):
            return name
        else:
            print("Error: Invalid credentials. Please try again.")
            print("---------------------")

def get_district():
    while True:
        print("Enter your District number")
        try:
            district = int(input("District: "))
            if district in districts:
                return district
            else:
                print("Unregistered District.")
                print("Please select one of the following districts")
                for i in districts:
                    print(f"    -District {i}")
        except ValueError:
            print("Invalid Credentials. Please try again.")


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            return age
        except ValueError:
            print("Invalid input")
            print("---------------------")


def check_credentials(age, district):
    while True:
        if district in red_districts:
            print("DISTRICT : RED")
            if age > 60 or age < 18:
                print(red_schedules[0])
                print(red_schedules[1])
                return
            else:
                print(red_schedules[0])
                return

        elif district in blue_districts:
            print("DISTRICT : BLUE")
            if age > 60 or age < 18:
                print(blue_schedules[0])
                print(blue_schedules[1])
                return
            else:
                print(blue_schedules[0])
                return

        elif district in green_districts:
            print("DISTRICT : GREEN")
            if age > 60 or age < 18:
                print(green_schedules[0])
                print(green_schedules[1])
                return
            else:
                print(green_schedules[0])
                return

        else:
            print("You belong to me chariz")
            return

def display_profile():
    name = get_name()
    district = get_district()
    age = get_age()

    print(f"NAME : {name}")
    print(f"AGE : {age}")
    check_credentials(age, district)
    print(f"Sunday Curfew: 21:00 - 06:00")


display_profile()
