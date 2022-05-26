# Web-scraping-challenge
Part 1: Scraping
Complete an initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

1). Create a Jupyter Notebook file called mission_to_mars.ipynb. Use this file to complete all scraping and analysis tasks. 

NASA Mars News
Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that I can reference later.

JPL Mars Space Images—Featured Image
Visit the URL for the Featured Space Image site here.

2). Use Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called featured_image_url.

Be sure to find the image URL to the full-sized .jpg image.

Be sure to save a complete URL string for this image.

3). Mars Facts
Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

Use Pandas to convert the data to a HTML table string.

4). Mars Hemispheres
Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.

You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.

Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


Part 2: MongoDB and Flask Application
1). Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

2). Start by converting your Jupyter notebook into a Python script called scrape_mars.py by using a function called scrape. This function should execute all your scraping code from above and return one Python dictionary containing all the scraped data.

Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

Store the return value in Mongo as a Python dictionary.
3). Create a root route / that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

Create a template HTML file called index.html that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


Part 3: Submission
To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1). The Jupyter notebook containing the scraping code used

2). Screenshots of your final application

3). Ensure your repository has regular commits and a detailed README.md file. Then, submit the link to your new repository.

![Screen Shot 2022-05-26 at 6 30 57 PM](https://user-images.githubusercontent.com/100645924/170599778-9d4747d5-1e58-4e3b-8458-90c7fa659882.png)

![Screen Shot 2022-05-26 at 6 29 42 PM](https://user-images.githubusercontent.com/100645924/170599956-62a4071b-1cec-4e2b-bf67-e07d29c3913f.png)

![Screen Shot 2022-05-26 at 6 31 17 PM](https://user-images.githubusercontent.com/100645924/170600161-c496bc0d-bc9c-415b-b36f-a73328b175ed.png)


