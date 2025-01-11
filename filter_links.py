import requests
from bs4 import BeautifulSoup

# Replace url of the webpage you wanted to scrape
url = "https://www.w3schools.com/python/python_try_except.asp"
try:
    response = requests.get(url)
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find_all('a', href=True) 
        https_links = [link['href'] for link in links if 'https://' in link['href']]
        
        # Print the filtered links
        if https_links:
            print("Filtered links:")
            for link in https_links:
                print(link)
        else:
            print("No HTTPS links found")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
