import json


if __name__ == "__main__":

    data = {
        1:{
                    'ID: ' : 1,
                    'des' : 'des 1',
                     'Status:': 'todo',
                     'CreatedAt:' : 3,
                     'Updated:' : None
                        },
    2:{
                    'ID: ' : 2,
                    'des' : 'des 2',
                     'Status:': 'todo',
                     'CreatedAt:' : 3,
                     'Updated:' : None
                        },
    3:{
                    'ID: ' : 3,
                    'des' : 'des 3',
                     'Status:': 'todo',
                     'CreatedAt:' : 3,
                     'Updated:' : None
                        }
    }

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("File written to file successfully!")

    