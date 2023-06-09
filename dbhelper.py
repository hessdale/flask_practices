import mariadb
import dbcreds
def run_procedure(sql,args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql,args)
        results = cursor.fetchall()
    except mariadb.ProgrammingError as error:
        print('there is an issue with the db code: ',error)
    except mariadb.OperationalError:
        print('there is an issue with connection to the DB',error)
    except Exception as error:
        print('there was an unknown error',error)
    finally:
        if(cursor!=None):
            cursor.close()
        if(conn != None):
            conn.close()
        return results
