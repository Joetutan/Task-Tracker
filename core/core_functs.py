

def add_task(tasks, ID: int, des: str, status: str, timestamp: str) -> str:

        tasks[ID] = { 
                    'ID: ' : ID,
                    'des' : des, 
                     'status': status, # type: ignore
                     'createdAt' : timestamp, # type: ignore
                     'updated' : None # type: ignore
                        }
        return print(f"Task added successfully! (ID: {ID})")


def list_tasks(tasks):
        if tasks:
                for i in range(len(tasks)):
                        print(f"{i+ 1} : {tasks[i+1]['des']}")
        else:
                print('Please add tasks..')

#def update_task():

#def del_task():

#def list_task():