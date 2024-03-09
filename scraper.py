
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

html = """
<div class="w-full p-3 bg-white border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700"><div class="flex justify-between items-center"><h2 class="mb-2 font-bold tracking-tight text-gray-900 dark:text-white">Apple</h2><div class="text-right"><span class="px-3 py-1 rounded-full text-xs bg-blue-200 text-blue-800">2 d ago</span></div></div><p class="mb-3 font-normal text-gray-700 dark:text-gray-400">AIML - Software Engineer  - MLPT, Bolt</p><button class="bg-black text-white px-3 py-1 rounded-full inline-block text-xs">Apply now</button></div>
"""
# https://modal.com/docs/examples/web-scraper

# https://medium.com/@pankaj_pandey/web-scraping-using-python-for-dynamic-web-pages-and-unveiling-hidden-insights-8dbc7da6dd26

# 

def scrape_jobpulse(url):
    # Send a GET request to the Jobpulse website
    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source

    response = requests.get(url)
    print("after request")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        # Extract job postings based on HTML elements
        job_postings = soup.find_all('div', class_='w-full p-3 bg-white border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700')
        print(f"job_postings: {job_postings}")
        # Print or process the extracted data as needed
        for job in job_postings:
          company_name = soup.find('h2', class_='mb-2 font-bold tracking-tight text-gray-900 dark:text-white').text.strip()
          job_title = soup.find('p', class_='mb-3 font-normal text-gray-700 dark:text-gray-400').text.strip()
          posted_ago = soup.find('span', class_='px-3 py-1 rounded-full text-xs bg-blue-200 text-blue-800').text.strip()


          print(f"Title: {job_title}\nCompany: {company_name}\Posted: {posted_ago}\n{'-' * 20}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
      
    driver.quit()

# Replace 'your_jobpulse_url' with the actual URL of the Jobpulse website
jobpulse_url = 'https://jobpulse.fyi/'
scrape_jobpulse(jobpulse_url)
