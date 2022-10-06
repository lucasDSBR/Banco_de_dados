import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="unilab"
)

con = mydb.cursor()
# con.execute("CREATE DATABASE unilab")
# con.execute("CREATE TABLE alunos (matricula int, nome varchar(60), data_nascimento date)")
# con.execute("INSERT INTO alunos(matricula, nome, data_nascimento) VALUES (232, 'LUCAS SILVA', '2022-05-30 07:39:00.000')")
con.execute(("SELECT * FROM alunos WHERE nome = 'LUCAS SILVA'"))
for (name) in con:
  print(name[0], name[1], name[2])
# mydb.commit()