from src.app import home


def test_homepage():
    # app = Flask(__name__)
    assert home() == "Home Page"