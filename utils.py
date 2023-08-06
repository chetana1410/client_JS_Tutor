import streamlit as st
import pandas as pd
import requests

lo = pd.read_excel('AI assignment metadata for Javascript.xlsx', sheet_name=1)
BASE_URL = 'https://js-tutor-server.onrender.com'
javascript = {
    "Basic Concepts": [
        "Data Types and Variables",
        "Operators",
        "Conditionals",
        "Loops",
        "Functions",
        "Strings",
        "Objects and Classes",
        "Arrays",
    ],
    "DOM": [
        "Selecting Elements",
        "Modifying Elements",
        "Creating and Deleting Elements",
        "Events",
    ],
    "Advanced Concepts": [
        "Asynchronous Javascript",
        "Callbacks",
        "Promises",
        "Fetch API",
        "Async Await",
        "Error Handling",
    ],
}


def get_subtopics():
    return list(javascript.keys())

def get_concepts(selected_subtopic):
    return javascript[selected_subtopic]

def get_learning_outcome(blooms_level,selected_concept):
    return lo[(lo['blooms_level']==blooms_level)&(lo['concept']==selected_concept)]['learning_outcome'].tolist()

def get_blooms_level():
    return ['Remembering', 'Applying', 'Creating']

def handle_response(url, payload):
    response = requests.post(url, json=payload)
    # Check the response status code to see if the request was successful
    if response.status_code == 200:
        print("POST request successful!")
        st.session_state.botReply.append(response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print("Response data:")
        print(response.text) 
        st.session_state.botReply.append("Server Error")

def send_info(selected_topic, selected_subtopic, selected_concept, blooms_level, learning_outcome):
    if selected_topic and selected_subtopic and selected_concept and blooms_level and learning_outcome:
        url = BASE_URL+'/info'
        payload = {
            'selectedTopic': selected_topic,
            'selectedSubtopic': selected_subtopic,
            'selectedConcept': selected_concept,
            'bloomsLevel':blooms_level,
            'learningOutcome':learning_outcome
            }
        handle_response(url, payload)

def chat(message):
    if message and message != "":
        url = BASE_URL+"/chat"
        payload = {
            'message': message
        }
        handle_response(url, payload)

def declare_state():
    if "botReply" not in st.session_state:
        st.session_state["botReply"] = []

    if "studentReply" not in st.session_state:
        st.session_state["studentReply"] = []