try:
    import configparser, os, pyodbc, socket, matplotlib.pyplot as plt, matplotlib.dates as mdates
except ImportError:
    raise ImportError("Packages could not be imported")

### ConfigParser config for the Database connection ###
config = configparser.ConfigParser()
config.read("/home/admin/config.ini")
username = config.get("configuration","username")
password = config.get("configuration","password")
database = config.get("configuration","database")

### MS SQL Database Connection ### 
try:
    con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=automation-maf.database.windows.net,1433', user=username, password=password, database=database)
    cur=con.cursor()
except Exception as db_connection:
    print("Er gaat iets mis. Foutmelding: %s" %(db_connection))

### Date format for the graphs in Matplotlib ###
dates = mdates.DateFormatter('%m-%d %H:%M:%S')


### This function checks if the table monitor exists and creates it if needed ###
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
create_table()

### This function querys the database, creates a Matplotlib figure and saves it on the server ###
def linux_client():
# Database query
    query_CPU= cur.execute("SELECT TOP 10 DateCreated, CPU FROM monitor WHERE Hostname='client.maf.local' ORDER BY DateCreated DESC").fetchall()
    query_MEM= cur.execute("SELECT TOP 10 DateCreated, Memory FROM monitor WHERE Hostname='client.maf.local' ORDER BY DateCreated DESC").fetchall()
    query_HDD= cur.execute("SELECT HDD FROM monitor WHERE Hostname='client.maf.local' ORDER BY DateCreated DESC").fetchone()
    Date_CPU = [x[0] for x in query_CPU]
    CPU_Y = [y[1] for y in query_CPU]
    Date_MEM = [x[0] for x in query_MEM]
    MEM_Y = [y[1] for y in query_MEM]
    HDD_STR = ("".join(map(str, query_HDD))) ### Change the datatype of the HDD query to a string ###
    HDD_INT = int(HDD_STR) ### Change the datatype of the HDD string to a int. This is needed for substraction in Matplotlib ###

# CPU GRAPH
    cpu_loc = ('/home/admin/django/static/sitefiles/img/linux-client-cpu.png')
    fig, ax = plt.subplots()
    fig.suptitle("Linux-Client", fontsize=20)
    fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
    fig.text(0.04, 0.5, 'CPU %Used', fontsize=20,va='center', rotation='vertical')
    plt.plot(Date_CPU,CPU_Y)
    ax.xaxis.set_major_formatter(dates)
    plt.grid(True)
    plt.ylim(0,100)
    fig.autofmt_xdate()
    plt.savefig(cpu_loc)
    plt.cla()
    plt.clf()

# MEMORY GRAPH
    mem_loc = ('/home/admin/django/static/sitefiles/img/linux-client-memory.png')
    fig, ax = plt.subplots()
    fig.suptitle("Linux-Client", fontsize=20)
    fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
    fig.text(0.04, 0.5, 'Memory %Used', fontsize=20,va='center', rotation='vertical')
    plt.plot(Date_MEM,MEM_Y)
    ax.xaxis.set_major_formatter(dates)
    plt.grid(True)
    plt.ylim(0,100)
    fig.autofmt_xdate()
    plt.savefig(mem_loc)
    plt.cla()
    plt.clf()

# HDD PIE CHART
    hdd_loc = ('/home/admin/django/static/sitefiles/img/linux-client-hdd.png')
    labels = ('Used space', 'Free space')
    sizes = (HDD_INT,100-HDD_INT)
    plt.title("Linux-Client", fontsize=20)
    colors = ('orange', 'yellowgreen')
    plt.pie(sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(hdd_loc, transparent=True)
    plt.cla()
    plt.clf()
linux_client()

### This function querys the database, creates a Matplotlib figure and saves it on the server ###
def windows_client():
# Database query
    query_CPU= cur.execute("SELECT TOP 10 DateCreated, CPU FROM monitor WHERE Hostname='win10-client' ORDER BY DateCreated DESC").fetchall()
    query_MEM= cur.execute("SELECT TOP 10 DateCreated, Memory FROM monitor WHERE Hostname='win10-client' ORDER BY DateCreated DESC").fetchall()
    query_HDD= cur.execute("SELECT HDD FROM monitor WHERE Hostname='win10-client' ORDER BY DateCreated DESC").fetchone()
    Date_CPU = [x[0] for x in query_CPU]
    CPU_Y = [y[1] for y in query_CPU]
    Date_MEM = [x[0] for x in query_MEM]
    MEM_Y = [y[1] for y in query_MEM]
    HDD_STR = ("".join(map(str, query_HDD)))
    HDD_INT = int(HDD_STR)

# CPU GRAPH
    cpu_loc = ('/home/admin/django/static/sitefiles/img/win-client-cpu.png')
    fig, ax = plt.subplots()
    fig.suptitle("Windows-Client", fontsize=20)
    fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
    fig.text(0.04, 0.5, 'CPU %Used', fontsize=20,va='center', rotation='vertical')
    plt.plot(Date_CPU,CPU_Y)
    ax.xaxis.set_major_formatter(dates)
    plt.grid(True)
    plt.ylim(0,100)
    fig.autofmt_xdate()
    plt.savefig(cpu_loc)
    plt.cla()
    plt.clf()

# MEMORY GRAPH
    mem_loc = ('/home/admin/django/static/sitefiles/img/win-client-memory.png')
    fig, ax = plt.subplots()
    fig.suptitle("Windows-Client", fontsize=20)
    fig.text(0.5, 0.010,'Timestamp',fontsize=20, ha='center')
    fig.text(0.04, 0.5, 'Memory %Used', fontsize=20,va='center', rotation='vertical')
    plt.plot(Date_MEM,MEM_Y)
    ax.xaxis.set_major_formatter(dates)
    plt.grid(True)
    plt.ylim(0,100)
    fig.autofmt_xdate()
    plt.savefig(mem_loc)
    plt.cla()
    plt.clf()

# HDD PIE CHART
    hdd_loc = ('/home/admin/django/static/sitefiles/img/win-client-hdd.png')
    labels = ('Used space', 'Free space')
    sizes = (HDD_INT,100-HDD_INT)
    plt.title("Windows-Client", fontsize=20)
    colors = ('orange', 'yellowgreen')
    plt.pie(sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(hdd_loc, transparent=True)
    plt.cla()
    plt.clf()
windows_client()