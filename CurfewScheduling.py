#   degree = BS CS / SET A

import pandas as pd

print("》》》》》》》》》》》》 PLEASE ENTER YOUR USER INFORMATION BELOW 《《《《《《《《《《《《")
print("")
name = input("⌨ Name: ")
age = int(input("⌨ Age: "))
district_number = int(input("⌨ District Number: "))
print("")

data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}

color_mapping = pd.DataFrame(data)

def get_curfew_schedule(age, district_number, color_mapping):
    district_info = color_mapping[color_mapping['District'] == district_number]
    if not district_info.empty:
        district_color = district_info['Color'].values[0]
        day = ""
        curfew_start = ""
        curfew_end = ""

        if age > 60 or age < 18:
            if district_color == 'blue':
                day = "Mon/Thu/Fri"
            elif district_color == 'red':
                day = "Wed/Sat/Mon"
            elif district_color == 'green':
                day = "Tue/Fri/Sat"
            curfew_start, curfew_end = "10PM", "5AM"
        else:
            if district_color == 'blue':
                day = "Mon/Wed"
            elif district_color == 'red':
                day = "Thu/Fri"
            elif district_color == 'green':
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
