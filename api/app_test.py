from app import process_query, get_score

def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == ("Dinosaurs ruled the Earth "
                                          "200 million years ago")


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

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
    
