# ------------------------------------------------------------------------------ #
#name = "John Smith"
#age = "20"
#is_new_patient = True
#
#if is_new_patient:
#    print(name + " " + "which is" + " " + age + " " + "is a new patient!")
# ------------------------------------------------------------------------------ #


#name = input("Show me what you got: ")
#print("Hello " + name)
# ------------------------------------------------------------------------------ #
#age =int(input("Enter your birth year: "))
#
#def calculate (n):
#    a = 2024 - n
#    print (a)
#
#if age < 2024:
#    calculate(age)
#else:
#    print("wrong!")
#
#x = int(input("First number: "))
#y = int(input("Second number: "))
#print(x + y)

# course = "Python for Beginners"
#course = input("Ce faci ba: ")
#
#if len(course) == 20:
#    print(course[-1::])
#elif len(course != 20):
#    print(course[2])
#print("Done!")

#assign two variables one is the mass and one is the weight


Anticariat = {'Mastodont':256, 'Riga Crypto și lapona Enigel':300, 'Iulius Cezar': 23}

i = 1
while i <= 3:
    match i:
        case 1:
            print("Helelujah!")
        case 2:
            print("YESSSSSSSSSs")
        case 3:
            print("Not so fast, Bucko!")
    i += 1





weight = int(input("Please enter your weight (in Newton): "))



if 480 < weight < 2500:
    print("Please chose a unit of measurement!")
    unit_value = input("For kilograms type 'k' for pounds type 'l': ")
    if unit_value == "k":
        kilos = int(weight / 10)
        print (kilos)
    elif unit_value == "l":
        pounds = int (weight * 0.2248089431)
        print(pounds)
    else:
        print("You haven't chosen a specified unit of measurement!")
else:
    print("Invalid character(s)!")
