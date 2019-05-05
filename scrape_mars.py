## Scraping

from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import pprint


def scrape():
    ### NASA Mars News

    browser = Browser("chrome")
    news_url = "https://mars.nasa.gov/news"

    browser.visit(news_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "html.parser")

    # Collect the latest News Title and Paragraph Text.
    news_title = soup.find('div', class_ = 'content_title').find('a').text
    print(news_title)
    print("\n")

    news_p = soup.find('div', class_ = 'article_teaser_body').text
    print(news_p)

    browser.quit()



    ### JPL Mars Space Images - Featured Image

    browser = Browser("chrome")
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(img_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "html.parser")

    #  Find the image url for the current Featured Mars Image
    img_str = soup.find('div', class_="carousel_items").find('article')['style']
    print(img_str)

    featured_image_url = img_url[0:36] + img_str[35:-3]

    print(featured_image_url)

    browser.quit()



    ### Mars Weather

    browser = Browser("chrome")

    tweet_url = "https://twitter.com/marswxreport?lang=en"

    browser.visit(tweet_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    # Scrape the latest Mars weather tweet from the page.

    tweet_qry = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").children

    for i in tweet_qry:
        mars_weather = i
        break

    print(mars_weather)

    browser.quit()



    # ### Mars Facts

    browser = Browser("chrome")
    facts_url = "https://space-facts.com/mars/"

    browser.visit(facts_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    facts_table = soup.find('tbody')
    print(facts_table)

    column1_lst = []
    column2_lst = []

    for i in facts_table.find_all('td', class_ = "column-1"):
        column1_lst.append(i.text[0:-1]) # using 0:-1 to omit the ":" that's at the end of each row element
        
    for i in facts_table.find_all('td', class_ = "column-2"):
        column2_lst.append(i.text)

    facts_df = pd.DataFrame(
    {'Metric': column1_lst,
     'Data': column2_lst
    })

    facts_df

    mars_facts = facts_df.to_dict(orient="records")
    
    browser.quit()



    ### Mars Hemispheres

    usgs_url = "https://astrogeology.usgs.gov"

    #### Hemisphere1: Cerberus Hemisphere Enhanced

    browser = Browser("chrome")
    cerebrus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"

    browser.visit(cerebrus_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    cerebrus_title = soup.find('h2', class_ = "title").text
    cerebrus_title = cerebrus_title.rsplit(' ',1)[0]
    print(cerebrus_title)

    cerebrus_src = soup.find('img', class_ = "wide-image")['src']
    cerebrus_img_url = usgs_url + cerebrus_src
    print(cerebrus_img_url)

    browser.quit()

    #### Hemisphere2: Schiaparelli Hemisphere Enhanced

    browser = Browser("chrome")
    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"

    browser.visit(schiaparelli_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    schiaparelli_title = soup.find('h2', class_ = "title").text
    schiaparelli_title = schiaparelli_title.rsplit(' ',1)[0]
    print(schiaparelli_title)

    schiaparelli_src = soup.find('img', class_ = "wide-image")['src']
    schiaparelli_img_url = usgs_url + schiaparelli_src
    print(schiaparelli_img_url)

    browser.quit()

    #### Hemisphere3: Syrtis Major Hemisphere Enhanced

    browser = Browser("chrome")
    syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"

    browser.visit(syrtis_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    syrtis_title = soup.find('h2', class_ = "title").text
    syrtis_title = syrtis_title.rsplit(' ',1)[0]
    print(syrtis_title)
    
    syrtis_src = soup.find('img', class_ = "wide-image")['src']
    syrtis_img_url = usgs_url + syrtis_src
    print(syrtis_img_url)

    browser.quit()

    #### Hemisphere4: Valles Marineris Hemisphere Enhanced

    browser = Browser("chrome")
    valles_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

    browser.visit(valles_url)

    time.sleep(2)

    html = browser.html 
    soup = bs(html, "lxml")

    valles_title = soup.find('h2', class_ = "title").text
    valles_title = valles_title.rsplit(' ',1)[0]
    print(valles_title)

    browser.quit()

    valles_src = soup.find('img', class_ = "wide-image")['src']
    valles_img_url = usgs_url + valles_src
    print(valles_img_url)

    hemisphere_image_urls = {}

    hemisphere_image_urls = [
    {"title": cerebrus_title, "img_url": cerebrus_img_url},
    {"title": schiaparelli_title, "img_url": schiaparelli_img_url},
    {"title": syrtis_title, "img_url": syrtis_img_url},
    {"title": valles_title, "img_url": valles_img_url},
    ]

    pprint.pprint(hemisphere_image_urls)

    ### Summary Dictionary

    summary_dict ={}

    summary_dict = {
        "News_Title": news_title,
        "News_Teaser": news_p,
        "Featured_Image": featured_image_url,
        "Mars_Weather": mars_weather,
        "Mars_Facts": mars_facts,
        "Mars_Hemispheres": hemisphere_image_urls
        }

    return summary_dict