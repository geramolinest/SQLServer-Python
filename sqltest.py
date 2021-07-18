import pyodbc 
import flask
def connectionSQL():

    try:
        conn = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};Server=DESKTOP-68VFB54;Database=TESTDB;Trusted_Connection=yes;')         
       
        cur  = conn.cursor()
        query = 'INSERT INTO DBO.PRUEBA (name) VALUES(?)'
        cur.execute(query,'Gerardo')
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)


if  __name__ == '__main__':
    connectionSQL()