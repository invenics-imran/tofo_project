
import streamlit as st
# streamlit is for making web apps
import function 


todos=function.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    print(todo)
    todos.append(todo)
    function.write_todos(todos)
     
 
 

st.title("My to-do app")
st.subheader("This is my todo app")
st.write("thi is productivity") 

for todo in todos:
    st.checkbox(todo)

st.text_input(label="new todo", placeholder="Add new todo...", on_change=add_todo, key='new_todo')adfet5t   errge