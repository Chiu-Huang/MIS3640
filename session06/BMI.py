ph = int(input ("Do you prefer inches (1) or meters (2)?"))
pw = int(input ("Do you prefer pounds (1) or kilograms (2)?"))

if ph == 1:
    hin = float(input("what's your height in inches?"))
    h = hin * 0.0254

elif ph == 2:
    h = float(input ("what's your height in meters?"))

if pw == 1:
    wlb = float(input ("what's your weight in pounds?"))
    wkg = wlb * 0.453592

elif pw == 2:
    wkg = float(input ("what's your weight in kilos?"))

BMI = wkg / (h**2) 

if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print ("Normal Weight")
elif BMI <= 29.9:
    print ("Overweight")
else: 
    print ("Obesity")

print ("Your BMI is:", BMI)