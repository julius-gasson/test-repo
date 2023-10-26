from app import app, process_query, get_score
import pytest


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


def test_submit_route_get(client):
    response = client.get('/submit')
    assert response.status_code == 200


def test_submit_route_post(client):
    response = client.post('/submit')
    assert response.status_code == 200


def score_calculated_correctly():
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
    assert get_score(user_answers) == 11
