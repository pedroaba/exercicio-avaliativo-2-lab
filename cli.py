from teacher_crud import TeacherCRUD


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud: TeacherCRUD):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create_teacher", self.create_teacher)
        self.add_command("read_teacher", self.read_teacher)
        self.add_command("update_teacher", self.update_teacher)
        self.add_command("delete_teacher", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome: ")
        year = int(input("Entre com o ano de nascimento: "))
        cpf = input("Entre com o cpf: ")
        self.teacher_crud.create(name, year, cpf)

    def read_teacher(self):
        name = input("Entre com o nome do professor: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print(teacher)

    def update_teacher(self):
        name = input("Entre com o nome do professor: ")
        cpf = input("Entre com o novo CPF: ")
        self.teacher_crud.update(name, cpf)

    def delete_teacher(self):
        name = input("Entre com o nome do professor: ")
        self.teacher_crud.delete(name)

    def run(self):
        print("Welcome to the teacher CLI!")
        print("Available commands: create_teacher, read_teacher, update_teacher, delete_teacher, quit")
        super().run()
