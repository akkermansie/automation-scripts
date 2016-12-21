import pyodbc, psutil, socket, datetime

con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
c=con.cursor()

    # if sys.platform.startswith('linux'):
    # elif sys.platform.startswith('win32'):

def mon_loop():
    for x in range(1):
        hostname = (socket.gethostname())
        cpu = (psutil.cpu_percent(interval=1))
        memory = (psutil.virtual_memory().percent)
        disk = (psutil.disk_usage('/').percent)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT into monitor values(?,?,?,?,?)",hostname,cpu,memory,disk,date)
mon_loop()
#c.execute("DROP table monitor")
c.commit()
