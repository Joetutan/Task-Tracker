

from core.core_functs import add_task, list_tasks, del_task, update_task, mark_task


if __name__ == "__main__":

    
    while True:
        cmd = input('Choose action (Add/Update/Mark/Delete/List/Exit): ').strip().lower()
        
        match cmd:
            case 'add':
                des = input('Enter task description:... ').strip()
                add_task(des)

            case 'list':
                while True:
                    
                    task_property = input("Choose (all/to-do/in-progress/done): ").strip().lower()
                    result = list_tasks(task_property)
                    if result == "fail":
                        continue
                    else:
                        break
            case 'delete':
                while True:
                    try:
                        task_id = int(input("Please enter task ID: ").strip())
                        result = del_task(str(task_id))
                        if result == "fail":
                            continue
                        if result == "pass":
                            break
                    except ValueError:
                        print("Invalid input: please enter a number")
            case 'exit':
                print("Goodbye")
                break

            case 'update':
                while True:
                    try:
                        task_id = int(input("Please enter task ID: ").strip())
                        update_task(str(task_id))
                        break
                    except ValueError:
                        print("Invalid input: please enter a number")

            case 'mark':
                while True:
                    try:
                        task_id = int(input("Please enter task ID: "))
                        result = mark_task(str(task_id))
                        if result == "fail":
                            continue
                        if result == "pass":
                            break
                    except ValueError:
                        print("Invalid input: please enter a number")


            case _:
                print('Unknown input')
