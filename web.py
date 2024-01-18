
import streamlit as st
# streamlit is for making web apps
import function 


todos=function.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    print(todo)
    todos.append(todo)
    function.write_todos(todos)
     
#session state will give a dictionary that has value entere in text box
    
 

st.title("My to-do app")
st.subheader("This is my todo app")     
st.write("thi is productivity") 

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    #print(checkbox)
    if checkbox:
        #print(checkbox)
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="new todo", placeholder="Add new todo...", on_change=add_todo, key='new_todo') 

# key is a unique id to represent value in the text box
# on_change will be a calllback function whicj is a custom function to call in the the same code, to call on change, and make sure cursor in todo.txt is in new line
# instead of end of last line otherwise it will be appended to last line

st.session_state

#if we give st.checkbox(todo,key="hello") then hello will give false in dictionary when rendered bcs same key for all checkbox
#so we make it dynamic by giving each todo its own name as key by makeing st.checkbox(todo,key=todo)

