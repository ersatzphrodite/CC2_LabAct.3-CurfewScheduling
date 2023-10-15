#BEHOLD THE ERSATZ SYSTEM OR WHATEVZ XD
import pandas as pd

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

def check_district_color(age):
    districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]

    data = {
        'Red': [districts[0], districts[2], districts[4]],
        'Blue': [districts[1], districts[3], districts[5]],
        'Green': [districts[6], districts[7], districts[8]]
    }
    
    color_mapping = pd.DataFrame(data)
    print(color_mapping)

    while True:
        print("--------------------------------------")
        district_input = input("Enter a district: ")

        district_info = color_mapping[color_mapping.isin([district_input])].dropna(how='all')
        if not district_info.empty:
            district_color = district_info.columns[0]
            if district_color == 'Red':
                #age checker
                if age > 60 or age < 18:
                    print("Dika belong")
                    return
                else:
                    print("Belong ka")
                    return 
                print("WOW!")
            elif district_color == 'Blue':
                print("OOPSIE!")
            elif district_color == 'Green':
                print("TRY AGAIN!")
            break
        else:
            print("District not found. Please try again.")

age = get_age()
check_district_color(age)
