# Atlas Gifts

![Gifts Image](https://github.com/shane-os/atlas-gifts/blob/main/media/home_page.jpg)

## Contents
[UX (User Experience)](#ux-user-experience)
 * [Project Goals](#project-goals)
 * [User Goals](#user-goals)
 * [User Stories](#user-stories)
 * [Site Owner Goals](#site-owner-goals)
 * [User Requirements](#user-requirements)
 * [User Expectations](#user-expectations)

[Site Layout and Design](#site-layout-and-design)
  * [Wireframes](#wireframes)
  * [Icons](#icons)
  * [Images](#images)
  * [Colour Scheme](#colour-scheme)
  * [Favicon](#favicon)

[Technologies](#technologies)
  * [Programming Languages](#programming-languages)
  * [Libraries and Tools](#libraries-and-tools)

[Database Architecture](#database-architecture)

[Features](#features)
  * [Developed](#developed)
  * [Future Implementation](#future-implementation)

[Testing](#testing)
 * [Code Validators](#code-validators)

[Resolution of Bugs](#resolution-of-bugs)

[Deployment](#deployment)

[Accreditation and Gratitude](#accreditation-and-gratitude)

[References](#references)

## UX (User Experience):

### Project Goals
 * The objective of the project is to create a website that enables users to purchase creative gifts tailored to the recipient's interests.
 * Users will be able to research the various products on offer in terms of price, weight and description.
 * Potential buyers can create their own accounts to pay for the desired gifts and deliver them directly to the gift recipient if they so choose.
 * Arising from the creation of the site, gift recipients and gift senders will enjoy a greater, more personlised experience than currently available.

### User Goals
 * Research and examine potential gifts.
 * Purchase gifts for family and friends.
 * Have delivery arranged to bring purchased items direct to gift recipients.
 * View past purchases made on the site.

### User Stories
 * As a user, I would like to research the various gifts available to purchase.
 * As a user, I want to be able to purchase my desired items.
 * As a user, I wish to arrange delivery of purchased gifts direct to their recipient.
 * As a user, I would like to create a personal profile to allow me to view my past purchases on the site.
 * As a user, I wish to contact the site administrator if an issue occurs or if I have a concern.

### Site Owner Goals
 * As a site owner, I wish to provide a range of products, that users are able to view and purchase.
 * As a site owner, I would like to provide a clear, simple process through which desired items can be purchased.
 * As a site owner, I want to provide a medium though which users can contact me about issues, suggestions, complaints or comments they have about the products on site.
 * As a site owner, I wish to promote my current product and future product offerings using a blog.
 * As a site owner, I want to be able to inform users of discounts or provide important store wide updates including potential delivery delays.
 * As a site owner, I would like to provide an individual profile for each user providing past order history and delivery details for a quicker purchasing process.

### User Requirements
 * Users are able to register an account and log in as required.
 * Users may view past purchases they made on the site (if any).
 * Gift search and filter capabilities operate as expected.
 * Products can be easily added to the shopping cart for payment.
 * Users can adjust the quantity of an item added to their cart.
 * Users can remove the gift entirely from the cart if they no longer wish to purchase the gift.
 * Customers are made aware of their shopping cart total as make their way through the site.
 * Purchase process is straightforward, secure and without error.
 * All internal site links redirect users to the appropriate section.

### User Expectations
 * Wide product selection on offer to purchase.
 * Product information and images are accurate, clear and well presented.
 * Users can directly contact the site administrator to dicuss any concerns or comments that they may have.
 * Delivery tracker portal is accurate and details the delivery process clearly to the consumer to avoid misunderstanding.

## Site Layout & Design:

### Wireframes
Initially, I wrote down all of the ideas that I had for this site. Once I had firmly decided on the project, I drew rough sketches of my vision for the site on pen and paper. Following the refining of my designs through more wireframe drafts, I created electronic versions of these wireframes using the Balsamiq Wireframes software. The final versions of the wireframes are stored in PDF format, for the following viewing mediums:

 * Mobile
 * Desktop
 * Tablet

### Icons
The majority of icons used throughout the project were obtained from the [font awesome](https://fontawesome.com/icons) collection. On the font awesome site an account was created to enable the creation of a new kit for the Atlas Gifts site. The icons utlised were specifically chosen to direct users to key parts of the site. By decorating navigation links and buttons with icons such as a shopping cart, bin, envelope or a profile, users are able to signup, login, select items and pay with less confusion. This will help to reduce the likelihood of a user dropping out of the key processes thst lead to purchases of gifts on the site.

### Images
The chosen images improved the asthetics of items available to purchase, providing much more details about the item than a description could. These came from a number of sites including unsplash and pexels. Please see the [references section](#references) at the bottom of this report for the referemces of individual photos.

### Colour Scheme

![Colour Scheme](https://github.com/shane-os/atlas-gifts/blob/main/wireframes/atlas_gifts_colour_palette.png)

For the Atlas Gifts project, I decided to use colours that convey a range of emotions to both inspire confidence in the site user and entice them to purchase particular items. For example: The indigo Dye shade of blue is used in the payment section of the website to invoke trust and security in the user. The colour palette seen above and the accompanying report available in the wireframes folder was created using the [Coolors.co](https://coolors.co/) website. The main colours utilised in this project were:

 * #000000 - Black - Headings & main body text
 * #083d77 - Indigo Dye - Payment processing area
 * #C41C1F - Venetian Red - Item bundles & delivery section
 * #11844A - Sea Green - Item bundles & shopping cart
 * #FC4C02 - International Orange Aerospace - Item bundles
 * #FFFFFF - White - Background & footer text

### Favicon

To enhance the website's design further, I created a favicon using the generator provided by [Favicon.ico](https://favicon.io/favicon-generator/).

## Technologies

### Programming Languages
 * [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
 * [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 * [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 * [Python](https://www.python.org/about/)

### Libraries & Tools
 * [Git](https://git-scm.com/)
 * [Github](https://github.com/)
 * [Gitpod](https://www.gitpod.io/)
 * [Balsamic Wireframes](https://balsamiq.com/)
 * [Bootstrap](https://getbootstrap.com/)
 * [Font Awesome](https://fontawesome.com/)
 * [Stripe](https://stripe.com/)
 * [Django](https://www.djangoproject.com/)

## Database Architecture

To enable data to be saved and recorded numerous data models were created as part of the django applications created:

<center><h2>Gifts Categories</h2></center>

Name  | Database Key | Field Type | Validation |
| ----- | ----- | ----- | ----- |
| Name | name | models.CharField | max_length=200 |
| Firendly Name | show_name | models.CharField | max_length=200 |

<center><h2>Gifts</h2></center>

Name  | Database Key | Field Type | Validation |
| ----- | ----- | ----- | ----- |
Category | category | models.ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL|
Stock Keeping Unit | SKU | models.CharField | max_length=25 |
Name | name | models.CharField | max_length=200 |
Description | description | models.TextField |  |
Price | price | models.DecimalField | max_digits=4, decimal_places=2 |
Weight | weight | models.DecimalField | max_digits=4, decimal_places=3, null=True, blank=True |
Image URL | image_url | models.URLField | max_length=1024, null=True, blank=True |
Image | image | models.ImageField |  |

<center><h2>Blog</h2></center>

Name  | Database Key | Field Type | Validation |
| ----- | ----- | ----- | ----- |
Title | title | models.Charfield | max_length=200 |
Categories | categories | models.ManyToManyField | 'Category', related_name='posts' |
Created By | created_by | models.TextField | 
Body | body | models.TextField | max_length=200 |
Posted Date | posted_date | models.DateTimeField | auto_now_add=True |

<center><h2>Contact Us</h2></center>

Name  | Database Key | Field Type | Validation |
| -----  | ----- | ----- | ----- |
| Name | name | models.TextField |  |
| Email | email | models.EmailField |  |
| Message | message | models.TextField |  |

## Features

### Developed
 * Navigation Bar
 * Account Registration
 * Account Login
 * Add Product
 * Shopping Cart
 * Stripe Payment Facility
 * Contact Form
 * Blog

### Future Implementation
 * Newsletter
 * Gift Wishlist
 * Recurring Orders
 * Frequently Asked Questions
 * Cryptocurrency Payments
 * Favicon
 * Delivery Tracker
 * Profile

Code Validators:
 * The HTML code was passed through the W3C Validator. One error found was the incorrect use of a p element as a child of a button element.
 * The CSS code was passed through the Jigsaw Validator and the three errors found were that of missing semi-colons.
 * The JavaScript code was passed through the JSHint Validator and the minor syntax mistakes were corrected.
 * The Python code files adhere to the PEP8 styling guidelines.


## Resolution of Bugs

### View Cart Items:
To make a purchase users must be able to view the gift selection on offer, select various items at various quantities and have them recorded in their personal cart. Users must then be able to view a summary of the items in their cart and edit or remove the items as required.

An issue arose when I tried to access the cart summary page after adding items to the cart. When the page is accessed either through clicking on the cart icon or typing the url in the browser. To determine the source of the error I examined the python files and cart html file for the cart app. After checking the model and view files and using the print function to help determine the error, I sought to make sure that the variable names were constant throughout the files. A small naming error was located between the files for the Gift Model. 

A second issue arose after the naming error had been solved. Unlike the previous error, this problem was resolved relatively quickly qith the help of the Tutor Support. Due to cached data from before the naming issue was resolved, attempts to access the cart summary were redirect to an error page. Once the cached data was deleted the summary page operated as expected once again.

## Deployment

To run the project locally please follow these steps:

1.  Go to the Atlas Gifts [repository](https://github.com/shane-os/atlas-gifts) on Github.
2.  Click the "Code" button and select the https option.
3.  Copy the link shown.
4.  In the Gitpod IDE (Integrated Development Environment) use the change working directory command ($ cd filepath)
5.  In the Git Terminal enter the git clone command ($ git clone filepath) where filepath is the link copied during step 3.

6. The project requires the installation of a number of python modules. For an individual module type the following into the terminal:

```
pip3 install module name
```

To install all of the modules required to run this project locally:

```
pip3 install -r requiremnts.txt
```

7. You will need to create a number of environment variables. Please create a new python file called env:

```
Environmental Variable Names and Keys
```

For the secret keys, a random key generator such as [randomkeygen](https://randomkeygen.com).

8. To migrate the models that are contained within the project code please enter the following in your development terminal:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

The above commands have created a local database.

9. To access the administrative panel that the Django framework creates, a superuser account will need to be created:

```
python3 manage.py createsuperuser
```

Once prompted you will need to enter a username, email address and a password. Create a strong password using a random password generator such as (Dashlane's password generator)[https://www.dashlane.com/features/password-generator]

10. To access the administrative panel run the server by entering the following into the terminal:

```
python3 manage.py runserver
```

Open the site using the "open browser" icon in the Gitpod Workspace. In the browser add "/admin" to the site address to get to the administration panel login. You will need to type in your username and password.


### Heroku Deployment

1. Log into your Heroku account

2. In the Git Terminal create the Procfile and requirements.txt file by entering the following into the terminal:

```
pip3 freeze --local > requirements.txt
```

3. Create the Procfile by entering the following into the terminal:
```
echo web: python app.py > Procfile
```

4. On heroku, select "Create a New App", input an app name and choose a region.

5. Select Github as the deployment method.

6. Add the Heroku Postgres to you project. Make sure to select the Hobby (Free) option . (This is where the database url in the table below comes from)

7. Select settings and click on "Reveal Config Vars".
Input the following environment variables:

|Key | Value |
| ---- | ---- |
| AWS_ACCESS_KEY_ID | Your AWS Access Key |
| AWS_SECRET_ACCESS_KEY | Your Secret Access Key |
| DATABASE_URL | Your Database URL |
| SECRET_KEY | Your Secret Key |

8. You will need to migrate the database models to the Postgress database on Heroku using the following:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

9. To access the administrative panel, a superuser will need to be created:

```
python3 manage.py createsuperuser
```

Once prompted you will need to enter a username, email address and a password. Create a strong password using a random password generator such as (Dashlane's password generator)[https://www.dashlane.com/features/password-generator]

10. To access the administrative panel in Heroku, click the deploy app button

## Accreditation & Gratitude
 * Code Institute Tutor Support: I would like to express my gratitude for the tutors help in resolving issues I faced in building the website. In particular, their help was invaluable in resolving the problem of the cart app not displaying.

 * I would like to express my gratitude fo my mentor Simen Daehlin's guidance in creating the project idea to meet the Milestone Project 4 guidelines and working through issues that I faced in the project.

 * Finally I would like to thank my family for their opinions on the colour scheme and for helping in testing the website.

## References
To create the Atlas Gifts project I researched a variety of styles and formats to determine the best combination for the site. Throughout the project I used the following resources:

 * [Code Institute](https://codeinstitute.net/): In particular I benefitted from the Boutique-Ado Walkthrough section of the course.

 * [Getbootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/): The starter template was utilised in creating the base.html file.

 * [Blog Template](https://realpython.com/get-started-with-django-1/#share-your-knowledge-with-a-blog): The Real Python tutorial was helpful in creating the site's blog.

In relation to the images used on the site for the background and gifts some were edited to improve their appearance on the site. The images can attributed to the following sources:

 * [Main Background Image](https://unsplash.com/photos/PxM8aeJbzvk)
 * [Christmas Puzzle](https://www.amazon.co.uk/Coppenrath-Jigsaw-Puzzle-German-Christmas/dp/B073ZHVDVM)
 * [Irish Favourites Basket](https://www.fiverr.com/irishsnack/send-you-your-favourite-irish-snacks)
 * [Mindfulness Journal](https://www.jennibick.com/products/black-leather-executive-journal)
 * [Sketching Kit](https://m.media-amazon.com/images/I/81i1gvARtvL._AC_SL1500_.jpg)
 * [Chocolate Fountain](https://m.media-amazon.com/images/I/61gIYrRI-EL._AC_SL1000_.jpg)
 * [World Scratch Map](https://m.media-amazon.com/images/I/91Pxr+oKNiL._AC_SS450_.jpg)
 * [Quiz Book](https://m.media-amazon.com/images/I/51wWwym5yeL.jpg)
 * [Advent Calendar](https://keyassets-p2.timeincuk.net/wp/prod/wp-content/uploads/sites/53/2020/09/918tz14E0L._AC_SL1500_.jpg)
 * 
