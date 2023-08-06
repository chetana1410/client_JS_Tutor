# Personal JavaScript Tutor App - Frontend

Welcome to the Personal JavaScript Tutor App frontend! This application is designed to help you learn JavaScript with the assistance of Langchain, Streamlit, and FastAPI technologies. The frontend is built using Streamlit, a Python library known for its exceptional UI features and state management utilities. The app allows you to interact with a personal JavaScript tutor, where you can send messages and receive responses from the tutor through the backend, which connects to OpenAI endpoints.

## Getting Started

To run the frontend part of the Personal JavaScript Tutor App, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.6 or above)
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine.

2. Navigate to the frontend directory.

3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Running the Frontend

After the installation is complete, you can start the frontend server by executing the following command:

```bash
streamlit run index.py
```

This will launch the Streamlit application, and you can access the frontend in your web browser at `http://localhost:8501`.

### Alternative Access

Alternatively, you can access the frontend directly through the following website:

[https://js-tutor-client.onrender.com/](https://js-tutor-client.onrender.com/)

## Usage

1. Once you access the frontend, you will be prompted to choose a particular topic to learn in JavaScript.

2. After selecting a topic, you can start sending messages to the personal JavaScript tutor. These messages will be sent to the backend server, which will connect to OpenAI endpoints to process the queries.

3. The responses from the backend will be streamed back to the website, where you can view them and continue the learning process.

## Configuration

If you are running both the frontend and backend servers locally, please ensure that you provide the backend URL to the `baseurl` variable in the frontend code. This ensures that the frontend can communicate with the backend effectively.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

## Acknowledgments

We express our gratitude to the Langchain, Streamlit, and FastAPI communities for providing powerful tools to build this app. We also thank OpenAI for granting access to their API, enabling us to create an enhanced learning experience for JavaScript enthusiasts.