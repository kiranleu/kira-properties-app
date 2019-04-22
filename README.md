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



#### Current Features

- Users can register, log in and log out in the website.
- A user can review the properties on the reviews App.
- A user cannot edit or delete another user's comment or the own ones.
- A user must be logged in to be able to record their reviews.

#### Future Features

- A user can edit and delete their comments.
- Enable users to view reviews no.
- Allow users to store multiple credit cards to be use in different subscriptions.
- Allow users to request password reset emails.
- Allow landlords or landladies to reply directly on negative comments only.
- Needs styling work to be apply.


## Billing App

The Billing app is used to use stripe within the Subscriptions App.


#### Current Features

- User can add a credit card through a payment form
- User can subscribe
- User can choose between two subscriptions> Monthly or Yearly


####Future Features 

- Add multiple cards



## Checkout App

The checkout app is used for making purchases with stripe.

#### Current Features

- Users can enter card information for making purchases.
- When user had chosen a subscription type, users will be redirected to their profile page where the subscription type is shown.
- Payment processing via stripe.

#### Future Features 

- Being able to send a personalised email that confirms that the subscription purchase have been processed.

## Rented properties App

The purpose of this App is: 

1. Add a property: User signed up can add a new property with their landlord/landlady to be review by other users.
2. Added property: Where users are redirected once they have added a property.
3. Homepage: Where the whole journey of review your Landlord site begins with a small explanation of what it is the site about.
4. Rented Properties detail: Here the user will log all the detials in the form about the property.
5. Rented properties list: Place where all the list of properties is shown.

#### Current Features

- Links to each property details.
- The add property form redirects the user to the full list of properties.

#### Future Features

- Delete the data after the user(tenant) has left the property reviewed.
- Add begining date and end date of renting the property

## Reviews App

The reviews app contains agives the ability to the users to read and write more reviews about the properties already created by others. 

#### Existing Features

- Users can review on new or old properties listed.

### Future features

- The ability to rate the landlord/landlady based on the users experience and review of the property.
- How many times the reviews where viewed.
- Allow users to edit and delete their previews reviews.

## Registration App

#### Current Features
Within this App the users can:

1. Log in
2. Sign Up
3. See their profile
4. Reset password

#### Future Features
- Being able to reset password using the email address



## How could you run this project locally?

Please follow the next steps:

##### Clone the github repository that you could access through this link: https://github.com/kiranleu/kira-properties-app 

##### Install requirements:
    pip3 install -r requirements.txt
    
    In base.py set debug to True.

##### Get a secret key, you can use the follwing link where automatically will be created a secret key.https://www.miniwebtool.com/django-secret-key-generator/
This  secret key will  need to be configure as an environment variable.

##### In DJANGO_SETTINGS_MODULE make sure it is set to be equal to retroplay.settings.local:

Now you will  need to migrate:

    python3 manage.py migrate
    
##### You will need to create a superuser, find the steps below:
    
    python3 manage.py createsuperuser
    
##### Now, update your allowed hosts within the base.py.

The site can be run locally. Although we won't be able to find any properties, reviews in it.

## Testing

# Automated test

- Travis-CI. Currently it holds an 86% coverage rate for the site's apps. 80 tests were written, however many of these were needless. At a later stage I would like to remove these and write more tests to achieve 100% coverage.
To run the tests, when you have the project running locally, enter:

python3 manage.py test
To get all tests to pass you will have to set an IGDB API key in your environment variables.

The site was tested on 21" monitors, 15" and 13" laptop screens and on an iPhone SE and iPhone 8 screen to test responsiveness.
It was also tested using chrome, firefox and safari.
There is an issue on very small screen sizes (iPhone SE size) where the large images on the home screen resize slightly when scrolling. This issue is not there on larger mobile screen sizes.

Manual tests were also done to ensure links/form submissions/model relationships/purchases/IGDB api usage worked correctly and that the site was defensively designed.

# Manual testing

- The site is working although it has so much room for improvement.
- th information the Users enters is kept vorrectly within the DB.
- Logging in and out is working correctly.
- Reviewing landlods is working.
- Links within the website are working
- Buttons are fully redirecting properly

# Security Design

- The Susbcription page is not accesible without adding a credit card.
- The data recollected about the credit card is encrypted so only the last 4 digits of the card are visible.
- Users can only add a property when they are logged in.
- Users only can write a review within theproperties when logged in or signed up.

Issues

The code used it has much room for improvement.I dwould definetly would like to have more time to improve it. although my experience had let me go this far,
from here and more practice will let me demostrate how much I could do within this project.


I wrote most of the custom styles using in my CSS files

Sometimes, loading images can take can be slower as intended.

## Deployment

It is hosted using HEROKU.

All the Static assets used are hosted on Amazon S3.

# Credits
#### Media that appears on the project

Static images were obtained from GOOGLE, UNSPLASH images.


