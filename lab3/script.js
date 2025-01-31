const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const todoList = document.getElementById('todoList');

// Add Task
addTaskBtn.addEventListener('click', () => {
    const taskText = taskInput.value.trim();
    if (taskText !== '') {
        const li = document.createElement('li');
        li.className = 'todo-item';

        li.innerHTML = `
                    <span>${taskText}</span>
                    <div>
                        <input type="checkbox" class="mark-done">
                        <button class="delete-btn">&#128465;</button>
                    </div>
                `;

        todoList.appendChild(li);
        taskInput.value = '';
    }
});

// Mark as Done or Delete Task
todoList.addEventListener('click', (e) => {
    if (e.target.classList.contains('mark-done')) {
        const task = e.target.closest('.todo-item');
        task.classList.toggle('done');
    } else if (e.target.classList.contains('delete-btn')) {
        const task = e.target.closest('.todo-item');
        todoList.removeChild(task);
    }
});