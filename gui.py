import function
import PySimpleGUI
import time
import os

# if todos.txt doesnt exist then, when the user run SAE only first time they run the prog file will be generated
# if file already exist then it wont be generated
if not os.path.exists("todos.txt"):
     with open("todos.txt","w") as file:
          pass   
     
# standalon executable is above SAE

# PySimpleGUI.theme('DarkTeal2')
clock=PySimpleGUI.Text('', key='clock')
label=PySimpleGUI.Text("Type in a Todo")
inpu_box=PySimpleGUI.InputText(tooltip="enter todo", key="todo")
add_button=PySimpleGUI.Button("Add", size=10)
# two instances
# tooltip to show what cursor should show when keep ther
# key todo is the key in key value pair of the tuple in event in the window.read()

list_box=PySimpleGUI.Listbox(values=function.get_todos(), key='todos' , 
                             enable_events=True , size=[45,10])
edit_button=PySimpleGUI.Button("Edit")
complete_button=PySimpleGUI.Button("Complete")
exit_button=PySimpleGUI.Button("Exit")

window=PySimpleGUI.Window('My To-do app', 
                          layout=[[clock],
                                 [label],
                                 [inpu_box,add_button],
                                 [list_box,edit_button,complete_button],
                                 [exit_button]], 
                          font=('Helvetica', 15))

# the object we put inside inner [] will be in same row 
# if we put [] [] seperately them=n it will be in row wise    

# print(event,vlaue) -> this prints event value tuple.
while True:
    event, values =window.read(timeout=200)
    # we gave timeout bcs otherwise loop runs only when an event happens
    window['clock'].update(value=time.strftime("%b %d %Y, %H %M %S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos=function.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            # print(todos)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
             try:   
                # print(values['todos'])
                todo_to_edit= values['todos'][0]
                new_todo=values['todo']

                todos=function.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo

                function.write_todos(todos)

                window['todos'].update(values=todos)
                
             except IndexError:
                    #  print("please select an item first")
                    PySimpleGUI.popup("please select an item first", font=("Helvetica",20))

            # In the provided code, the line window['todos'].update(values=todos) is using the correct keyword argument,
            #  which is values. This is because values is the correct keyword argument to update the values of a Listbox in PySimpleGUI.
        case "Complete": 
                try:
                    todo_to_complete=values['todos'][0]
                    todos=function.get_todos()
                    todos.remove(todo_to_complete)
                    function.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                    # update method for an InputText element in PySimpleGUI uses the keyword argument value, not values.
                
                except IndexError:
                     PySimpleGUI.popup("please select an item first", font=("Helvetica",20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case PySimpleGUI.WIN_CLOSED:
            break



print("bye")
window.close()

