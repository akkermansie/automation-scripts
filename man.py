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

def laptop_arif():
    query_CPU= cur.execute("SELECT DateCreated, CPU FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
    query_MEM= cur.execute("SELECT DateCreated, Memory FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
    query_HDD= cur.execute("SELECT DateCreated, HDD FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
    DateCreated = [x[0] for x in query_CPU]
    CPU_Y = [y[1] for y in query_CPU]
    MEM_Y = [y[1] for y in query_MEM]
    HDD_Y = [y[1] for y in query_HDD]

    plt.plot(DateCreated,CPU_Y)
    plt.title("LAPTOP-ARIF")
    plt.grid(True)
    plt.savefig('test.png')
    plt.show()


    # plt.plot(*zip(*MEM))
    # plt.title("LAPTOP-ARIF")
    # plt.grid(True)
    # plt.show()
    #
    # plt.plot(*zip(*HDD))
    # plt.title("LAPTOP-ARIF")
    # plt.show()

laptop_arif()


# def laptop_arif():
#     hostname= cur.execute("SELECT Hostname FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchone()
#     arif_hostname = hostname[0]
#     return arif_hostname
#
# def cpu_arif():
#     CPU= cur.execute("SELECT CPU FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
#     arif_cpu = CPU[1:]
#     return arif_cpu


# arif_hostname = laptop_arif()
# arif_cpu = cpu_arif()
# print (arif_hostname)
# print (arif_cpu)

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
