from bs4 import BeautifulSoup
import requests


def fetch_html_from_url(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching HTML from URL: {e}")

    return response.text


def extract_body_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('body')

    if body is None:
        return ""

    return body.get_text()
