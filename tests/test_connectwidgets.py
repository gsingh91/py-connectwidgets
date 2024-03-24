import pytest
from py_connectwidgets import connectwidgets
from dotenv import load_dotenv
import os

load_dotenv()


# Create a fixture for Connect client
@pytest.fixture
def Connect_client():
    return connectwidgets.connect(
        os.getenv("CONNECT_SERVER"), os.getenv("CONNECT_API_KEY")
    )


# test if the provided values for CONNECT_SERVER and CONNECT_API_KEY work
def test_connect(Connect_client):
    assert Connect_client != None


# test if the retrieved content is not empty
def test_get_content(Connect_client):
    df = Connect_client.get_content()
    assert not df.empty
