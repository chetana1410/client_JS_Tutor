import streamlit as st
from streamlit_chat import message
from utils import get_subtopics, get_concepts, get_learning_outcome, send_info, chat, declare_state, get_blooms_level

    
# Streamlit app with sidebar
def main():
    # Initializing state
    declare_state()

    st.sidebar.title("Select the below entries and start the training")

    # Choose Topic in the sidebar
    selected_topic = st.sidebar.selectbox("Choose Topic", ['JavaScript'])

    # Choose Subtopic in the sidebar
    selected_subtopic = st.sidebar.selectbox("Choose Subtopic", get_subtopics())

    # Choose Concept in the sidebar
    selected_concept = st.sidebar.selectbox("Choose Concept", get_concepts(selected_subtopic))

    # Slider for Bloom's Level
    blooms_level = st.sidebar.select_slider("Bloom's Level", options=get_blooms_level())

    # Slider for Learning Outcome
    learning_outcome = st.sidebar.selectbox("Choose Learning Outcome", get_learning_outcome(blooms_level,selected_concept))

    # Button to start learning
    if st.sidebar.button('Start Training'):
        send_info(selected_topic, selected_subtopic, selected_concept, blooms_level, learning_outcome)
    
    # Streamlit text input element
    user_input = st.chat_input("Type your response here")

    # Appending models reply to state
    if user_input:
        st.session_state.studentReply.append(user_input)
        chat(user_input)

    # Writing messages
    if st.session_state["botReply"]:
        for i in range(len(st.session_state["botReply"])):
            message(st.session_state["botReply"][i], key=str(i))
            if st.session_state["studentReply"] and i < len(st.session_state["studentReply"]) and st.session_state["studentReply"][i] != "":
                message(st.session_state["studentReply"][i], is_user=True, key=str(i) + "_user")


if __name__ == "__main__":
    main()