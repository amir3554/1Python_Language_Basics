from .Task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace



class TaskController():
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def add_task(self, args):
        #task initializtion from sys args
        task = Task(args.title, args.description, args.start_date, args.end_date, args.done)
        
        #1 start date if it wasn't included   
        if task.start_date is None:
            now = date.today().isoformat()
            task.start_date = now
        
        #open file and save info 
        with open(self.file_name, 'a') as file:
            file.write(str(task) + '\n')

    def unfinished_list_tasks(self):
        unfinished_tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')#خاصية فك التحزيم
                                                                            #تعيد الدالة  سبليت قائمة من العناصر الناتجة من عملة فصل السطر بواسطة ما داخل القوسين
                                                                            #ستؤدي عملية فك التحزيم الى ارجاع قائمة و اسناد جميع القيم فيها الى هذه المتغيرات
                end_date = None if end_date == 'None' else end_date 
                done = False if done.strip('\n')=='False' else True
                if done:
                    continue
                unfinished_tasks.append({"Title": title,"description":description,"start_date":start_date, "end_date":end_date})
        return unfinished_tasks


    def list_all_tasks(self):
        tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')
                end_date = None if end_date == 'None' else end_date 
                done = False if done.strip('/n')=='False' else True
                tasks.append({"Title": title,"description":description,"start_date":start_date, "end_date":end_date, 'done': done})
        return tasks

    def due_date(self, start, end):
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        delta_date =  end_date - start_date 
        return f'{delta_date.days} days left.'
    
    def print_table(self, tasks):
        formatted_tasks = []
        for number, task in enumerate(tasks, 1):
            if task['start_date'] and task['end_date']:
                due_date = self.due_date(task['start_date'] ,task['end_date'])
            else:
                due_date = 'open'
            formatted_tasks.append({'id':number, **task, 'due_date':due_date})
        print(tabulate(formatted_tasks,headers='keys'))

    def Display(self, args):
        all_tasks = self.list_all_tasks()
        unfinished_tasks = self.unfinished_list_tasks()

        if not all_tasks:
            print("There are no tasks, To add a tasks use add <task> .")
            return
        if args.all:
            self.print_table(all_tasks)
        else:
            if unfinished_tasks:
                self.print_table(unfinished_tasks)
            else:
                print("All the tasks are checked! . ")

    def check_task(self, args):
        index = int(args.task)
        tasks = self.list_all_tasks()
        if index <= 0 or index > len(tasks):
            print(f"task number ({index}) does not exist. ")
            return
        tasks[index -1]['done'] = True
        with open(self.file_name, 'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def remove_task(self, args):
        tasks = self.list_all_tasks()
        if args.task :
            index = args.task
        else:
            index = len(tasks ) -1 

        if index < 0 or index > len(tasks):
            print(f"task number ({index}) does not exist. ")
            return
        
        tasks.pop(index - 1)
        with open(self.file_name, 'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def reset(self, *args):#لتجب حدوث خطا في عدد المعاملات الموقعية
        with open(self.file_name) as file:
            file.write('')            
        print("All tasks has been cleared, You have deleted all tasks . ")

