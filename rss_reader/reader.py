import os
import sys

from content.convert_page import convert_content
from feeds.rss import load_feed
from urls import is_valid_url


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reader.py <url to read>")
        exit(1)

    url = sys.argv[1]

    if not is_valid_url(url):
        print("URL provided is not valid", url)
        exit(1)

    output_directory_name = "output"

    os.makedirs("output", exist_ok=True)

    feed_results = load_feed(url)

    for item in feed_results:
        # print(item)
        filename, content = convert_content(item["url"])

        output_path = os.path.join(output_directory_name, filename)

        with open(output_path, "w") as output_file:
            output_file.write(content)
