from pathlib import Path
import json

file = Path("./data/data.json")

if file.exists():
                with open(file, "r") as f:
                        tasks = json.load(f)
else:
        tasks = {}

def add_task(des: str, status: str, timestamp: str) -> str:
        ID = len(tasks) + 1
        while str(ID) in tasks:
                ID += 1
        tasks[ID] =  { 
                    'ID: ' : ID,
                    'des' : des, 
                     'status': status, 
                     'createdAt' : timestamp,
                     'updatedAt' : None
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

def del_task(dl: str):
        
        del tasks[dl]

        with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
        return print(f"Task deleted successfully! (ID: {dl})")

def update_task(task_id, des, timestamp):
        tasks[task_id]["des"] = des
        tasks[task_id]["updatedAt"] = timestamp
        with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
        return print(f"Task updated successfully! (ID: {task_id})")

def mark_task(task_id, status, timestamp):
        tasks[task_id]["status"] = status
        tasks[task_id]["updatedAt"] = timestamp
        with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
        return print(f"Task marked as {status} successfully! (ID: {task_id})")
        
        



#def update_task():

#def del_task():

#def list_task():