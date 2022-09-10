from app import index


def test_index():
    assert index() == "Welcome to my webiste"

def test_about():
    assert about() == "My name is A.J"


