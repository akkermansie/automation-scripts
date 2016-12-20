import pyodbc
con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')

<<<<<<< HEAD
c=con.cursor()
# test = (
#   """
#   CREATE TABLE monitor
#   (
#   Hostname varchar(255),
#   CPU varchar(255),
#   HDD varchar(255),
#   Network varchar(255),
#   Memory varchar(255),
#   )
#   """)
# c.execute(test)
# c.execute("INSERT into monitor values('client1', 'cannabichstraat', 'Tilburg', 'Breda', 'Rotterdam')")
c.execute("SELECT * from monitor")
print("EERSTE:",c.fetchone())
con.commit()
con.close()
=======
personal_ov_1 = Smartcard(input("Geslacht: "),input("Voorletter: "),input("Achternaam: "),input("Geboortedatum: "))
personal_ov_2 = Smartcard(input("Geslacht: "),input("Voorletter: "),input("Achternaam: "),input("Geboortedatum: "))

Smartcard.load(personal_ov_1)
#Smartcard.load(personal_ov_2)

Smartcard.withdraw(personal_ov_1)
#Smartcard.withdraw(personal_ov_2)

print(personal_ov_1)
#print(personal_ov_2)

wijziging
>>>>>>> origin/master
