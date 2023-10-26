from app import app, process_query, get_score
import pytest
    user_answers = [
        "Japan",
        "Rome",
        "Spanish",
        "Smith",
        "scurvy",
        "Apollo",
        "Al Capone",
        "1945",
        "x",
        "Eminem",
        "10080",
        "Volkswagen",
        "x",
        "12",
        "x"
    ]


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == ("Dinosaurs ruled the Earth "
                                          "200 million years ago")


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_quiz_route_get(client):
    response = client.get('/')
    assert response.status_code == 200


def test_quiz_route_post(client):
    response = client.post('/')
    assert response.status_code == 302


def test_submit_route_post_with_sample_answers(client):
    response = client.post('/submit', data={
        'q1': 'Japan',
        'q2': 'Rome',
        'q3': 'Spanish',
        'q4': 'Smith',
        'q5': 'Scurvy',
        'q6': 'Apollo',
        'q7': 'Al Capone',
        'q8': '1945',
        'q9': 'Walt Disney',
        'q10': 'Drake',
        'q11': '10080',
        'q12': 'Volkswagen',
        'q13': 'Amazon',
        'q14': '12',
        'q15': 'Astrophysics'
    })
    assert response.status_code == 200


def test_submit_route_get_with_sample_answers(client):
    response = client.get('/submit', data={
        'q1': 'Japan',
        'q2': 'Rome',
        'q3': 'Spanish',
        'q4': 'Smith',
        'q5': 'Scurvy',
        'q6': 'Apollo',
        'q7': 'Al Capone',
        'q8': '1945',
        'q9': 'Walt Disney',
        'q10': 'Drake',
        'q11': '10080',
        'q12': 'Volkswagen',
        'q13': 'Amazon',
        'q14': '12',
        'q15': 'Astrophysics'
    })

    assert response.status_code == 200



def score_calculated_correctly():
    assert get_score(user_answers) == 11
