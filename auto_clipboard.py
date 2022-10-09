import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def save():
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

def load():
    key = input("Enter a key: ")
    if key in data:
        clipboard.copy(data[key])
        print("Data copied to clipboard.")
    else:
        print("Key does not exist.")

def delete():
    key = input("Entert a key")
    data[key] = " "
    save_data(SAVED_DATA, data)
    print("Data deleted!")



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        save()
    elif command == "load":
        load()
    elif command == "list":
        print(data)
    elif command == "delete":
        delete()
    else:
        print("Unknown command")
else:
    print("Please pass only one command.")


    

    