
from datetime import datetime
from core.core_functs import add_task, list_tasks, del_task, update_task, mark_task

if __name__ == "__main__":
    
    while True:
        cmd = input('Chose action (Add/Update/Mark/Delete/List/Exit): ').strip().lower()
        timestamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        match cmd:
            case 'add':
                des = input('Enter task description:... ').strip()
                status = 'to-do'
                add_task( des, status, timestamp)

            case 'list':
                list_tasks()

            case 'delete':
                task_id = input("Please enter task ID: ")
                del_task(task_id)

            case 'exit':
                print("Goodbye")
                break

            case 'update':
                task_id = input("Please enter task ID: ")
                change = input("Enter update:... ")
                update_task(task_id, change, timestamp)
            case 'mark':
                s = {"to-do","in-progress", "done"}
                task_id = input("Please enter task ID: ")
                status = input("mark-task: \n to-do \n in-progress \n done \n")
                if status in s:
                    mark_task(task_id , status, timestamp)
                else:
                    print('wrong entry please try again')
            case _:
                print('Unknown input')
