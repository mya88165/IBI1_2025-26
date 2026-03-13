# Store age, weight, gender, and creatine concentration
# Check whether each input is valid
 
age = float(input("please enter age: "))
weight = float(input("please enter weight: "))
cr = float(input("please enter creatine concentration: "))
gender = input("please enter gender (male/female): ") .lower()

# If any input is invalid, print which one is wrong
error = False 

if age >= 100:
    print("Error: age needs corrected")
    error = True 
if weight <= 20 or weight >= 80:
    print("Error: weight needs corrected")
    error = True 
if cr <= 0 or cr >= 100:
    print("Error: creatine concentration needs corrected")
    error = True 
if gender != "male" and gender != "female":
    print("Error: gender needs corrected")
    error = True  
if not error: # Otherwise calculate CrCl
    crcl = ((140 - age) * weight) / (72 * cr)

# If gender is female, multiply CrCl by 0.85
    if gender == "female":
        crcl = crcl * 0.85

# Print the final CrCl value
    print("CrCl =", crcl)
