#pytest-mock -установить
import pytest
import requests
from unittest.mock import patch
from main import get_random_cat_image


def test_get_random_cat_image_success():
    mock_response = [{"url": "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"}]

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = get_random_cat_image()
        assert url == "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"


def test_get_random_cat_image_failure():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        url = get_random_cat_image()
        assert url is None
