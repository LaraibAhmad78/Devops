import requests
from bs4 import BeautifulSoup

def scrape_webpage(https://en.wikipedia.org/wiki/Python_(programming_language):
    # Send an HTTP request to the URL
    response = requests.get(https://en.wikipedia.org/wiki/Python_(programming_language)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the parsed content
        clean_text = soup.get_text()

        return clean_text

    else:
        print(f"Error: Unable to fetch content from {https://en.wikipedia.org/wiki/Python_(programming_language}. Status code: {response.status_code}")
        return None

# Example usage:
url_to_scrape = 'https://en.wikipedia.org/wiki/Python_(programming_language'
clean_text = scrape_webpage(url_to_scrape)

if clean_text:
    print(clean_text)

