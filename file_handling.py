from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"[i+1] : {items}")


def createfile():
    
    try:
        readfileandfolder()
        name = input("Please enter name of your file:-")
        p = Path(name)
        if not p.exist():
            with open(p,"w") as f:
                data = input("what you wantn to add:-")
                f.write(data)

            print("File Created Sucefully")
        else:
            print("this file already exist")
    except Exception as err:
        print(f"An error occured as:{err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Enter name of file:")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as f:
                data = f.read()
                print(data)
            print("sucesfully open a file")
        else:
            print("file did not exist")

    except Exception as err:
        print(f"an  error occured as {err}")

def updatefile():
    try:
            
        readfileandfolder()
        name = input("tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("tell  your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data :- ")
                    fs.write(data)
        
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" "+data)

    except Exception as err:
        print("an error occured as {err}")


def deletefile():
    try:

        readfileandfolder()
        name = input("whuich file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

    










print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please tell your respose:-"))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()