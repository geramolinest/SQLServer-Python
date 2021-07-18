import pyodbc as sql
from persona import Persona
def INSERTSQL(parameters,table):
    print("Here we'll insert")


def connectionSQL():
    conn = sql.connect(r'DRIVER={ODBC Driver 17 for SQL Server};Server=DESKTOP-68VFB54;Database=TESTDB;Trusted_Connection=yes;')         
    return conn

def SELECTSQL(table, condition):
    conn = connectionSQL()
    cur =conn.cursor()
    query = 'SELECT * FROM ' + table

    rows = cur.execute(query).fetchall()

    person = Persona()

    for row in rows:
        person.id = row.id
        person.name = row.name

        print('Persona con id: ' + person.getId() + ' y su nombre es: ' + person.getName())
        


if __name__ == '__main__':
    SELECTSQL('prueba','')