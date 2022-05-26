# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Scrape the url "redplantscience.com"
    url = 'https://redplanetscience.com/'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    html = browser.html
    soup = bs(html, "html.parser")  
  
    news_title = soup.find(class_= 'content_title').text.strip()
    news_p = soup.find(class_='article_teaser_body').text.strip()

    #spaceimages-mars.com
    url_2 = 'https://spaceimages-mars.com/'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(url_2)
    html = browser.html
    soup = bs(html, 'html.parser')

    image_url_1 = soup.find('img', class_='headerimage fade-in')
    image_url = image_url_1.get('src')

    featured_image_url = 'https://spaceimages-mars.com/' + image_url
    
    #Mars Facts 
    url_3 = 'https://galaxyfacts-mars.com/'

    table = pd.read_html(url_3)
    df=table[0]
    df.rename(columns={0: "Description", 1: "Mars_info", 2: "Earth_info"}, inplace=True)
    df.set_index('Description', inplace=True)
    
    html_table = df.to_html()

    text_file = open('df.html', 'w')
    text_file.write(html)
    text_file.close()

    # Mars Hemispheres
    url_4 = 'https://marshemispheres.com/'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_4)
    html = browser.html
    soup = bs(html, "html.parser")  

    hemisphere_image_urls = []

    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemisphere = {}
    
        links[i].click()
    
        sample_img = browser.links.find_by_text('Sample').first
    
        hemisphere['img_url'] = sample_img['href']
    
        hemisphere['title'] = browser.find_by_css('h2.title').text
    
        hemisphere_image_urls.append(hemisphere)
    
        browser.back()

    mars_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'html_table': html,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    return mars_data