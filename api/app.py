from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions and answers
questions = [
    "What country has the highest life expectancy?",
    "Where would you be if you were standing on the Spanish Steps?",
    "Which language has more native speakers: English or Spanish?",
    "What is the most common surname in the United States?",
    "What disease commonly spread on pirate ships?",
    "Who was the Ancient Greek God of the Sun?",
    "What was the name of the crime boss who was head of the feared Chicago Outfit?",
    "What year was the United Nations established?",
    "Who has won the most total Academy Awards?",
    "What artist has the most streams on Spotify?",
    "How many minutes are in a full week?",
    "What car manufacturer had the highest revenue in 2020?",
    "What company was originally called 'Cadabra'?",
    "How many faces does a Dodecahedron have?",
    "Queen guitarist Brian May is also an expert in what scientific field?",
]

answers = [
    "Hong Kong",
    "Rome",
    "Spanish",
    "Smith",
    "Scurvy",
    "Apollo",
    "Al Capone",
    "1945",
    "Walt Disney",
    "Drake",
    "10,080",
    "Volkswagen",
    "Amazon",
    "12",
    "Astrophysics",
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = []
        for i in range(len(questions)):
            user_answer = request.form.get(f"q{i + 1}")
            user_answers.append(user_answer)
        return redirect(url_for("submit", answers=user_answers, questions=questions))
    return render_template("quiz.html", questions=questions)

def get_score(user_answers, answers):
    sum(1 for user, correct in zip(user_answers, answers) if user.lower() == correct.lower())

@app.route("/submit", methods=["GET", "POST"])
def submit():
    user_answers = request.args.getlist("answers")
    score = get_score(user_answers, answers)
    return render_template("submit.html", user_answers=user_answers, questions=questions, score=score)

def process_query(input):
    if input == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if input == "asteroids":
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get('q')
    return process_query(query_param)

