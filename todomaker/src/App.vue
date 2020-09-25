<template>
  <div id="app">
    <div id = "headerbar">
      <p id = title>Todo Maker</p>
    </div>
    <div id = "main">
      <Todo :key="todo.id" @delete="deleteTodo"
          v-for="todo in todos"
          :todo="todo"/>
    </div>
    <input type="text" @keyup.enter="addTodo"
           v-model="newTodo"/>
    <p style = 'font-size: 1em'> Enter a name to add a list </p>
  </div>
</template>

<script>
import Todo from './components/Todo.vue'

export default {
	name: 'App',
  components: {
    Todo
  },
	data() {
		return {
			todos: [],
			newTodo: ""
		};
	},
	mounted () {
		fetch("http://localhost:8000/api/todo/")
			.then(response => response.json())
			.then(todolists => {
				console.log(todolists);
				this.todos = todolists;
			});
	},
	methods: {
		addTodo () {

      const formData = new FormData();
      formData.append('name', this.newTodo);

      fetch('http://localhost:8000/api/todo/', {
          method: 'POST',
          body: formData
      }).then(response => response.text())
      .then(data => console.log(data))

			this.todos.push({name: this.newTodo});
      this.newTodo = ""
		},
		deleteTodo (todo) {

      fetch('http://localhost:8000/api/todo/' + todo.id + '/', {
        method: 'DELETE',
      }).then(res => res.json())
        .then(res => console.log(res))

			this.todos = this.todos.filter(
				(x) => x.name != todo.name
			);
		}
	}
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#headerbar {
  width: 100%;
  height: 5vh;
  box-shadow: 0px 2px #ccc;
    -moz-box-shadow: 0px 2px #ccc;
    -webkit-box-shadow: 0px 2px #ccc;
    -khtml-box-shadow: 0px 2px #ccc;

      }

  #title{
    font-size: 2em;
    font-family: Avenir;
    text-align: left;
    height: 5vh;
    margin-left: 3%;
  }

  #body{
    margin: 0;
    display: block;
  }

  #main{
    display: flex;
    flex-wrap: wrap;
  }
</style>
