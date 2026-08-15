import functions
import streamlit as st

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write(
    "This app is to increase your <strong>productivity</strong>.",
    unsafe_allow_html=True,
)

st.text_input(
    label="New todo", placeholder="Add a new todo..", on_change=add_todo, key="new_todo"
)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

st.session_state
