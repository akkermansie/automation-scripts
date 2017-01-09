Configuration InstallAgent
{
    param(
         [parameter(Mandatory=$true)]
         [string]$Servers
    )

    Node $Servers
    {
        File PythonToTarget
        {
            Ensure = "Present"
            Type = "File"
            SourcePath = "\\Windows-master\Share\python-3.4.3.msi"
            DestinationPath = "C:\DSC\Packages\python-3.4.3.msi"
        }

        Package PythonInstall
        {
            Ensure = "Present"
            DependsOn = "[File]PythonToTarget"
            Name = "python 3.4.3"
            ProductId = "CCD588A7-8D55-49F1-A30C-47FAB40889ED"
            Path = "C:\DSC\Packages\python-3.4.3.msi"
        }

        File PyodbcToTarget
        {
            Ensure = "Present"
            Type = "File"
            SourcePath = "\\Windows-master\Share\pyodbc-3.0.10-cp34-none-win32.whl"
            DestinationPath = "C:\DSC\Packages\pyodbc-3.0.10-cp34-none-win32.whl"
        }

        File PsutilToTarget
        {
            Ensure = "Present"
            Type = "File"
            SourcePath = "\\Windows-master\Share\psutil-5.0.1-cp34-cp34m-win32.whl"
            DestinationPath = "C:\DSC\Packages\psutil-5.0.1-cp34-cp34m-win32.whl"
        }

        File AgentToTarget
        {
            Ensure = "Present"
            Type = "File"
            SourcePath = "\\Windows-master\Share\agentwin.py"
            DestinationPath = "C:\DSC\Scripts\agentwin.py"
        }

        File ConfigToTarget
        {
            Ensure = "Present"
            Type = "File"
            SourcePath = "\\Windows-master\Share\config.ini"
            DestinationPath = "C:\DSC\Scripts\config.ini"
        }

        Script InstallPyodbc
        {
            DependsOn = "[Package]PythonInstall"
            SetScript = {pip install C:\DSC\Packages\pyodbc-3.0.10-cp34-none-win32.whl}
            TestScript = {$False}
            GetScript = {# Do Nothing}
            }
        }

        Script InstallPsutil
        {
            DependsOn = "[Package]PythonInstall"
            SetScript = {pip install --upgrade pip; pip install C:\DSC\Packages\psutil-5.0.1-cp34-cp34m-win32.whl}
            TestScript = {$False}
            GetScript = {# Do Nothing}
            }
        }

        Script InstallConfigParser
        {
            DependsOn = "[Package]PythonInstall"
            SetScript = {pip install configparser}
            TestScript = {$False}
            GetScript = {# Do Nothing}
            }
        }
		
    }
}

InstallAgent -Output c:\DSC\Agent -Servers "Win10-client"