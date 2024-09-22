import requests
from bs4 import BeautifulSoup

def scrape_cnn_articles(limit=10):  # Added a 'limit' parameter to control how many articles to scrape
    # Step 1: Send an HTTP request to CNN's homepage
    search_url = 'https://www.cnn.com/'
    response = requests.get(search_url)

    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 4: Find the article titles and their corresponding URLs from the search results
        # Look for the 'a' tag containAing the articles
        articles = soup.find_all('a', class_='container__link')

        if not articles:
            print("No articles found with the specified class.")
            return

        # Step 5: Extract titles and URLs, limit the results dynamically
        for article in articles[:limit]:  # Use 'limit' to control how many articles to fetch
            # Get the title text inside the <span> tag
            title_tag = article.find('span', class_='container__headline-text')
            if title_tag:
                title = title_tag.get_text(strip=True)  # Get title text and remove extra whitespace

                # Get the article URL from the <a> tag
                link = article['href']  # Extract the href attribute from the <a> tag
                if not link.startswith('http'):  # Handle relative URLs
                    link = 'https://www.cnn.com' + link
                
                print(f'Title: {title}\nURL: {link}\n')

    else:
        print(f'Failed to retrieve page. Status code: {response.status_code}')

# Run the scraper function and pass in a dynamic limit, for example, 5 articles
scrape_cnn_articles(limit=5)  # You can change the limit dynamically
