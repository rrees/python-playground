import httpx
from bs4 import BeautifulSoup
import re


def is_rss_feed(content):
    """
    Check if the content is an RSS feed using regex patterns to look for
    common RSS/Atom elements near the start of the document.
    """
    start_content = content[:1000].lower()

    patterns = [
        r"<\?xml.*?\?>.*?<rss.*?>",
        r'<\?xml.*?\?>.*?<feed.*?xmlns="http://www\.w3\.org/2005/Atom"',
        r'<\?xml.*?\?>.*?<rdf:RDF.*?xmlns="http://purl\.org/rss/1\.0/',
    ]

    return any(
        re.search(pattern, start_content, re.DOTALL | re.IGNORECASE)
        for pattern in patterns
    )


def find_feed_link(html_content):
    """
    Search HTML content for RSS/Atom feed links.
    Returns the first feed URL found or None.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    feed_links = soup.find_all("link", type=re.compile(r"application/(rss|atom)\+xml"))
    if feed_links:
        return feed_links[0].get("href")

    possible_feed_links = soup.find_all("a", href=re.compile(r"/(feed|rss|atom)(/|$)"))
    if possible_feed_links:
        return possible_feed_links[0].get("href")

    return None


def extract_tag_content(content, tag):
    """Helper function to extract content from XML tags."""
    match = re.search(f"<{tag}[^>]*?>(.*?)</{tag}>", content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_feed_items(content, feed_url):
    items = []

    # Handle both RSS items and Atom entries
    item_patterns = [r"<item[^>]*?>.*?</item>", r"<entry[^>]*?>.*?</entry>"]

    # Find all items in the feed
    all_items = []
    for pattern in item_patterns:
        all_items.extend(re.findall(pattern, content, re.DOTALL | re.IGNORECASE))

    for item_content in all_items:
        item_data = {"title": None, "url": None}

        # Extract title
        title = extract_tag_content(item_content, "title")
        if title:
            item_data["title"] = title

        # Extract URL - try different patterns
        # First try Atom link with href
        url_match = re.search(r'<link[^>]*?href=[\'"]([^\'"]+)[\'"]', item_content)
        if not url_match:
            # Try RSS link
            url_match = re.search(r"<link[^>]*?>([^<]+)</link>", item_content)

        if url_match:
            url = url_match.group(1).strip()
            item_data["url"] = url

        if item_data["url"]:  # Only add items that have a URL
            items.append(item_data)

    return items


def load_feed(url):
    if not url:
        raise ValueError("URL not provided")

    headers = {"User-Agent": "RSS Feed Detector/1.0"}

    try:
        with httpx.Client(follow_redirects=True) as client:
            # Make initial request
            response = client.get(url, headers=headers)
            response.raise_for_status()
            content = response.text

            # Check if it's already a feed
            if is_rss_feed(content):
                items = extract_feed_items(content, url)
                return items

            # If not a feed, look for feed link
            feed_url = find_feed_link(content)
            if not feed_url:
                return None

            # Load the feed
            feed_response = client.get(feed_url, headers=headers)
            feed_response.raise_for_status()
            feed_content = feed_response.text

            if not is_rss_feed(feed_content):
                return None

            items = extract_feed_items(feed_content, feed_url)
            return items

    except httpx.RequestError as e:
        raise ConnectionError(f"Failed to fetch URL: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise ConnectionError(f"HTTP error occurred: {str(e)}")
