from smartcardscript import Smartcard

personal_ov_1 = Smartcard(input("Geslacht: "),input("Voorletter: "),input("Achternaam: "),input("Geboortedatum: "))
personal_ov_2 = Smartcard(input("Geslacht: "),input("Voorletter: "),input("Achternaam: "),input("Geboortedatum: "))

Smartcard.load(personal_ov_1)
#Smartcard.load(personal_ov_2)

Smartcard.withdraw(personal_ov_1)
#Smartcard.withdraw(personal_ov_2)

print(personal_ov_1)
#print(personal_ov_2)
