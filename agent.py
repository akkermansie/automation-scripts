import pyodbc
con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
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
