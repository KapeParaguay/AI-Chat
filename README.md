# AI-Chat
This is a Flask app that uses OpenAI's GPT-3 language model to generate text responses based on a user's prompt. The app includes a simple HTML form where users can enter a prompt, which is then sent to the server for processing. The server sends the prompt to the OpenAI API, which generates a response based on the provided prompt.

## Setup
To use this app, you will need to have an OpenAI API key. You can get one by signing up on the OpenAI website.

After you have an API key, you can set it as the value of the openai.api_key variable in the code. You can also change the model_engine variable to use a different language model.

## Running the App
To run the app, you can execute the app.py script in your terminal or command prompt. This will start a Flask server that listens on port 5000. You can then navigate to http://localhost:5000 in your web browser to use the app.

## Dependencies
This app depends on the Flask, OpenAI, and os Python packages. You can install these packages using pip by running the following command:

```
pip install flask openai
```
