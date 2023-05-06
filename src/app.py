from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Configuración de OpenAI
openai.api_key ="YOUR_OPENAI_API_KEY"

model_engine = "text-davinci-003"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    prompt = request.form['prompt']
    response = generate_response(prompt)
    return response

def generate_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

if __name__ == '__main__':
    app.run()