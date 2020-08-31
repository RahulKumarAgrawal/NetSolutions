from bs4 import BeautifulSoup
import requests
import time
from random import randint
import pandas as pd
import json
response = requests.get("https://www.udacity.com/courses/school-of-ai")
html_soup = BeautifulSoup(response.content, 'html.parser')

#find all the URLs (items in the html where href exists)
url = html_soup.find_all(href=True)
print(url)
# #Iterate through the urls, and only return the ones that contain course and --
links = []
for u in url:
    if (u['href'].find('courses') != -1):
        if (u['href'].find('--') != -1):
            links.append(u['href'])
            
#remove duplicates by converting the list of links to a set, then back to a list
links = list(set(links)) 
print(links)
print(len(links))

#initilise the lists to store the extracted info
course_name = []
course_urls = []
course_school = []
skill_covered = []
difficulty = []
course_costs = []

# Preparing the monitoring of the loop
start_time = time.time()
requests_count = 0

#iterate through each link to extract info about the nano degree it belongs to and the cost
for i in range(len(links)):
    #need to make requests at random times in order to not be blocked by website
    time.sleep(randint(2,6)) 
    url = "https://www.udacity.com" + links[i]
    response = requests.get(url)
    content = response.content
    html_soup = BeautifulSoup(content, 'html.parser')
    
    # Monitor the requests
    requests_count += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests_count, requests_count/elapsed_time))
    #clear_output(wait = True)
    
    # Break the loop if the number of requests is greater than expected
    if requests_count > 250:
        warn('Number of requests was greater than expected.')  
        break 
    
    try:
        course_school = html_soup.find('h3',class_="card__title__school greyed").text
    except:
        course_school = 'None'
    try:
        course_name = html_soup.find('h2',class_='card__title__nd-name').text
    except:
        course_name = 'None'
    try:
        cost = html_soup.find('span',class_='price__payable').text
    except:
        cost = 'None'
    try:
        skill_covered = html_soup.find('p',class_='text-content__text').text
    except:
        skill_covered = 'None'
    try:
        difficulty = html_soup.find('small',class_='difficulty small').text
    except:
        difficulty = 'None'
    course_name.join(course_name,)
    course_urls.append(url,)
    course_school.join(course_school,)
    skill_covered.join(skill_covered,)
    difficulty.join(difficulty,)
    course_costs.append(cost)


courses_df = pd.DataFrame({'Name': course_name,
                          'URL': course_urls,
                          'course_school': course_school,
                          'skill_covered': skill_covered,
                          'difficulty' : difficulty,
                          'Cost':course_costs})
courses_df = courses_df.sort_values('course_school')
print(courses_df.info())
print(courses_df)
json = courses_df.to_json() 
print(json) 