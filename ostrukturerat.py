#
# Detta är ett exempel på ett ostrukturerat program. Så här ska det inte se ut!
#
# - Strukturera programmet med hjälp av funktioner!
#   Möjligt arbetssätt:
#   * Börja med att lägga in egna kommentarer för vad delarna i programmet gör.
#   * Bryt sedan ut vissa delar till funktioner.
# - Hitta ett sätt att undvika redundansen i menyutskrifter och inläsning av menysvar.
# - En svaghet i programmet är beroendet på menyalternativens siffror. Dels är de anonyma
#   (säger inget om vad de innebär), dels är de känsliga för ändringar. Antag att du vill
#   ändra på ordningen i menyerna, vilka andra ändringar måste göras? Hur kan man ändra i
#   programmet så att man slipper dessa problem?
#
# På några ställen i programmet är det markerat att det är "farligt". Där bör man egentligen
# använda särfall för att hantera att användaren kan ge dåliga indata, men det hoppar vi över
# för tillfället.

import sys

def print_menu():
    ''' Prints the menu
        Returns the users choice '''
    print()
    print('Menu')
    print('1 Load a polynomial')
    print('2 Show current polynomial')
    print('3 Evaluate the polynomial in a point')
    print('4 Quit')

    menu_choices = {'1' : 'Load polynomial', '2' : 'Show polynomial', '3' : 'Evaluate polynomial', '4' : 'Quit'}

    while True:
        answer = input("What menu choice? ")
        if answer in menu_choices:
            return answer
        else:
            print("Not an option. Please try again.")


def load_poly():
    pass
    
coefficients = dict()           # Lagrar ett inläst polynom

while True:                     # Loopa tills användaren avslutar programmet
    print()
    print('Menu')
    print('1 Load a polynomial')
    print('2 Show current polynomial')
    print('3 Evaluate the polynomial in a point')
    print('4 Quit')

    good_input=False
    menu_choices = {'1' : 'Load polynomial', '2' : 'Show polynomial', '3' : 'Evaluate polynomial', '4' : 'Quit'}

    while not good_input:
        answer = input("What menu choice? ")
        if answer in menu_choices:
            good_input = True
        else:
            print("Not an option. Please try again.")

    if answer == '1':
        coefficients = dict()   # Skapa ny tom uppslagstabell
        reading_coefficients = True
        print("Enter terms as degree followed by coefficient with space inbetween. For example, the term '2.1x^3' is written as '3 2.1'.")
        print("Just hit enter when you are done with the polynomial.")
        while reading_coefficients:
            line = input("Enter a term: ")
            if line == "": # Tomma strängen -> polynomet är klart
                reading_coefficients = False
            else:
                degree_str, coeff_str = line.split() # Ingen felhantering här. Farligt.
                coefficients[int(degree_str)] = float(coeff_str) # Ingen felhantering här. Farligt.

    elif answer == '2':
        polynomial = ""
        first_term = True
        for degree in sorted(coefficients, reverse=True):
            coefficient = coefficients[degree]
            if coefficient == 0.0:
                term = ""
            else:
                if coefficient < 0.0:
                    c_str = str(coefficient)
                else:
                    if first_term:
                        c_str = str(coefficient) # Vill ej ha + på första termen
                    else:
                        c_str = "+" + str(coefficient)
                first_term = False

                # Bestäm vi hur x-delen av en term ska se ut
                if degree == 0:
                    x_str = ""
                elif degree == 1:
                    x_str = "x"
                else:
                    x_str = "x^" + str(degree)

                term = c_str + x_str

            polynomial = polynomial + term
        print("Current polynomial:", polynomial)

    elif answer == '3':
        x_str = input("Which point? x=")
        x = float(x_str)
        y = 0
        for degree, coefficient in coefficients.items():
            y = y + coefficient * x**degree

        print("y = " + str(y))

    elif answer == '4':
        pass
        #sys.exit()                  # Rekommenderat sätt att avsluta sitt program
    else:
        print("Not an alternative! Please try again.")
