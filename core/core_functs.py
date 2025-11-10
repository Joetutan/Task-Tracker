from pathlib import Path
import json

file = Path("./data/data.json")

if file.exists():
                with open(file, "r") as f:
                        tasks = json.load(f)
else:
        tasks = {}

ID = len(tasks) + 1

def add_task(des: str, status: str, timestamp: str) -> str:

        tasks[ID] =  { 
                    'ID: ' : ID,
                    'des' : des, 
                     'status': status, 
                     'createdAt' : timestamp,
                     'updated' : None
                        }
        with open(file, "w") as f:
                json.dump(tasks, f, indent=4)
                        
                
        return print(f"Task added successfully! (ID: {ID})")

def list_tasks():
        if tasks:
                for i in tasks:
                        print(f"{i} : {tasks[i]['des']}")
        else:
                print('Please add tasks..')

def del_task(dl):
        if isinstance(dl, int):
                del tasks[dl]
        else:
                print("Please enter a number")
        



#def update_task():

#def del_task():

#def list_task():