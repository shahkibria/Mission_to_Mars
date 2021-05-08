# Mission_to_Mars

## Overview

Use BeautifulSoup, Splinter, and Pandas to scrape four different webpages related to Mars, and display the results on a webpage using MongoDB and Flask.

## Process

### Scrape Mars Data
We performed the scraping initially on Jupyter Notebook. Scraping was first done on the [Nasa Mars News](https://redplanetscience.com/) website where we scraped the latest news and text related to Mars. The second page that we scraped was the [JPL Space Image](https://spaceimages-mars.com) website. We extracted the full-size featured image from this site. The third site to be scraped was the [Space Facts](https://galaxyfacts-mars.com) website which was used to gather data regarding Earth and Mars. Finally we extracted the four Mars hemisphere full-size images from [USGS Astrogeology](https://marshemispheres.com/) website. 

After all the data was checked, we transfered the code to a Python file and created a scraping function. The [Jupyter](https://github.com/shahkibria/Mission_to_Mars/blob/main/Mission_to_Mars_Challenge.ipynb) notebook file and the [Scraping](https://github.com/shahkibria/Mission_to_Mars/blob/main/Scraping.py) python file has been included in the repository. 

### Using MongoDB to store the data
Once the data was scraped, we used MongoDB to store the data. Using the scraping function, the data extracted was compiled in a dictionary and stored in a MongoDB collection titled "mars". 

### Using Flask to present our scraped data
An instance of Flask was created and a connection to the database was established. Using the connection, the scraped data is presented on the Flask website. The website UI was updated using Bootstrap. The [python code](https://github.com/shahkibria/Mission_to_Mars/blob/main/app.py) to run the flask website and [HTML](https://github.com/shahkibria/Mission_to_Mars/blob/main/templates/index.html) for the flask website has been included in the repository. 

### Related Screenshots
 
 Deliverable 1: Full Resolution Image and Title Dictionary
![](https://github.com/shahkibria/Mission_to_Mars/blob/main/Screenshots/Mars%20-%20Hemisphere%20-%20dictionary.png)

Deliverable 2: Mars Hemisphere full-resolution images
![](https://github.com/shahkibria/Mission_to_Mars/blob/main/Screenshots/Mars%20-%20Hemisphere%20-%20Screenshot.png)

Deliverable 3: Mobile-friendly version
![](https://github.com/shahkibria/Mission_to_Mars/blob/main/Screenshots/Web-page%20Mobile%20Responsive.png)

Deliverable 3: Bootstrap Mod 1: paragraph is made to stand out by adding .lead
![](https://github.com/shahkibria/Mission_to_Mars/blob/main/Screenshots/Bootstrap%20Mod%201%20-%20Lead%20Body.png)

Deliverable 3: Bootstrap Mod 2: Table is updated
![](https://github.com/shahkibria/Mission_to_Mars/blob/main/Screenshots/Bootstrap%20Mod%202%20-%20table%20striped.png)



