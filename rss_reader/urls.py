from urllib.parse import urlparse


def is_valid_url(url):
    """Check if the provided URL is valid."""
    result = urlparse(url)
    return all([result.scheme, result.netloc, result.hostname, result.path])
