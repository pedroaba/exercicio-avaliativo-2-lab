from cli import TeacherCLI
from database import Database
from teacher_crud import TeacherCRUD

database = Database("neo4j+s://41c6a52c.databases.neo4j.io", "neo4j", "Wa2M3am3AOP8WtN9k3VwnD-eEuUJuRgTASn95IhTl0Y")

print("Questão 1 --------")
response = database.execute_query('MATCH(teacher:Teacher{name:"Renzo"}) RETURN teacher.ano_nasc, teacher.cpf')
print(f"A) {response}")

response = database.execute_query("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf")
print(f"B) {response}")

response = database.execute_query("MATCH (c:City) RETURN c.name")
print(f"C) {response}")

response = database.execute_query("MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number")
print(f"D) {response}")


print("Questão 2 --------")
response = database.execute_query('MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS anoDoProfessorMaisNovo, MAX(t.ano_nasc) AS anoDoProfessorMaisVelho')
print(f"A) {response}")

response = database.execute_query("MATCH (c:City) RETURN AVG(c.population) AS mediaPopulacional")
print(f"B) {response}")

response = database.execute_query("MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A')")
print(f"C) {response}")

response = database.execute_query("MATCH (t:Teacher) RETURN t.name AS nomeCompleto, substring(t.name, 2) AS nomeCortado")
print(f"D) {response}")

print("Questão 3 --------")

# A)
teacher_crud = TeacherCRUD("neo4j+s://41c6a52c.databases.neo4j.io", "neo4j", "Wa2M3am3AOP8WtN9k3VwnD-eEuUJuRgTASn95IhTl0Y")

# B)
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

# C)
teacher = teacher_crud.read('Chris Lima')
print(teacher)

# D)
teacher_crud.update('Chris Lima', '162.052.777-77')

# E)
cli = TeacherCLI(teacher_crud)
cli.run()
