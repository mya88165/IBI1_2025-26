# Store age, weight, gender, and creatine concentration
# Check whether each input is valid
# If any input is invalid, print which one is wrong
# Otherwise calculate CrCl
# If gender is female, multiply CrCl by 0.85
# Print the final CrCl value
 
age = float(input("please enter age: "))
weight = float(input("please enter weight: "))
cr = float(input("please enter creatine concentration: "))
gender = input("please enter gender (male/female): ") .lower()
if age >= 100:
    print("Error: age needs corrected")
elif weight <= 20 or weight >= 80:
    print("Error: weight needs corrected")
elif cr <= 0 or cr >= 100:
    print("Error: creatine concentration needs corrected")
elif gender != "male" and gender != "female":
    print("Error: gender needs corrected")
else:
    crcl = ((140 - age) * weight) / (72 * cr)

    if gender == "female":
        crcl = crcl * 0.85

    print("CrCl =", crcl)
