import psycopg2

class Connection():

  def getConnection(self):
    connection = psycopg2.connect(user="postgres", password="mysecretpassword", host="localhost", port="5432", database="postgres")

    return connection
