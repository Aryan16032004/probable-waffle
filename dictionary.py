
capital={"India":"Delhi","America":"Washington","Russia":"Moscow","China":"Beijing"}
print(capital)
country=input("country: ")
print(capital.get(country))

#adding items in dictionary
capital["Australia"]="Canberra"
print(capital)

#deleting item in dictionary
del capital["America"]
print(capital)