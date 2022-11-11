<script setup>
import { ref } from 'vue'

const tarefas = ref([])
const descricao = ref("")

async function carregar_tarefas() {
  const resposta = await fetch("http://localhost:8000/api/tarefa")
  const novasTarefas = await resposta.json()

  tarefas.value = novasTarefas
}

async function criar() {
  if (descricao.value.length == 0){
    document.getElementById("descricao").placeholder = "Digite uma tarefa" 
  }
  else{
    const descricaoFormatada = encodeURIComponent(descricao.value)
    await fetch(`http://localhost:8000/api/tarefa?descricao=${descricaoFormatada}`, { method: "POST" })
    await carregar_tarefas()
  }
}

async function concluido(tarefa) {
  await fetch(`http://localhost:8000/api/tarefa/${tarefa.id}`, { method: "PATCH" })
  await carregar_tarefas()
}

async function deletar(tarefa) {
  await fetch(`http://localhost:8000/api/tarefa/${tarefa.id}`, { method: "DELETE" })
  await carregar_tarefas()
}

carregar_tarefas()
</script>

<template>
  <div class="container">
    <h1>- - To Do List - -</h1>
    <input id="descricao" class="descricao" type="text" v-model="descricao" placeholder="Escreva sua tarefa aqui..."><br />
    <button  class="btn-submit" type="submit" @click="criar()">Adicionar tarefa</button><br /><br />
    <div  v-for="tarefa in tarefas" :key="tarefa.id">
      <div class="row">
        <div class="col-1">
          <input type="checkbox" v-model="tarefa.concluido" @change="concluido(tarefa)" />
          <!-- <label for="checkbox"><i class="fa fa-check" aria-hidden="true"></i></label> -->
        </div>
        <div class="tarefa col-5">
          <div id="task">{{ tarefa.descricao }}</div>
        </div>
        <div class="data col-5">
          {{ tarefa.dtCriacao }}
        </div>
        <div class="col-1">
          <button type="submit" class="btn-delete" @click="deletar(tarefa)">X</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
body {
  color: rgb(255, 225, 225);
}

h1 {
  margin-top: 25px;
  text-align: center;
  font-family: courier;
  color: rgb(236, 42, 74);
}

.tarefa{
  font-family: georgia; 
  font-weight: bolder;
  letter-spacing: 3px;
}

.data{
  font-family: courier; 
}

.container {
  text-align: center;
}

.descricao {
  border-radius: 25px;
  height: 150px;
  width: 600px;
  text-align: center;
  font-family: georgia;
  cursor: pointer; 
}

.btn-submit {
  font-family: georgia;
  border-radius: 25px;
  border-color: rgb(236, 42, 74);
  width: 600px;
  letter-spacing: 3px;
  margin-top: 5px;
}

button:hover{
  transform: scale(1.1);
  transition: all 0.3s;
}

.btn-delete {
  border: none;
  background-color: rgb(255, 225, 225);
  font-family: georgia;
  font-weight: bolder;
}

/* input[type="checkbox"] {
  position: absolute;
  z-index: -1;
  opacity: 0;
}

input[type="checkbox"] + label {
  position: relative;
  cursor: pointer;
  padding-left: 100px;
  color: rgb(236, 42, 74);
} */

/* .teste{
  text-decoration: line-through;
} */

</style>
