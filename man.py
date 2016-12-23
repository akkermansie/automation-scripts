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
    query_HDD= cur.execute("SELECT HDD FROM monitor WHERE Hostname='LAPTOP-ARIF' ORDER BY DateCreated DESC").fetchone()
    DateCreated = [x[0] for x in query_CPU]
    CPU_Y = [y[1] for y in query_CPU]
    MEM_Y = [y[1] for y in query_MEM]
    HDD_STR = ("".join(map(str, query_HDD)))
    HDD_INT = int(HDD_STR)

## CPU GRAPH ##
    # plt.plot(DateCreated,CPU_Y)
    # plt.title("LAPTOP-ARIF")
    # plt.grid(True)
    # plt.savefig('test.png')
    # plt.show()

## MEMORY GRAPH ##
    # plt.plot(*zip(*MEM))
    # plt.title("LAPTOP-ARIF")
    # plt.grid(True)
    # plt.show()

## HDD PIE CHART ##
    # labels = ('Used space', 'Free space')
    # sizes = (HDD_INT,100-HDD_INT)
    # plt.title("LAPTOP-ARIF")
    # colors = ('orange', 'yellowgreen')
    # plt.pie(sizes,
    #     labels=labels,
    #     colors=colors,
    #     autopct='%1.1f%%',
    #     shadow=True,
    #     startangle=70
    #     )
    # plt.axis('equal')
    # plt.tight_layout()
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
