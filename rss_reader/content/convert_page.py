import httpx

from bs4 import BeautifulSoup
from markdownify import markdownify


def convert_content(url):
    response = httpx.get(url)

    if response.status_code != 200:
        print(f"Received status code {response.status_code} for url: {url}")
        return None

    page = response.raise_for_status().text

    parsed_content = BeautifulSoup(page, "html.parser")

    title = parsed_content.find("h1")

    filename = f"{title.string.strip().replace(' ', '_')}.md"

    page_content = parsed_content.find("article")

    if not page_content:
        page_content = parsed_content.find("body")

    # Clean content

    for tag_name in ("img", "svg", "script", "style"):
        for tag in parsed_content.find_all(tag_name):
            tag.decompose()

    page_content.smooth()

    content = markdownify(str(page_content))

    return filename, content
