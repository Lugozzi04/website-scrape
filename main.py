import requests
from bs4 import BeautifulSoup

# Function to scrape data from a website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example 1: Extracting article titles from a blog
    article_titles = soup.find_all('h2', class_='article-title')
    print("Article titles:")
    for title in article_titles:
        print(title.text)

    # Example 2: Extracting image links from a gallery
    image_links = soup.find_all('img', class_='gallery-image')
    print("\nImage links:")
    for image in image_links:
        print(image['src'])

    # Example 3: Extracting information from a table
    table = soup.find('table', id='data-table')
    if table:
        rows = table.find_all('tr')
        print("\nTable content:")
        for row in rows:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            print(row_data)

    # Example 4: Extracting internal links from a page
    internal_links = soup.find_all('a', href=True)
    print("\nInternal links:")
    for link in internal_links:
        if link['href'].startswith('/'):
            print(url + link['href'])

    # Example 5: Extracting external links from a page
    external_links = soup.find_all('a', href=True)
    print("\nExternal links:")
    for link in external_links:
        if link['href'].startswith('http'):
            print(link['href'])

    # Example 6: Extracting paragraph texts
    paragraphs = soup.find_all('p')
    print("\nParagraphs:")
    for paragraph in paragraphs:
        print(paragraph.text)

    # Example 7: Extracting data from forms
    forms = soup.find_all('form')
    print("\nForms:")
    for form in forms:
        form_data = {}
        form_inputs = form.find_all(['input', 'textarea'])
        for input_field in form_inputs:
            field_name = input_field.get('name')
            field_value = input_field.get('value', '')
            form_data[field_name] = field_value
        print("Form data:")
        print(form_data)

    # Example 8: Extracting data from a list
    list_items = soup.find_all('li')
    print("\nList items:")
    for item in list_items:
        print(item.text)

# URL of the website to scrape data from
website_url = 'https://www.meteo.it/'

# Call the scraping function
scrape_website(website_url)
