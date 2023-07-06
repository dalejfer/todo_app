import mysql.connector

config = {'user': 'juan',
          'password': '123456',
          'host': '127.0.0.1',
          'database': 'todo'}

def conectar():
    conn = mysql.connector.connect(**config)
    return conn

# def create_database(self):
#     pass            

# def set_tarea(self, tarea):
#     pass

# def del_tarea(self, id_tarea):
#     pass

# def update_tarea(self, id_tarea, detalle):
#     pass

def get_tareas(tipo="all"):
    consulta = """SELECT id_tarea, tarea, completada
                    FROM tareas {}
                    ORDER BY creacion DESC"""
    where = "WHERE completada = {}"
    if tipo == "done":
        consulta = consulta.format(where.format("true"))
    elif tipo == "pending":
        consulta = consulta.format(where.format("false"))
    elif tipo == "all":
        consulta = consulta.format("")
    conn = conectar()
    cur = conn.cursor()
    cur.execute(consulta)
    resultado = cur.fetchall()
    conn.close()
    print(resultado)
    return resultado