
from datetime import datetime

from core.core_functs import add_task, list_tasks, del_task

if __name__ == "__main__":
    
    tasks = {}
    IDs = []
    

    while True:
        cmd = input('Chose action (Add/Update/Delete/List): ').strip().lower()

        match cmd:
            case 'add':
                des = input("Enter task description: ").strip()
                timestamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                IDs.append(None)
                ID = len(IDs)
                status = 'to-do'
                add_task( tasks, ID, des, status, timestamp)
            case 'list':
                list_tasks(tasks)
            case 'delete':
                dl = int(input("Please enter task ID: "))
                del_task(tasks, dl)
            
            case _:
                print('Unknown input')
'''
            case 'update':

            case 'list':

            case 'delete':

            #case _:
                print('Unknown entry...')
'''