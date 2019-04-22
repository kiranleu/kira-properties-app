#  Fullstack Frameworks Django Project

## Review your Landlord

Revie your Landlord is a fabricated e-commerce website allows users to review, read and add more infomration about the Landlords or landladies that
they have experience with during renting: a room, house or apartment.

## Overview of features:

- A selection of reviews of different type of properties.
- The ability to add other properties to the list properties already created and leave new reviews related to the property rented.
- A property list section were all reviews posted and information about properties can be read.
- Users can leave leave reviews on new properties added.
- A Subscription section where users can sign for a monthly or year subscription in order to support the Review your Landlord Project.
- This project "Review your Landlord"  was built in Python3 using the Django framework.
- It is a project built only for educational porposes.
A live version is hosted here

## UX

I have been developing this project the past year as I saw the necesity of a web where every tenant could review their landlords and landladies and keep the record of them.

When looking for ideas of similar webs I found similar sites but most of them were focused on reviewing the properties not the landlords or landladies as well as the people who you migh end sharing the facilities with.

My aim for this project was to have an informative web where we could find deep information about the possible properties will be renting as well as their owners.



The visual theme used for the site has been kept simple so users can be focus primarily on the reviews.

To achieve this I had used cards where all the information of the properties is displayed.  Underneath the car will find:

- Form to add a Review
- Previous reviews from other tenants

Site navigation is designed to be as intuitive as possible. The navbar contains links to:

    - Sign up
    - Log in
    - Profile
    - Add Property
    
1. If the user is not logged in it will bring you to Log in option
2. If the user is not signed up then the user could click on Sign up option
3. If the user is logged in and had signed up previously, then; the user will have access to its profile and the Add property option.

This was achieved through  a dropdown menu in mobile device.

I would like to confirm that no Template was used for the creation of this site.

###  Technologies Used

Please find here the list of technologies used within the creation of the project:

* HTML, CSS and Bootstrap
* Python3
* Django2 Framework
* Javascript
* Jquery and SQLite Database
* lightbox and S3 storage
* Stripe: Used for processing payments of subscriptions types.
* Wireframing were made using the Balsamiq application and can be found in the wireframes folder

# Background and features per app
## Accounts App
The accounts app is used for user authentication. 

One of the benefits to creating an account is:
1. Being able to review on properties.
2. User is able to add a new propertie and landlord/landlady.
3. Create a profile
4. Add their own Avatar to their profile.
5. Add and keep in the DB the credit card details.
6. Able to subscribe.



#### Existing Features

- Users can register, log in and log out in the website.
- A user can review the properties on the reviews App.
- A user cannot edit or delete another user's comment or the own ones.
- A user must be logged in to be able to record their reviews.

#### Features left to implement

- A user can edit and delete their comments.
- Enable users to view reviews no.
- Allow users to store multiple credit cards to be use in different subscriptions.
- Allow users to request password reset emails.
- Allow landlords or landladies to reply directly on negative comments only.
- Needs styling work to be apply.


## Billing
The Billing app is used to use stripe within the Subscriptions App.


The app makes use of this python wrapper, designed for working with the IGDB API in python.
The information retrieved gives a games' name, cover image, a selection of screenshots, aggregate rating, date released, a summary, and a link to the IGDB page for the game to get more information.
Originally the cover images and screenshots sent through the api linked to small thumbnail images. These did not display well on the site due to the small sizes, so in the view for retrieving the data I edited the string of the returned url to link instead to where a full size image was hosted:

if 'cover' in game:
    game['cover']['url']=game['cover']['url'].replace("t_thumb","t_cover_big")

if 'screenshots' in game:
    for i in game['screenshots']:
        i['url']=i['url'].replace("t_thumb","t_original")
Existing Features
Users can use the bible to search for information about any game.
Information is presented in a simple layout, which gives the users access to screenshots, summary, rating, release date and link to get more information.
In the case of the rating the animated color progress bar will show a color appropriate to the rating: green, orange, or red.
The instances of no information for some of the returned values are handled in the following ways:
In the event a game has no cover image a default image will display instead.
No rating will display a grey animated progress bar stating no rating available.
Features left to implement
Enable users to search for a game they discovered in the bible in the sites' products directly, without having to enter the title in the search products bar. This should be relatively easy to implement.
Cart App
The cart app is used for adding products to a cart session and updating the cart.

Existing Features
Users can easily add items to a cart
Users can easily update the number of items in a cart and delete items from a cart.
The image for the cart in the navbar will display the amount of items currently in the cart
Checkout App
The checkout app is used for making purchases with stripe.

Existing Features
Users can enter address and card information for making purchases.
While making payment the order details are available on screen with an edit button should the user want to edit their cart before finalising purchases.
When purchases are complete users will be redirected to a confirmation screen where they can view their order details. Billing information is also available on screen.
Payment processing via stripe.
Features left to implement
Sending email confirmation upon succesful purchases.
Info App
The info app exists to create a sense of authenticity to the project as a whole.
Rather than having dead links in the nav and footer I created the info app and filled the individual urls with dummy data.

Existing Features
Working links to Contact, FAQ and Shipping information views.
Filled with dummy data.
The contact form redirects to the FAQ via a get request.
News App
The news app contains news articles sourced from the internet. Here the users can read and comment on the news articles.

Existing Features
Users can comment on news articles.
Features left to implement
The ability to like articles.
Number of views displayed on article.
When users edit or delete a comment the page is reloaded, I would like this to happen dynamically without needing to reload the page.
Products App
The products app contains all the information relating to the games found on the site.
For this project I wanted to work with a large amount of data in order to learn how to present it to users in an easily consumable/navigatable manner.
To this end there are over 1500 products in the database for users to look through. This is too much to render in a view all display.
It was important to consider how to construct the models in order to make the data easy to deal with and present to the user.
In the end there are three different models: Brand, Console and Game. Giving the Console model a foreign key to the Brand model and giving the Game model a foreign key to both Console and Brand made the data easy to work with and present in an intuitive fashion.

To source the products I used Beautiful soup to scrape data from consolemad.co.uk, an online retro gaming store. I wrote this script and ran it from the django shell.
The original site uses pagination in displaying their results. As a result I had to write a scrape function for multiple urls where it could recognise paginated pages on the site and scrape through each paginated page accordingly.
Originally, due to the amount of data, I chose not do download images for products, but rather linked them via url to the original image.
This caused issue however as when the original site sold an item, they took down the image link. As a result a product on my site would display no image if the corresponding product on theirs was sold.
To overcome this I attempted to write it into the view for retrieving and rendering products that, when filtering Game objects to be rendered, the view would check to see if the image link was returning a 404 status code. If it did then the game object with the broken image link would be deleted from the database before it could be rendered.
This slowed the process of filtering and returning games down too much, and also meant that my inventory of games would slowly decrease.
In the end I elected to expand the scrape function to also download images.

Context processors were written in order to easily work with and dynamically display the database models in the navbar and side navigation menu, rather than hardcoding them in the html.
In deciding how to present the brands, consoles and games for rendering in the navs and templates I decided to order the consoles and games alphabetically, while brands are ordered in reverse alphabetical order.
I did this as the brands which appear first in reverse alphabetical order (ie. Sony, Sega, Nintendo) have more consoles and games to display; and I feel they would be more popular.

Existing Features
Users can easily navigate through the products via brand and console.
There is also an ever present search bar in the side navigation menu where users can search for games by title.
Each product, when hovered on, will display two buttons; one to add the item to the cart, and the other to search for the item in the game bible where the user can get information about the product.
Product pages are paginated in order to load the pages quickly and present an easily consumable chunk of games on screen at one time.
Features left to implement
Several test users have noted that they would like to be able to include a console in the search bar when searching for a game (for example someone wanting to search for a Fifa game only on playstation 2 would like to search using 'fifa playstation 2'). This is a feature I plan to implement.
Run locally
Clone the github repository
Install requirements:
pip3 install -r requirements.txt
In base.py set debug to True.
Get a secret key and set it as an environment variable. You can get one at https://www.miniwebtool.com/django-secret-key-generator/
Set as an environment variable DJANGO_SETTINGS_MODULE equal to retroplay.settings.local:
migrate:
python3 manage.py migrate
Create a superuser:
python3 manage.py createsuperuser
You will need to update your allowed hosts in base.py.
The site will now run locally. There will be no products or news articles.
If you wish to use the game bible you will need to get an API key from IGDB and set it as an environment variable called IGDB_API_KEY.
Testing
Build Status
Automated testing was done using Travis-CI. Currently it holds an 86% coverage rate for the site's apps. 80 tests were written, however many of these were needless. At a later stage I would like to remove these and write more tests to achieve 100% coverage.
To run the tests, when you have the project running locally, enter:

python3 manage.py test
To get all tests to pass you will have to set an IGDB API key in your environment variables.

The site was tested on 21" monitors, 15" and 13" laptop screens and on an iPhone SE and iPhone 8 screen to test responsiveness.
It was also tested using chrome, firefox and safari.
There is an issue on very small screen sizes (iPhone SE size) where the large images on the home screen resize slightly when scrolling. This issue is not there on larger mobile screen sizes.

Manual tests were also done to ensure links/form submissions/model relationships/purchases/IGDB api usage worked correctly and that the site was defensively designed.

Manual testing was done to ensure:

The site works as intended.
User entered information was handled correctly (adding/editing/deleting comments, adding to and updating the cart, purchases etc).
Logging in and out and registering works as intended.
The Bible retrieves and displays data as intended.
Defensive design:
The checkout page is not accessible if no items are in the cart.
The checkout confirmation is only accessible when payment is complete.
Users can only enter comments on news articles when logged in.
Only a user who creates a comment can edit or delete it.
Issues
Due to the time constraints in creating this project I have not had time to satisfactorily refactor the code.
As a result there is some repeated code and some 'messy' code with needless complexity.
For example any view that checks for a search query (which is a majority of views) via a get request has the same code to redirect to the search_results view, as per below:

search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
I attempted to place this within its own function but it would not work. I would like to go back and get this working to reduce the amount of code.
I also must make time to include comments on code blocks where it is not immediately clear what the code is doing.

In addition to this the custom.css file where I wrote most of the custom styles for the site is not what I would consider to be best practice for writing css. I definitely wish to clean this up.

Occasionally the information returned in the Game Bible can be a little slow.

Deployment
The site is hosted on heroku.
Static assets are hosted on Amazon S3.

Credits
Media
Static images on this site that do not represent a product were all sourced from google images.
Products and their images were sourced from consolemad.co.uk
Font awesome was used for the various icons in the site.
Google fonts used - Press Start 2P, Libre Barcode 39 Extended Text & Orbitron.

Acknowledgements
Corey Schafer's video on web scraping with beautiful soup.
WDTutorials video on Django pagination
Code for the smooth scrolling effect on the animated arrow on the home screen was taken from css tricks.