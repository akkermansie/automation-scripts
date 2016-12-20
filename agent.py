import pyodbc, sys, psutil

con = pyodbc.connect('DRIVER={SQL Server};SERVER=automation-maf.database.windows.net,1433', user='marif@automation-maf', password='P@ssw0rd', database='monitoring')
c=con.cursor()

def function():
    pass
    # if sys.platform.startswith('linux'):
    # elif sys.platform.startswith('win32'):

#cpu percentage 5 samples with 1 sec interva;
def cpu_usage():
    for x in range(5):
        cpu = (psutil.cpu_percent(interval=1))
        print ('Cpu:',cpu,'% used')
cpu_usage()

#memory percentage
def mem_usage():
    for x in range(1):
        memory = (str(psutil.virtual_memory().percent))
        print ('Memory: '+memory+'% used')
mem_usage()

#disk percentage
def disk_usage():
    for x in range(1):
        disk = str(psutil.disk_usage('/').percent)
        print ('Disk: ',disk+'% used')
disk_usage()

#network percentage
def network_usage():
    pass
#wat gaan we monitoren??
