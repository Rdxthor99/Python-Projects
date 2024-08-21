import requests
from bs4 import BeautifulSoup

def google_search(query):
    try:
        # Create a Google search query URL
        url = f"https://www.google.com/search?q={query}&num=5"
        
        # Set the user-agent to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Make a request to Google
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            print("Failed to retrieve results. Status code:", response.status_code)
            return
        
        # Parse the response HTML content
        soup = BeautifulSoup(response.text, "lxml")
        
        # Find search result containers
        results = soup.find_all('div', class_='tF2Cxc', limit=5)
        
        # Print the top 5 results
        for i, result in enumerate(results):
            title = result.find('h3').text if result.find('h3') else "No Title"
            link = result.find('a')['href'] if result.find('a') else "No Link"
            print(f"{i+1}. {title}")
            print(f"Link: {link}\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
query = input("Enter the search query: ")
google_search(query)
