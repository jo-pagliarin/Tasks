import sqlite3
conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()


def inicializa():
    cursor.execute("""--sql
    CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            dtCriacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            concluido BIT default 0
    );
    """)
    
def converte_tarefa(tarefaTupla):
    tarefaDict = {
        'id': tarefaTupla[0], 
        'descricao': tarefaTupla[1],
        'dtCriacao': tarefaTupla[2],
        'concluido': True if tarefaTupla[3] == 1 else False
    }
    return tarefaDict


def criar_tarefa(descricao: str):
    cursor.execute("""--sql
    INSERT INTO tarefas(descricao) VALUES (?);
    """, [descricao])
    conn.commit()
    
    cursor.execute("""--sql
    SELECT * FROM tarefas WHERE id = (SELECT LAST_INSERT_ROWID() AS id FROM tarefas);
    """)
    tarefaTupla = cursor.fetchall()[0]
    return converte_tarefa(tarefaTupla)

def obter_tarefas():
    cursor.execute("""--sql
    SELECT * FROM tarefas;
    """)
    tarefas = map(converte_tarefa, cursor.fetchall())    
    return list(tarefas)

def buscar_tarefa(id:int):
    cursor.execute("""--sql
    SELECT * FROM tarefas WHERE id = (?);
    """, [id])
    
    tarefas = cursor.fetchall()
    if len(tarefas) == 0:
        return None
    return converte_tarefa(tarefas[0])
   
def deletar_tarefas(id: int):
    cursor.execute("""--sql
    DELETE FROM tarefas WHERE id = (?);
    """, [id])
    conn.commit()
    

def completar_tarefa(id: int):
    cursor.execute("""--sql
    UPDATE tarefas
    SET concluido = 1
    SET descricao = "teste"
    WHERE id = (?);
    """, [id])
    conn.commit()


inicializa()
