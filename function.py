
# if we give FILEPATH= "todos.txt" in first line then we can replace filepath="todos.txt" with FILEPATH=filepath
# then we can easily change th variable 


def get_todos(filepath="todos.txt"):

    """Read a text file and return  
    """
    with open(filepath,'r') as file_local:
                todos_local=file_local.readlines() 
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
      with open(filepath,'w') as file_whatever:
            file_whatever.writelines(todos_arg)



# Now this will get printed if we call in this function 
# But if we call in the other function wher this two lin is ther it wont be printed
# 

print(__name__)


if __name__=="__main__":
    print("Hello from funtions") 
    print(get_todos()) 
    