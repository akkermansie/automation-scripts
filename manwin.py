try:
    import pyodbc, socket, matplotlib.pyplot as plt, matplotlib.dates as mdates, xml.etree.ElementTree as etree
except ImportError:
    raise ImportError("Packages could not be imported")

tree = etree.parse('config.xml')
root = tree.getroot()
for i in root:
    print(i.find('password').text)

# try:
#     con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
#     cur=con.cursor()
# except Exception as db_connection:
#     print("Er gaat iets mis. Foutmelding: %s" %(db_connection))
#
# dates = mdates.DateFormatter('%m-%d %H:%M:%S')
#
# def create_table():
# #CREATE DB TABLE
#     if cur.tables(table='monitor', tableType ='TABLE').fetchone():
#         print ("Table exists")
#     else:
#         data = ("""
#                           CREATE TABLE monitor
#                           (
#                           Hostname varchar(25),
#                           CPU int,
#                           Memory int,
#                           HDD int,
#                           DateCreated DATETIME,
#                           )
#                           """)
#         cur.execute(data)
#         cur.commit()
#         cur.close()
#         print ("Table created")
# create_table()
#
# def laptop_arif():
# # Database query
#     query_CPU= cur.execute("SELECT DateCreated, CPU FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
#     query_MEM= cur.execute("SELECT DateCreated, Memory FROM monitor WHERE Hostname='LAPTOP-ARIF'").fetchall()
#     query_HDD= cur.execute("SELECT HDD FROM monitor WHERE Hostname='LAPTOP-ARIF' ORDER BY DateCreated DESC").fetchone()
#     Date_CPU = [x[0] for x in query_CPU]
#     CPU_Y = [y[1] for y in query_CPU]
#     Date_MEM = [x[0] for x in query_MEM]
#     MEM_Y = [y[1] for y in query_MEM]
#     HDD_STR = ("".join(map(str, query_HDD)))
#     HDD_INT = int(HDD_STR)
#
# # CPU GRAPH
#     fig, ax = plt.subplots()
#     fig.suptitle("Laptop-Arif", fontsize=20)
#     fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
#     fig.text(0.04, 0.5, 'CPU %Used', fontsize=20,va='center', rotation='vertical')
#     plt.plot(Date_CPU,CPU_Y)
#     ax.xaxis.set_major_formatter(dates)
#     plt.grid(True)
#     plt.ylim(0,100)
#     fig.autofmt_xdate()
#     plt.savefig('linux-client-cpu.png')
#     plt.cla()
#     plt.clf()
#
# # MEMORY GRAPH
#     fig, ax = plt.subplots()
#     fig.suptitle("Laptop-Arif", fontsize=20)
#     fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
#     fig.text(0.04, 0.5, 'Memory %Used', fontsize=20,va='center', rotation='vertical')
#     plt.plot(Date_MEM,MEM_Y)
#     ax.xaxis.set_major_formatter(dates)
#     plt.grid(True)
#     plt.ylim(0,100)
#     fig.autofmt_xdate()
#     plt.savefig('linux-client-memory.png')
#     plt.cla()
#     plt.clf()
#
# # HDD PIE CHART
#     labels = ('Used space', 'Free space')
#     sizes = (HDD_INT,100-HDD_INT)
#     plt.title("Laptop-Arif", fontsize=20)
#     colors = ('orange', 'yellowgreen')
#     plt.pie(sizes,
#         labels=labels,
#         colors=colors,
#         autopct='%1.1f%%',
#         shadow=True,
#         startangle=70
#         )
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.savefig('linux-client-hdd.png')
#     plt.cla()
#     plt.clf()
# laptop_arif()
