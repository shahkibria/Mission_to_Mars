#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[4]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


# Visit the Quotes to Scrape site
url = 'http://manutd.com/'
browser.visit(url)


# In[6]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[7]:


# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[12]:


slide_elem.find('div', class_ = 'content_title')


# In[10]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[15]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[18]:


# This is an alternative code which is not shown in the module
# This is much simpler code similar to the Practice notebook
# This was done to see if we get the same result. As we can see the result is the same
html = browser.html
news_soup = soup(html, 'html.parser')
title = news_soup.find('div', class_='content_title').get_text()
summary = news_soup.find('div', class_='article_teaser_body').get_text()
print(title)
print ('------------')
print (summary)


# ### Featured Images 

# In[19]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[21]:


# Find and click the full image button
# Since there are only three results in "button" when we search in Dev Tools
# We are asking to find the second instance which has an index of 1
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[23]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[25]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[27]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Data

# In[28]:


# Visit URL
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[32]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[34]:


df_2 = pd.read_html('https://galaxyfacts-mars.com')[1]
df_2.columns=['description', 'Mars']
df_2.set_index('description', inplace=True)
df_2


# In[35]:


df.to_html()


# In[36]:


browser.quit()


# In[ ]:




