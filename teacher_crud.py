from database import Database


class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.db = Database(uri, user, password)  # Composição: TeacherCRUD possui um Database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        self.db.execute_query(query, parameters={'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        return self.db.execute_query(query, parameters={'name': name})

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        self.db.execute_query(query, parameters={'name': name})

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        self.db.execute_query(query, parameters={'name': name, 'new_cpf': new_cpf})

    def close(self):
        self.db.close()
