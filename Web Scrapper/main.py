import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data from the webpage and store it in variables
    title = soup.find('h1').text.strip()
    description = soup.find('p').text.strip()

    # Return the extracted data as a dictionary
    return {'Title': title, 'Description': description}

def save_to_csv(data, filename):
    fieldnames = data[0].keys()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    # Specify the URLs of the websites you want to scrape
    urls = ['https://www.example1.com', 'https://www.example2.com']

    scraped_data = []

    # Scrape each website and append the extracted data to the list
    for url in urls:
        scraped_data.append(scrape_website(url))

    # Save the extracted data to a CSV file
    save_to_csv(scraped_data, 'scraped_data.csv')

if __name__ == '__main__':
    main()
