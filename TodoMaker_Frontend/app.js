var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

var urlencoded = new URLSearchParams();
urlencoded.append("senderId", "1");
urlencoded.append("receiverId", "3");
urlencoded.append("lastDate", "2020-04-01 15:22:15");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};



const getItems = () =>
  fetch("http://localhost:8000/item", requestOptions)
    .then(response => response.json())
    .then(result => {return result, console.log(result)})
    .catch(error => console.log('error', error));

let Item = {
  props:{
    value: ""
  },

  template: `<div> {{value}} </div>`
}


let vm = new Vue({
  el: '#app',

  data: {
    roger: [],
    todos: [
      {name:'test1',add:''},
      {name:'test2',add:''},
      {name:'test3',add:''},
    ]
  },

  mounted(){
    this.roger = getItems()
  },

  computed:{},

  methods:{

    alertColor(color){
      alert('best color = ' + color)
    },

    addItem(id,item){
      console.log(id + item)
      this.todos[id].add = item,
      this.roger = ''
    },
  }
})
