from pathlib import Path
from datetime import datetime
import json



# check if file exists in dir. Read file and assign to tasks if true else create new dict 
file = Path("./data/data.json") # dir to save and retreive json file

if file.exists(): 
        with open(file, "r") as f:
                    tasks = json.load(f)
else:
        tasks = {}
    

# keep record of current timestamp
timestamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

def add_task(des: str) -> str:
        '''
        -Assign unique task ID.
        -Increment ID in while loop to avoid assigning duplicate key after deletion.
        -Assign status 'to-do' as default for new tasks.
        -Write to json file after updating task properties.
        -Print success message to cli
        '''
        ID = len(tasks) + 1 
        while str(ID) in tasks:
                ID += 1

        status = 'to-do' 
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

def list_tasks(task_property):
        '''
        -List tasks with matching task property in dict sorted by Unique IDs
        '''
        
        s = {'all', 'to-do', 'in-progress', 'done'}
        if task_property not in s:
                print("Invalid input: please try again")
                return "fail"
        if not tasks:
                print('Please add tasks..')
                return "pass"
        
        match task_property:
                case 'all':
                        
                        for i in sorted(tasks, key=lambda x: int(x)):
                                print(f"{i} : {tasks[i]['des']}")
                        return "pass"
                
                case 'to-do':
                        count = sum(t['status'] == task_property for t in tasks.values())
                        if count > 0:
                                list_helper(task_property)
                        else:
                                print("None...")
                                return "pass"
                
                case 'in-progress':
                        count = sum(t['status'] == task_property for t in tasks.values())
                        if count > 0:
                                list_helper(task_property)
                        else:
                                print("None...")
                                return "pass"

                case 'done':
                        count = sum(t['status'] == task_property for t in tasks.values())
                        if count > 0:
                                list_helper(task_property)
                        else:
                                print("None...")
                                return "pass"

def list_helper(task_property):
        '''
                -Helper function for list_tasks() to avoid repetition
        '''
        for i in sorted(tasks, key=lambda x: int(x)):
                        if tasks[i]['status'] == task_property:
                                print(f"{i} : {tasks[i]['des']}")
        return "pass"
                
                        

def del_task(dl):
        '''
        -delete task with given ID key
        -update the change in json file
        -print success message  to cli
        '''
        while True:
                if dl not in tasks:
                        print(f"Task {dl} not found. Please try again")
                        return "fail"
                del tasks[dl]
                with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
                print(f"Task deleted successfully! (ID: {dl})")
                return "pass"

def update_task(task_id):
        '''
        -assign description property change for task with provided ID as key
        -update change updated timestamp
        -write change to json file
        -print success message
        '''
        while True:
                if task_id not in tasks:
                        print(f"Task {task_id} not found. Please try again")
                        return "fail"
                
                des = input("Enter update:... ")
                tasks[task_id]["des"] = des
                tasks[task_id]["updatedAt"] = timestamp

                with open(file, "w") as f:
                                json.dump(tasks, f, indent=4)
                print(f"Task updated successfully! (ID: {task_id})")
                return "pass"


def mark_task(task_id):
        '''
        -Validate input if true continue else print fail message
        -assign status property change for task with provided ID as key
        -update change updated time stamp
        -write change to json file
        -print success message
        '''
        while True:
                if task_id not in tasks:
                        print(f"Task {task_id} not found. Please try again")
                        return "fail"

                status = input("mark-task: (to-do/in-progress/done) ").strip().lower()
                s = {"to-do","in-progress", "done"}
                if status not in s :
                        print("Invalid input: please enter: (to-do/in-progress/done)")
                        continue
                
                tasks[task_id]["status"] = status
                tasks[task_id]["updatedAt"] = timestamp

                with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)

                print(f"Task marked as {status} successfully! (ID: {task_id})")
                return "pass"
                
                
                        
                                
                
                        




#def update_task():

#def del_task():

#def list_task():