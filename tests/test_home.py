from src.app import home


def test_homepage(client):
    # app = Flask(__name__)
    res = cilent.get('/')
    assert res.status_code == 200 
