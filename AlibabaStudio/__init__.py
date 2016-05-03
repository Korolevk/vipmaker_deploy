import pymysql
import platform

# Если OS == Windows, то подключаем MySQL
# В Linux подобных системах достаточно просто "sudo apt-get install mysql-server"
# И подключиться через ODBS
if platform.system() == 'Windows':
    pymysql.install_as_MySQLdb()