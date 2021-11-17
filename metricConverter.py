unit2 = str(input("Enter unit2: "))
num1= float(input("Enter a number to convert: "))

if unit2=="mm":
    num1= num1*1000
elif unit2=="cm":
    num1 = num1*100
elif unit2=="mi":
    num1= num1*0.000621371192
elif unit2=="in":
    num1 = num1*39.3700787
elif unit2=="km":
    num1 = num1*0.001
elif unit2=="ft":
    num1 = num1*3.2808399
else:
    num1 = num1*1.0936133

print(num1)
