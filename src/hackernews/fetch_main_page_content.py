from bs4 import BeautifulSoup
from web_utils import fetch_html_from_url
from hackernews import web_url


def get_new_posts():
    html = fetch_html_from_url(web_url)
    soup = BeautifulSoup(html, "html5lib")

    # All posts are between <a></a> tag
    links_and_posts = soup.find_all("a")

    # The first eleven links are related to the website
    # such as taskbar, header, etc.
    # Therefore we skip these links
    posts = links_and_posts[11:]

    posts_dict = dict()
    for post in posts:
        post_url = post["href"]
        post_title = post.string
        posts_dict[post_title] = post_url

    return posts_dict
