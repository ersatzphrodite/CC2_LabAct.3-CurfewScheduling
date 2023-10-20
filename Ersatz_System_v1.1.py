# BEHOLD THE ERSATZ SYSTEM OR WHATEVZ XD
# Version 1.1
# oct/20/2023 19:33
import pandas as pd

districts = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#District colors
d_colors = {
    'Red': [districts[0], districts[2], districts[4]],
    'Blue': [districts[1], districts[3], districts[5]],
    'Green': [districts[6], districts[7], districts[8]]
}
#District Schedules
d_schedules = {
    'Red': ["MarketDays : Mon, Wed. 06:00 - 21:00", "Curfew: Mon, Wed, Sat. 20:00 - 05:00"],
    'Blue': ["MarketDays : Tue, Sat. 06:00 - 19:00", "Curfew: Mon, Tue, Fri. 20:00 - 05:00"],
    'Green': ["MarketDays: Thur, Fri. 06:00 - 19:00", "Curfew: Tue, Fri, Sat. 20:00 - 06:00"]
}
#Variable setting
color = pd.DataFrame(d_colors)
schedule = pd.DataFrame(d_schedules)

#Converting to list
red_districts = color['Red'].tolist()
blue_districts = color['Blue'].tolist()
green_districts = color['Green'].tolist()

red_schedules = schedule['Red'].tolist()
blue_schedules = schedule['Blue'].tolist()
green_schedules = schedule['Green'].tolist()


def get_name():
    while True:
        name = input("⌨ Name: ")
        if all(char.isalpha() or char.isspace() or char in "., " for char in name):
            return name
        else:
            print("Error: Invalid credentials. Please try again.")
            print("---------------------")

def get_district():
    while True:
        try:
            district = int(input("⌨ District Number: "))
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
            age = int(input("⌨ Age: "))
            return age
        except ValueError:
            print("Invalid input")
            print("---------------------")


def check_credentials(age, district):
    while True:
        if age > 60 or age < 18:
            if district in red_districts:
                district_color = "Red"
                curfew_days = ', '.join(red_schedules)
                return district_color, curfew_days
    
            elif district in blue_districts:
                district_color = "Blue"
                curfew_days = ', '.join(blue_schedules)
                return district_color, curfew_days
            
            elif district in green_districts:
                district_color = "Green"
                curfew_days = ', '.join(blue_schedules)
                return district_color, curfew_days
            else:
                print("You belong to me chariz")
                return
        else: 
            if district in red_districts:
                district_color = "Red"
                curfew_days = red_schedules[0]
                return district_color, curfew_days
    
            elif district in blue_districts:
                district_color = "Blue"
                curfew_days = blue_schedules[0]
                return district_color, curfew_days
            
            elif district in green_districts:
                district_color = "Green"
                curfew_days = green_schedules[0]
                return district_color, curfew_days
            else:
                print("You belong to me chariz")
                return
        
#Main
def display_profile():
    print("》》》》》》》》》》》》 PLEASE ENTER YOUR USER INFORMATION BELOW 《《《《《《《《《《《《")
    name = get_name()
    age = get_age()
    district = get_district()
    district_color, curfew_days = check_credentials(age, district)
    
    print("》》》》》》》》》》》》》》》》 HERE IS YOUR CURFEW SCHEDULE 《《《《《《《《《《《《《《《《")
    print("")
    print(f"☞ Name: {name}")
    print(f"☞ District Color : {district_color}")
    print(f"☞ Curfew Schedule : {curfew_days}, ")
    print(f"☞ Sunday Curfew : 21:00 - 9:00")
    print("")
    print("》》》》》》》》》》》》》》》》》》》 PLEASE STAY SAFE! 《《《《《《《《《《《《《《《《《《《《")    

display_profile()
