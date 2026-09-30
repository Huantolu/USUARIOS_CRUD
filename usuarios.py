from mysqlconnection import connectToMySQL
DB_NAME = "usuarios_crud"

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, datos):
        #query  
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES %(nombre)s, %(apellido)s, %(email)s, NOW(), NOW()"
        return connectToMySQL('usuarios_crud').query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_en_bd = connectToMySQL('usuarios_crud').query_db(query)
        usuarios = []
        for usuarios in usuarios_en_bd:
            


    #CRUD - CREATE READ{get all & get one & get by name} UPDATE DELETE