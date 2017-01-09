install-ius:
  cmd.run:
    - name: yum -y install https://centos7.iuscommunity.org/ius-release.rpm

install-pkgs:
  pkg.installed:
    - pkgs:
      - yum-utils
      - python35u
      - python35u-pip
      - python35u-devel
      - unixODBC-devel
      - python2-pip
      - gcc
      - gcc-c++

pyodbc3:
  cmd.run:
    - name: pip3.5 install pyodbc

psutil3:
  cmd.run:
    - name: pip3.5 install psutil

configparser3:
  cmd.run:
    - name: pip3.5 install configparser

odbc-driver:
  cmd.run:
    - name: |
        curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/mssql-release.repo
        yum -y remove unixODBC
        ACCEPT_EULA=Y yum -y install msodbcsql-13.0.1.0-1 mssql-tools
        yum -y install unixODBC-utf16-devel

copy-script:
  file.managed:
    - name: /tmp/agent.py
    - source: salt://agent/agent.py
    - mode: 777

copy-configfile:
  file.managed:
    - name: /tmp/config.ini
    - source: salt://agent/config.ini
    - mode: 777 

agent-cron:
  cron.present:
    - name: python3.5 /tmp/agent.py
    - user: root
    - identifier: AgentScript
    - special: '@reboot'

reboot-pc:
  cmd.run:
    - name: reboot
