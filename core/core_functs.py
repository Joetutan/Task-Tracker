

def add_task(tasks, ID: int, des, status, timestamp) -> str:

        tasks[ID] = { 
                    'ID: ' : ID,
                    'Description: ' : des, 
                     'Status:': status, # type: ignore
                     'CreatedAt:' : timestamp, # type: ignore
                     'Updated:' : None # type: ignore
                        }



#def update_task():

#def del_task():

#def list_task():