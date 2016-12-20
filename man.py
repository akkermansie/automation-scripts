import pyodbc
# con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
# cur=con.cursor()
#
#
# #CREATE DB TABLE
# if cur.tables(table='monitor', tableType ='TABLE').fetchone():
#     print ("Table exists")
# else:
#     data = ("""
#                       CREATE TABLE monitor
#                       (
#                       Hostname varchar(255),
#                       CPU varchar(255),
#                       HDD varchar(255),
#                       Network varchar(255),
#                       Memory varchar(255),
#                       )
#                       """)
#     cur.execute(data)
#     cur.commit()
#     cur.close()
#     print ("Table created")
    
class Monitoring:
    ''''This is the management script for the monitoring application'''

    def db_connection(self):
        ''''Set the database connection'''
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
        self.cur = self.conn.cursor

    def check_table(self):
        '''Set the database Table'''
        if self.cur.tables(table='monitor', tableType ='TABLE').fetchone():
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
            self.cur.execute(data)
            self.cur.commit()
            self.cur.close()
