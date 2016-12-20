import pyodbc
con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
c=con.cursor()

#CREATE DB TABLE
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

#EXECUTE TABLE INTO DB
# c.execute(test)

#EXECUTE DATA INTO TABLE
#  c.execute("INSERT into monitor values('client1', 'cannabichstraat', 'Tilburg', 'Breda', 'Rotterdam')")

#SELECT ALL DATA FROM TABLE MONITOR
# c.execute("SELECT * from monitor")
# print("EERSTE:",c.fetchone())

# DELETE TABLE
# c.execute("DROP TABLE persons")

#COMMIT CHANGES
#con.commit()

#CLOSE CONNECTION WITH DB
#con.close()
