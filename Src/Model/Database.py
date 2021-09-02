import pyodbc 

class Database:
    def __init__(self, server, database):
        self.server =  server
        self.database = database
        self.cursor = self.connect(self.server, self.database).cursor()
    
    def connect(self, server, database):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + server +';'
                      'Database=' + database + ';'
                      'Trusted_Connection=yes;')
        return conn




