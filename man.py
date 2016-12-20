import pyodbc

con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
cur=con.cursor()


#CREATE DB TABLE
if cur.tables(table='monitor', tableType ='TABLE').fetchone():
    print ("Table exists")
else:
    data = ("""
                      CREATE TABLE monitor
                      (
                      Hostname varchar(255),
                      CPU varchar(255),
                      HDD varchar(255),
                      Network varchar(255),
                      Memory varchar(255),
                      )
                      """)
    cur.execute(data)
    cur.commit()
    cur.close()
    print ("Table created")
