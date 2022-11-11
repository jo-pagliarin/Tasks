<script setup>
import { ref } from 'vue'
// import { createApp } from 'vue'
// import App from './App.vue'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// createApp(App)
// .component('font-awesome-icon', FontAwesomeIcon)
// .mount('#app')

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
  descricao.value = ""
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
          <label class="caixa">
            <input class="checkbox" type="checkbox" v-model="tarefa.concluido" @change="concluido(tarefa)" />
          <span class="checkmark"></span>
          </label>
        </div>
        <div class="tarefa col-5">
          <s v-if="tarefa.concluido">{{ tarefa.descricao }}</s>
          <p v-else>{{ tarefa.descricao }}</p>
          
        </div>
        <div class="data col-5">
          {{ tarefa.dtCriacao }}
        </div>
        <div class="col-1">
          <button type="submit" class="btn-delete" @click="deletar(tarefa)">X
              <!-- <div id="app">
                <font-awesome-icon icon="fa-light fa-delete-left"/>
              </div> -->
          </button>
        </div>          
      </div>
    </div>
  </div>
  
</template>

<!-- <script>
  export default {
    name: 'App'
  }
</script> -->


<style scoped>

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
  background-color: rgb(241, 228, 228);
  border-radius: 25px;
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
  border-color: black;
  width: 600px;
  letter-spacing: 3px;
  margin-top: 5px;
  background-color: rgb(236, 42, 74);;
}

button:hover.btn-submit{
  transform: scale(1.1);
  transition: all 0.3s;
}

button:hover.btn-delete{
  transform: scale(1.5);
  transition: all 0.3s;
}

.btn-delete {
  border: none;
  background-color: rgb(255, 225, 225);
  font-family: georgia;
  font-weight: bolder;
}

.caixa {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 6px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  font-size: 16px;
}
/* Hide the browser's default checkbox */
.caixa input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 21px;
  width: 21px;
  border-radius: 2px;
  background-color: rgb(236, 42, 74);
  border: 1px solid #ccc;
}
/* On mouse-over, add a grey background color */
.caixa:hover input ~ .checkmark {
  background-color: rgb(236, 42, 74);;
  transform: scale(1.5);
  transition: all 0.3s;
}

.caixa input:checked ~ .checkmark {
  background-color: rgb(236, 42, 74);
}
/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}
/* Show the checkmark when checked */
.caixa input:checked ~ .checkmark:after {
  display: block;
}
/* Style the checkmark/indicator */
.caixa .checkmark:after {
  left: 7px;
  top: 0px;
  width: 7px;
  height: 15px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}


</style>
