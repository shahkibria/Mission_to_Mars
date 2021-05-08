# Mission_to_Mars

## Overview

Use BeautifulSoup, Splinter, and Pandas to scrape four different webpages related to Mars, and display the results on a webpage using MongoDB and Flask.

## Process

### Scrape Mars Data
We performed the scraping initially on Jupyter Notebook. Scraping was first done on the [Nasa Mars News](https://redplanetscience.com/) website where we scraped the latest news and text related to Mars. The second page that we scraped was the [JPL Space Image](https://spaceimages-mars.com) website. We extracted the full-size featured image from this site. The third site to be scraped was the [Space Facts](https://galaxyfacts-mars.com) website which was used to gather data regarding Earth and Mars. Finally we extracted the four Mars hemisphere full-size images from [USGS Astrogeology](https://marshemispheres.com/) website. 

After all the data was checked, we transfered the code to a Python file and created a scraping function. 

### Using MongoDB to store the data
Once the data was scraped, we used MongoDB to store the data. Using the scraping function, the data extracted was compiled in a dictionary and stored in a MongoDB collection titled "mars". 

### Using Flask to present our scraped data
An instance of Flask was created and a connection to the database was established. Using the connection, the scraped data is presented on the Flask website. The website UI was updated using Bootstrap. 

