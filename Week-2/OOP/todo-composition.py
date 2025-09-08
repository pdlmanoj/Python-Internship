class Task:

    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = 'DONE' if self.done else 'NOT DONE'
        return f"{self.title} -> {[status]}"
    

class TaskManager:

    def __init__(self):
        self.task = []
    
    def add_task(self, title):
        task = Task(title)
        self.task.append(task)

    def mark_task(self, index):
        if index >= 0 and index < len(self.task):
            self.task[index].mark_done()
    
    def list_task(self):
        for i in self.task:
            print(i)

c1 = TaskManager()
c1.add_task('Task1')
c1.add_task('Task2')
c1.add_task('Task5')
c1.mark_task(0)
c1.list_task()

