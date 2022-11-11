from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/tarefa")
async def obter_tarefa():
    return database.obter_tarefas()

@app.post("/api/tarefa")
async def criar_tarefa(descricao: str):
    return database.criar_tarefa(descricao)

@app.delete("/api/tarefa/{id}")
async def deletar_tarefa(id: int):
    tarefa = database.buscar_tarefa(id)
    if tarefa is not None:
        database.deletar_tarefas(id)
        return f'{tarefa["descricao"]} deletada'
    return 'Tarefa não encontrada'


@app.patch('/api/tarefa/{id}')
async def completar_tarefa(id: int):
    tarefa = database.buscar_tarefa(id)
    if tarefa is not None:
        database.completar_tarefa(id)
