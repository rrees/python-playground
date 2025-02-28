import os
import sys

from pathlib import Path

from content.convert_page import convert_content
from feeds.rss import load_feed
from urls import hostname, is_valid_url

DEFAULT_URLS = [
    "https://www.goonhammer.com/",
    "https://billmitchell.org/blog/",
]

urls_to_read = []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        urls_to_read.extend(DEFAULT_URLS)
    else:
        url = sys.argv[1]

        if not is_valid_url(url):
            print("URL provided is not valid", url)
            exit(1)

        urls_to_read.append(url)

    output_directory_name = "output"

    os.makedirs("output", exist_ok=True)

    for url in urls_to_read:
        site_name = hostname(url)
        os.makedirs(os.path.join(output_directory_name, site_name), exist_ok=True)

        print(f"Checking {site_name}")

        feed_results = load_feed(url)

        if feed_results is None:
            print("No feed found")
            continue

        for item in feed_results:
            # print(item)
            conversion_result = convert_content(item["url"])

            if not conversion_result:
                continue

            filename, content = conversion_result

            output_path = Path(os.path.join(output_directory_name, site_name, filename))

            if not output_path.exists():
                with open(output_path, "w") as output_file:
                    output_file.write(content)
