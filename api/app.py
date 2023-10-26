from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

def get_score(answers):
    assert len(answers) == 15
    score = 0
    if answers[0] == "hong kong": score += 1
    if answers[1] == "rome": score += 1
    if answers[2] == "spanish": score += 1
    if answers[3] == "smith": score += 1
    if answers[4] == "scurvy": score += 1
    if answers[5] == "apollo": score += 1
    if answers[6] == "al capone": score += 1
    if answers[7] == "1945": score += 1
    if answers[8] in ["walt disney", "disney"]: score += 1
    if answers[9] == "drake": score += 1
    if answers[10] in ["10,080", "10 080", "10080"]: score += 1
    if answers[11] == "volkswagen": score += 1
    if answers[12] == "amazon": score += 1
    if answers[13] == "12": score += 1
    if answers[14] == "astrophysics": score += 1
    return score

@app.route("/submit", methods=["POST"])
def submit():
    
    for i in range(1, 16):
        question_key = f"q{i}"
        answer = request.form.get(question_key)
        answers.append(answer.lower())
    score = get_score(answers)

    for i in range(15):
        globals()[f'q{i+1}'] = answers[i]
    
    return render_template("hello.html", 
    q1 = q1,
    q2 = q2,
    q3 = q3,
    q4 = q4,
    q5 = q5,
    q6 = q6,
    q7 = q7,
    q8 = q8,
    q9 = q9,
    q10 = q10,
    q11 = q11,
    q12 = q12,
    q13 = q13,
    q14 = q14,
    q15 = q15,
    total_score = score
    )


def process_query(input):
    if input == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if input == "asteroids":
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get('q')
    return process_query(query_param)
