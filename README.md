# TodoMaker

## Général

![](https://img.shields.io/badge/vue.js-4.5.6-blue?style=flat&color=green&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACQAAAAfCAYAAACPvW%2F2AAAABGdBTUEAALGPC%2FxhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA%2FwD%2FAP%20gvaeTAAAAB3RJTUUH5AoGCTkgFOEitAAABAZJREFUWMO1l09oXEUcxz8z78%2FuZv9kl0ZMoTkkoIuFSrckeOhB48VoI0VyEfzX3kqvHiWnHov%2FqFVQPBQi9mCxFUpbUWMUK6KQQwULBVMI%20F9a0xjXze4bD2%2F2ZffNvN23if3BwHszvz%2Ff%20c5v5jcjpi%20fuAQ8RlwENL69xb9f%2FSEsY7cR4ing8%208unukamjz0AsAjKPUhinLcNHNwRPlTFVDY5IoETgK%2FhRC6m1stCjmSMY0VZZQ6jmRoau5o1D01dxQkQyh13ACjQI5kcKtFYYulMZyUwBJwhnhYBbLk4tfK4JgkoZilpWbVneZW150mtNQsillD3xH4tTKy5NrYURrDkpi%20fAJgHLgIPGBoNgLql36h%20eM6yBgwwTdIcVg44lcA1VL3EqgLKB7q0gsU7kSB7BOjCE%2FaluoH4BCwIhdn5smt1VaAU8CmkS5ZB%2F9AGZFzbEs3SaCOCF8KfCkI1BEUk%2FG5i5z2kXFsYDaBU0HQWlmcmUcC%2FFNaBjgLfGmoBwpnzxButWhz5qA4Fmy0qmqjVUVxDDCiutUizp4hCKyZ%2FAXwvpSOdgjcXFhk%2FNlH68DvwJNApstEgix5tG5uoOpBmIJbUgZywEFgOs6OLHtkH74Hkbeyswa8CHy%2FODPfDtUlnwLnDDMFcpeP9%20BwHEx7%2FHkUzxn9Arx9w8hdftI2%2F0DH7Jx7KBphA3gNWLVZe3tLOLuzNueebl2TcHZn8faWSJBV4HWg0WbHYEgPXAPeAYJ4AJF38WsV8AR9xRP4tQoib93mAfA2cK0TjAFoKzTvAsumG4U7kccdzyclaIdeAXciUW9ZxzAGDUAa8U%20ES1c3XLkC%2F0AFUXDteaFAFPSB6lqZrAOvAj%2FH2UliqC3ngSu2gM5oz9wIc200m1ivtG%20rWAFp5OvAK8CfhkLS7mnvxn0JuzH09TLwt42dfgwBXAUWbCzJYQ9%2Ff7nbgwR%2Ffxk57CWxswB83StgIiA9gyZwGrhh03HvL%20KM6RM4UDhjiSc62sdpoJnETl%20GtGHkKM5SWKMqiIyDyOjvrGNjpwm8AdzoBaYvoL5UBwp3LId7XyFsY7mkbX4VeC9NoBQnHOgrymENrBD3EPwVXhIScmcdeAb4qB87gzAE4Xa9YPTqBO%20RyOeBj9MGSQVIzyw60GygEsBEB2wadgZiSIQBE498i0QlKBhgIVJrfvb4PHQUxRQmUZFemnnp%2FwcE0dKtEi5Do4dqdI1Ju1TbAtQh54hdrGLyCbaL3t0ApGe8RliTbltUbumxtUHZ2QlDoC%2Fnln77Y%20FuAtIz3yR8Oq10DEXPqe2wsyOGdMDrwFtAS7c3gevbBQPgbtsylPYTeE7%2Fm0%2FyASVVLeslus49rX%2FP7oQdgP8AvRNH20La3U4AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMTAtMDZUMDk6NTc6MzItMDQ6MDBuX%20sDAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTEwLTA2VDA5OjU3OjMyLTA0OjAwHwJTvwAAAABJRU5ErkJggg%3D%3D&fbclid=IwAR2m3eEbNxiMZr-f-kqGUJdgx7-qF7t8zO6zyZQ41OAFBAPYIJdef3mWDtI)![](https://img.shields.io/badge/django-3.1.1-white?style=flat&color=red&logo=python&logoColor=white)

TodoMaker est une application de todo-liste réalisée dans le cadre d'un test technique pour un recrutement chez Think Deep. Il s'agit d'une application web réalisée en deux parties, un front en [Vue.js](https://vuejs.org/) supporté par une API restful créée avec [Django REST framework](https://www.django-rest-framework.org/).  

## Installation

### Prérequis

Ce projet nécessite [python 3+](https://www.python.org/downloads/) ainsi que Vue.js pour fonctionner. Des packages supplémentaires tels que djange-rest-framework ou encore vue-cli peuvent êtres demandés. Afin de l'éxecuter, réaliser les étapes suivantes:

#### Back-end

Télécharger le projet :

```shell
$ git clone https://https://github.com/saudrix/TodoMaker
```

Se placer dans le dossier 

```shell
$ cd TodoMaker_Backend
```

Executer le *back* selon le système (*resp windows/unix*)

```shell
$ py manage.py runserver
```

```bash
$ python3 manage.py runserver
```

Pour tester que le server est bien lancé et que l'API fonctionne, vous pouvez vous rendre à [l'url](http://localhost:8000/api/) suivante.

#### Front-end

Ensuite se placer dans le dossier

```shell
$ cd ..\todomaker
```

 lancer le front en exécutant l'une des commandes suivantes :

```shell
$ npm run serve
$ yarn serve
```

pour vérifier que l'application est bien lancée, vous pouvez vous rendre à [l'url](http://localhost:8080)

## Architecture



------

------

### Todo

[ ] API 

[x] Tests

