#   degree = BS CS / SET A
import pandas as pd

print("》》》》》》》》》》》》 PLEASE ENTER YOUR USER INFORMATION BELOW 《《《《《《《《《《《《")
print("")
name = input("⌨ Name: ")
age = int(input("⌨ Age: "))
district_number = int(input("⌨ District Number: "))
print("")

#new variable set
districts = ["District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9"]
data = {
    'Red': [districts[0], districts[2], districts[4]],
    'Blue': [districts[1], districts[3], districts[5]],
    'Green': [districts[6], districts[7], districts[8]]
}

color_mapping = pd.DataFrame(data)

def get_curfew_schedule(age, district_input, color_mapping):
    district_info = color_mapping[color_mapping.isin([district_input])].dropna(how='all')
    if not district_info.empty:
        district_color = district_info.columns[0]
        day = ""
        curfew_start = ""
        curfew_end = ""

        if age > 60 or age < 18:
            if district_color == 'Blue':
                day = "Mon/Thu/Fri"
            elif district_color == 'Red':
                day = "Wed/Sat/Mon"
            elif district_color == 'Green':
                day = "Tue/Fri/Sat"
            curfew_start, curfew_end = "10PM", "5AM"
        else:
            if district_color == 'Blue':
                day = "Mon/Wed"
            elif district_color == 'Red':
                day = "Thu/Fri"
            elif district_color == 'Green':
                day = "Tue/Sat"
            curfew_start, curfew_end = "6AM", "9PM"

        return district_color, day, f"{curfew_start}-{curfew_end}"
    else:
        return 'unknown', '', ''

district_color, day, curfew_schedule = get_curfew_schedule(age, district_number, color_mapping)

print("》》》》》》》》》》》》》》》》 HERE IS YOUR CURFEW SCHEDULE 《《《《《《《《《《《《《《《《")
print("")
print("☞ Name:", name)
print("☞ District Color:", district_color)
print("☞ Curfew Schedule:", day, curfew_schedule + ", Sun 9PM-6AM")
print("")
print("》》》》》》》》》》》》》》》》》》》 PLEASE STAY SAFE! 《《《《《《《《《《《《《《《《《《《《")
