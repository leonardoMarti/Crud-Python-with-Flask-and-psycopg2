import psycopg2
from connection import Connection

class Aluno():

    def create(self, nome, codigo):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into aluno (nome, codigo) values ('{nome}', '{codigo}');"
            cursor.execute(insert)
            connection.commit()
            return f"Aluno {nome}({codigo}) foi adicionado ao banco"

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def getAll(self):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT * FROM aluno;"
            cursor.execute(select)
            aluno = cursor.fetchall()

            if len(aluno):
                return aluno
            else:
                return 'Nenhum registro foi encontrado'


        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()


    def getAlunoByIdLivro(self, id):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT * FROM aluno WHERE idlivro = {id};"
            cursor.execute(select)
            aluno = cursor.fetchall()
            return aluno

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()

    def update(self, codigo, id):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE aluno SET idlivro={id} WHERE codigo='{codigo}'"
            cursor.execute(update)
            connection.commit()
            return f'O aluno codigo={codigo} teve seu livro atualizado'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def updateIdLivro(self, id, value):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE aluno SET idlivro={value} WHERE idLivro='{id}'"
            cursor.execute(update)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def delete(self, codigo):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"DELETE from aluno WHERE codigo='{codigo}';"
            cursor.execute(update)
            connection.commit()
            return f'O aluno com codigo={codigo} foi deletado'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()
