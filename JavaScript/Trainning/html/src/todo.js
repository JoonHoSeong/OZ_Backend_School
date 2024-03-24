// 요소 선택 및 배열 선언
const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
let todoArr = [];

// displayTodos 함수
function displayTodos(){
  todoList.innerHTML = ""
  todoArr.forEach((aTodo) => {
    const todoItem = document.createElement('li')
    const todoDelBtn = document.createElement('span')
    todoDelBtn.innerText = 'x'
    todoDelBtn.title = '클릭시 삭제'
    todoItem.innerText = aTodo.todoText
    todoItem.title = '클릭시 완료'
    todoItem.classList.add(aTodo.todoDone ? 'done' : 'yet')
    todoItem.appendChild(todoDelBtn)
    todoDelBtn.addEventListener('click', function(){
      handleTodoDelBtnClick(aTodo.todoId)
    })
    todoItem.addEventListener('click', function(){
      handleTodoItemClick(aTodo.todoId)
    })
    todoList.appendChild(todoItem)
  });
}

// handleTodoDelBtnClick 함수
function handleTodoDelBtnClick(clickedId){
  todoArr = todoArr.filter(function(aTodo){
    return aTodo.todoId !== clickedId
  })
  displayTodos()
  saveTodos()
}

// handleTodoItemClick 함수
function handleTodoItemClick(clickedId){
  todoArr = todoArr.map(function(aTodo){
    return aTodo.todoId !== clickedId ? 
    aTodo : { ...aTodo, todoDone: !aTodo.todoDone } 
  })
  displayTodos()
  saveTodos()
}

// saveTodos 함수
function saveTodos(){
  const todoSting = JSON.stringify(todoArr)
  localStorage.setItem('myTodos', todoSting)
}

// loadTodos 함수
function loadTodos(){
  const myTodos = localStorage.getItem('myTodos') 
  todoArr = myTodos !== null ? JSON.parse(myTodos) : todoArr
  displayTodos()
}

// 할일 입력 후 제출하면 발생하는 이벤트 핸들링
todoForm.addEventListener('submit', function(e){
  e.preventDefault()
  const toBeAdded = {
    todoText: todoForm.todo.value,
    todoId: new Date().getTime(),
    todoDone: false
  }
  todoForm.todo.value = ""
  todoArr.push(toBeAdded)
  displayTodos()
  saveTodos()
})

loadTodos() // 시작할 때 한번만!