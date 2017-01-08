try:
    import pyodbc, psutil, socket, datetime, time
except ImportError:
    raise ImportError("Packages could not be imported")

try:
    con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
    c=con.cursor()
except Exception as db_connection:
    print("Er gaat iets mis. Foutmelding: %s" %(db_connection))

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

while True:
    mon_loop()