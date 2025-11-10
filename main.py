
from datetime import datetime

from core.core_functs import add_task, list_tasks, del_task

if __name__ == "__main__":
    
    while True:
        cmd = input('Chose action (Add/Update/Delete/List/Exit): ').strip().lower()

        match cmd:
            case 'add':
                des = input("Enter task description: ").strip()
                timestamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                status = 'to-do'
                add_task( des, status, timestamp)

            case 'list':
                list_tasks()

            case 'delete':
                dl = int(input("Please enter task ID: "))
                del_task(dl)

            case 'exit':
                print("Goodbye")
                break
            
            case _:
                print('Unknown input')
'''
            case 'update':

            case 'list':

            case 'delete':

            #case _:
                print('Unknown entry...')
'''