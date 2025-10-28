// Ejercicio 2: Crear un sistema simple de gestión de tareas

function createTaskManager() {
    let tasks = [];
    let newId = 1;

    return {
        addTask: function(task) {
            if (typeof task === 'string' && task.trim() !== '') {
                const newTask = {
                    id: newId++,
                    description: task.trim(),
                    completed: false
                };
                tasks.push(newTask);
                console.log(`Tarea agregada: "${task}" (ID: ${newTask.id})`);
            } else {
                console.log("Vuelve a escribir la tarea, no se encontró texto");
            }
        },

        completeTask: function(taskId) {
            const task = tasks.find(t => t.id === taskId);
            if (task) {
                task.completed = true;
                console.log(`Felicitaciones tarea completa: "${task.description}"`);
            } else {
                console.log(`No se encontró una tarea con el ID: ${taskId}`);
            }
        },

        listTasks: function() {
            if (tasks.length === 0) {
                console.log("No hay tareas pendientes...");
                return;
            }
            
            console.log("--LISTA DE TAREAS--");
            tasks.forEach(task => {
                const status = task.completed ? "✅" : "⏳";
                console.log(`${status} [ID: ${task.id}] ${task.description}`);
            });
        }
    };
}


const myTasks = createTaskManager();

myTasks.addTask("Entregar este trabajo a tiempo");
myTasks.addTask("Presentar Trabajo final antes del 10/11");
myTasks.addTask("Presentar Trabajo de ingles antes del 06/11");
myTasks.addTask("Aprobar el semestre con honores");
myTasks.addTask();
myTasks.listTasks();
myTasks.completeTask(1);
myTasks.listTasks();