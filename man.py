import pyodbc, socket, matplotlib.pyplot as plt
con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
cur=con.cursor()



def create_table():
#CREATE DB TABLE
    if cur.tables(table='monitor', tableType ='TABLE').fetchone():
        print ("Table exists")
    else:
        data = ("""
                          CREATE TABLE monitor
                          (
                          Hostname varchar(25),
                          CPU int,
                          Memory int,
                          HDD int,
                          DateCreated DATETIME,
                          )
                          """)
        cur.execute(data)
        cur.commit()
        cur.close()
        print ("Table created")

# data = cur.execute("SELECT hostname, avg(cpu), avg(Memory), avg(HDD) from monitor GROUP BY Hostname").fetchall()
# print (data)

def create_list():
    cur.execute("SELECT DISTINCT hostname from monitor")
    host_data = cur.fetchall()
    host_list = []
    for index in range(len(host_data)):
        host_list.append(host_data[index][0])
    return (host_list)


def get_hostname():
    hostnames = create_list()
    for hostname in hostnames:
        data = cur.execute("SELECT Hostname, CPU, Memory, HDD from monitor WHERE Hostname='%s'"%(hostname)).fetchall()
        print (data)
get_hostname()


# class Monitoring():
#     ''''This is the management script for the monitoring application'''
#
#     def db_connection(self):
#         ''''Set the database connection'''
#         self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
#         self.cur = self.conn.cursor
#
#     def check_table(self):
#         '''Set the database Table'''
#         if self.cur.tables(table='monitor', tableType ='TABLE').fetchone():
#             print ("Table exists")
#         else:
#             data = ("""
#                               CREATE TABLE monitor
#                               (
#                               Hostname varchar(255),
#                               CPU varchar(255),
#                               HDD varchar(255),
#                               Network varchar(255),
#                               Memory varchar(255),
#                               )
#                               """)
#             self.cur.execute(data)
#             self.cur.commit()
#             self.cur.close()
#
