### Import required modules ###
try:
    import pyodbc, psutil, socket, datetime, time, configparser
except ImportError:
    raise ImportError("Packages could not be imported")

### ConfigParser config for the Database connection ###
config = configparser.ConfigParser()
config.read("C:\DSC\Scripts\config.ini")
username = config.get("configuration","username")
password = config.get("configuration","password")
database = config.get("configuration","database")

### MS SQL Database Connection ###
try:
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user=username, password=password, database=database)
    c=con.cursor()
except Exception as db_connection:
    print("Er gaat iets mis. Foutmelding: %s" %(db_connection))

### This function collects information about the hostname, cpu, memory, disk and date and store the information in the Azure Database ###
def mon_loop():
    for x in range(1):
        hostname = (socket.gethostname())
        cpu = (psutil.cpu_percent(interval=1))
        memory = (psutil.virtual_memory().percent)
        disk = (psutil.disk_usage('/').percent)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT into monitor values(?,?,?,?,?)",hostname,cpu,memory,disk,date)
        c.commit()
        time.sleep(30)

### Infinite loop ###
while True:
    mon_loop()
