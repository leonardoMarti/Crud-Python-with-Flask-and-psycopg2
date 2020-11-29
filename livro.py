import psycopg2
from connection import Connection
from aluno import Aluno

aluno = Aluno()

class Livro():

    def create(self, nome, genero):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into livro (nome, genero) values ('{nome}', '{genero}');"
            cursor.execute(insert)
            connection.commit()
            return f'O livro {nome}({genero}) foi adicionado ao banco'

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
            select = f"SELECT * FROM livro;"
            cursor.execute(select)
            livro = cursor.fetchall()

            if len(livro):
                return livro
            else:
                return 'Nenhum registro foi encontrado'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def update(self, nome, novoNome, genero):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE livro SET nome='{novoNome}', genero='{genero}' WHERE nome='{nome}'"
            cursor.execute(update)
            connection.commit()
            return f'O livro {nome} foi atualizado para nome={novoNome}({genero})'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def delete(self, id):
        if len(aluno.getAlunoByIdLivro(id)):
            aluno.updateIdLivro(id, 'NULL')

        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"DELETE from livro WHERE id='{id}'"
            cursor.execute(update)
            connection.commit()
            return f'O livro com id={id} foi deletado'
        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()
