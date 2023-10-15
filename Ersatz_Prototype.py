#BEHOLD THE ERSATZ SYSTEM OR WHATEVZ XD
#This shit works
#oct/16/2023 00:33
import pandas as pd

districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]

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


def get_district():
    district = input("Enter district: ")
    return district


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            while True:
                print("---------------------")
                print(f"Entered age: {age}")
                confirmation = input("Please confirm if the credentials are correct (y/n): ")
                if confirmation == "y":
                    print("---------------------")
                    return age
                elif confirmation == "n":
                    print("Resubmit credentials.")
                    print("---------------------")
                    break  
                else:
                    print("Invalid response. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input")
            print("---------------------")


def check_credentials(age):
    while True: 
        if district in red_districts:
            print("You belong to Red")
            if age > 60 or age < 18:
                print(red_schedules[0])
                print(red_schedules[1])
                return
            else:
                print(red_schedules[0])
                return
                
        elif district in blue_districts:
            print("You belong to Blue")
            if age > 60 or age < 18:
                print(blue_schedules[0])
                print(blue_schedules[1])
                return
            else:
                print(blue_schedules[0])
                return
                
        elif district in green_districts:
            print("You belong to Green")
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
        
district = get_district()
age = get_age()
check_credentials(age)

