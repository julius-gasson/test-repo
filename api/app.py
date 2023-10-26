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
    "What was the name of the crime boss who ran the feared Chicago Outfit?",
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
    "Japan",
    "Rome",
    "Spanish",
    "Smith",
    "Scurvy",
    "Apollo",
    "Al Capone",
    "1945",
    "Walt Disney",
    "Drake",
    "10080",
    "Volkswagen",
    "Amazon",
    "12",
    "Astrophysics",
]

user_answers = []  # Moved this list outside of the route function


@app.route("/", methods=["GET", "POST"])
def quiz():
    global user_answers  # Use the global user_answers list
    if request.method == "POST":
        return redirect(url_for("submit"))
    return render_template("quiz.html", questions=questions)


def get_score(user_answers, answers):
    if len(user_answers) == 15:
        return sum(1 for user, correct in zip(user_answers, answers)
                   if user.lower() == correct.lower())
    else:
        return len(user_answers)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    for i in range(15):
        user_answer = request.form.get(f"q{i + 1}")
        user_answers.append(user_answer)
    score = get_score(user_answers, answers)
    user_answers = []
    return render_template("submit.html", score=score)


def process_query(input):
    if input == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if input == "asteroids":
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get('q')
    return process_query(query_param)
