<template>
  <div class=item>
		<input type="checkbox" v-model="item.status" @click="Check"/>
		<p id = 'text'>{{ item.descp }}</p>
    <div>
        <img  @click="$emit('delete', item)" class="closeBtn" src="../assets/closeBtn.png" />
		</div>
	</div>
</template>

<script>
export default {
  name: 'Item',
  props: {
		item: Object
  },
	mounted () {
		console.log(this.item);
	},
  methods:{
    Check(){
      const formData = new FormData();
      formData.append('status', !this.item.status);
      formData.append('descp', this.item.descp);
      formData.append('todo_id', this.item.todo_id);

      fetch('http://localhost:8000/api/item/' + this.item.id +'/', {
          method: 'PUT',
          body: formData
      }).then(response => response.text())
      .then(data => console.log(data))
    },
  }
}
</script>

<style scoped>
.item {
  font-size: .8em;
	display: flex;
	justify-content: space-between;
	align-items: center;
  background: #bbb;
  border-radius: 20px;
  padding: 0px 5px;
  margin:10px;
}

.closeBtn{
 width: 15px;
 cursor: pointer;
 height:15px;
 margin-right: 10px;
}


</style>
