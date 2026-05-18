from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from chains.career_chain import generate_career_guidance

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():

    data = request.json

    skills = data.get('skills')
    interests = data.get('interests')
    experience = data.get('experience')
    goals = data.get('goals')

    response = generate_career_guidance(
        skills,
        interests,
        experience,
        goals
    )

    return jsonify({
        'response': response
    })


if __name__ == '__main__':
    app.run(debug=True)