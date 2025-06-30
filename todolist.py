import streamlit as st # type: ignore

st.title("To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

def add_task():
    task = st.session_state.new_task.strip()
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ""

st.text_input("Aggiungi un nuovo task:", key="new_task", on_change=add_task)

tasks_to_keep = []

for i, task in enumerate(st.session_state.tasks):
    checked = st.checkbox(task, key=f"task_{i}")
    if not checked:
        tasks_to_keep.append(task)

st.session_state.tasks = tasks_to_keep

#per farlo partire python -m streamlit run todolist.py
