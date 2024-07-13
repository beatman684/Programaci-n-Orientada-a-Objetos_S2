class FileManager:
    def __init__(self, filename):
        """
        Constructor: Se llama automáticamente al crear una instancia de la clase.
        Inicializa el atributo 'filename' y abre el archivo.
        """
        self.filename = filename
        self.file = open(filename, 'w')
        print(f"Archivo '{self.filename}' abierto.")

    def write_to_file(self, content):
        """
        Método para escribir contenido en el archivo.
        """
        self.file.write(content)
        print(f"Escribiendo '{content}' en '{self.filename}'.")

    def __del__(self):
        """
        Destructor: Se llama automáticamente cuando todas las referencias al objeto se eliminan.
        Realiza tareas de limpieza cerrando el archivo.
        """
        self.file.close()
        print(f"Archivo '{self.filename}' cerrado.")


class DatabaseConnection:
    def __init__(self, db_name):
        """
        Constructor: Inicializa el atributo 'db_name' y simula una conexión a la base de datos.
        """
        self.db_name = db_name
        self.connected = True
        print(f"Conectado a la base de datos '{self.db_name}'.")

    def execute_query(self, query):
        """
        Método para ejecutar una consulta en la base de datos.
        """
        if self.connected:
            print(f"Ejecutando consulta: {query}")
        else:
            print("No hay conexión a la base de datos.")

    def __del__(self):
        """
        Destructor: Simula el cierre de la conexión a la base de datos.
        """
        self.connected = False
        print(f"Desconectado de la base de datos '{self.db_name}'.")


# Crear una instancia de FileManager y escribir en el archivo
file_manager = FileManager('example.txt')
file_manager.write_to_file('Hola, mundo!')

# Crear una instancia de DatabaseConnection y ejecutar una consulta
db_connection = DatabaseConnection('mi_base_de_datos')
db_connection.execute_query('SELECT * FROM usuarios')

# Eliminar las referencias a los objetos para llamar a los destructores
del file_manager
del db_connection
