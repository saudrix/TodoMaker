<template>
  <div class="todo">
		<div class="header">
			{{ todo.name }}
        <img  @click="$emit('delete', todo)" class="closeBtn" src="../assets/closeBtn.png" />
		</div>
		<Item :key="item.id" @delete="deleteItem"
					v-for="item in items"
					:item="item"/>
    <div class = "footer">
      <input class = "itemInput"
             type="text" @keyup.enter="addItem"
             v-model="newItem"/>
      <p style = 'font-size: .7em'> Enter an item to add to the list </p>
    </div>
  </div>
</template>

<script>
import Item from './Item.vue'

export default {
	components: { Item },
  name: 'Todo',
  props: {
    todo: Object
  },
	data () {
		return {
			items: [],
      newItem: ''
		};
	},
  methods:{
    addItem () {

      const formData = new FormData();
      formData.append('descp', this.newItem);
      formData.append('status', false);
      formData.append('todo_id',this.todo.id);

      console.log(formData);

      fetch('http://localhost:8000/api/item/', {
          method: 'POST',
          body: formData
      }).then(response => response.text())
      .then(data => console.log(data))

      this.items.push({descp: this.newItem});
      this.newItem = ""
    },
    deleteItem (item) {

      fetch('http://localhost:8000/api/item/' + item.id + '/', {
        method: 'DELETE',
      }).then(res => res.json())
        .then(res => console.log(res))

			this.items = this.items.filter(
				(x) => x.descp != item.descp
			);
		}
  },
	mounted () {
		fetch("http://localhost:8000/api/item/")
			.then(response => response.json())
			.then(items => {
        console.log(items)
				this.items = items.filter(
					(i) => i.todo_id == this.todo.id
				);
			});
	},
}
</script>

<style scoped>
.todo {
  width: 18%;
  margin: 1%;
  box-shadow: 2px 2px #aaa;
  background: lightgray;
}

.header{
	background: gray;
	color: white;
  padding: 5px 0px;
  font-size: 1.5em;
  font-family: Avenir;
  position: relative;
}

.closeBtn{
  position: absolute;
  top: 8px; right: 10px;
  width: 15px;
  height:15px;
  cursor:pointer;
}

.itemInput{
  border-radius:20px;
  border:none;
  margin: none;
  padding: 2px;
}

.footer{
  margin: 5px 0px;
}

</style>
