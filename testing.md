# Atlas Gifts Testing Document

## Contents
* [Code Validators](#code-validators)
* [Homepage](#homepage)
* [Navigation Bar](#navigation-bar)
* [Footer](#footer)
* [Blog](#blog)
* [Gifts](#gifts)
* [Shopping Cart](#shopping-cart)
* [Purchases](#purchases)
* [Profile](#profile)
* [Contact Page](#contact-page)
* [Conclusion](#conclusion)

## Code Validators
* The HTML code was passed through the [W3C Validator](https://validator.w3.org/). One error found was the incorrect placement of <h2> tag.
* The CSS code was passed through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/). No errors were found.
* The JavaScript code was passed through the [JSHint Validator](https://jshint.com/) and the minor syntax mistakes such as missing semi-colons were corrected.
* The Python code files adhere to the [PEP8 styling](https://peps.python.org/pep-0008/) guidelines.

Devices used to test Atlas Gifts Site: Laptop, Desktop, Tablet, Phone. The responsiveness of the site was checked using the Developer Tools in the Google Chrome Browser.

## Homepage
* User Story: As a user, I would appreciate a high-quality, aesthetically pleasing homepage to welcome me to the site.
* User Story: As a user, I would like to be able to access the site across various devices, particularly by using a phone.

When a user accesses the site, I wish for them to be excited by the homepage. They should feel instantly welcome and have a desire to explore the rest of the site. To encourage this, warm, bright colours were primarily used for the site. 

Tests:
 * Test Carousel Display (CRUD Functionality)
 * Homepage Responsiveness

To test the carousel's create, read, update and delete functions, the following steps were taken:
1. The site was accessed using a variety of browsers and devices without logging in. As expected the text displayed on the carousel changed every 3-4 seconds.
2. The left and right arrows were clicked to check that the user could move between content.
3. To check the create, update and delete functions, a superuser profile was logged into. The text carousel appears as before but shows three new buttons: "Add new home page content", "Edit Content" and "Delete Content". 
4. Each button brings the site admin to their respective form. For Example:

![new_home_page_content_desktop](https://user-images.githubusercontent.com/72452781/165380472-1b77e153-0935-4664-b1ad-7da9a2467451.png)

5. Three seperate pieces of content were created using this form.
6. Each of the three pieces of content were updated using the "Edit Content" form
7. The content items were then deleted and later restored, demonstrating CRUD Functionality.
8. After each content piece creation, update or deletion a toast message notification appears on screen.

Lighthouse Report

To test the homepage's responsiveness and performance, the page was accessed using a variety of devices and a Lighthouse report was run for both desktop and mobile formats. Initially the site's dekstop performance was 80 and its accessiblity was 87. After looking at the performance issues identified I utilised the [Tinypng](https://tinypng.com/) to reduce the storage size of the homepage background image. Without compromising on the image, the size of the file was reduced by approximately 65%. In addition I added labels to the buttons on the homepage. As a result of these changes the Lighthouse performance rating increased to 91 and the accessibility increased to 91.

![homepage_desktop](https://user-images.githubusercontent.com/72452781/165378805-8ea99e7a-62c1-4416-91d6-b1f9b55696fc.png)

## Navigation Bar
* User Story: As a user, I want to be able to easily navigate the different sections of the site.

Test:
 * Navigation Bar Links

Users will see 1 of 2 versions of the navigation bar depending on their profile authentication and whether they are are a super user:
1. Anonymous/ Not Signed-In: The navigation bar will only show links for the homepage, blog, contact form, sign-in, registration and shopping cart
2. Super User/ Ordinary User Signed-In: The navigation bar will be the same as the previous group but with the sign-in and registration links replaced with a link to their respective profile and a log-out option.

Firstly, the navbar was tested by clicking on the links as a user that has not signed-in. Then each link was tested as an authenticated user and finally with a superuser profile. Each link was tested repeatedly and arrived at the expected page.


## Footer
* User Story: As a user, I want to able to follow the company on its various social media pages, so that I can find out about special offers, new products and discounts.

Tests:
 * External Links
 * Positioning

To enable users to follow the site on various social media, I placed 5 social media icons in the footer of the site: Facebook, Twitter, Instagram, Youtube and Tiktok. The intended target for each icon is the social media platform's homepage. I clicked on each icon and as expected a new tab is opened in the browser taking the user to the correct homepage. As lighthouse reports for each page noted that labels were lacking for the icons, labels were added to each footer icon corresponding to their correct platform.

It is intended for the footer to remain at the bootom of the user's screen regardless of the page size. This is to allow for a cleaner site appearance for the user. To validate this, the site's pages were accessed on a variety of devices and on each applicable page, the viewer scrolled to the bottom of the screen and checked that the footer was positioned at the bottom of the screen and was not covering any other site content.

## Blog
* User Story: As a user, I would like to be able to read articles about updates to the site's product offerings, changes to the site and other important information.

To inform site visitors about upcoming events, new product launches, sales announcements, etc. a blog has created. This should be both eyecatching and informative. The CRUD functionality allows the site administrator to delete, change and add blog posts as required. This encourages users to visit the site more frequently to find out the latest information.

Tests:
* Blog Display (CRUD Functionality)
* Sort Function

To test the blog's create, read, update and delete functions, the following steps were taken:
1. The blog page was accessed using a variety of browsers and devices without logging in. As expected the the blog posts appeared on screen
2. The left and right arrows were clicked to check that the user could move between content.
3. To check the create, update and delete functions, a superuser profile was logged into. Next to each blog post was an update and delete button. The create button appears at the top of the blog posts.
4. Each button brings the site admin to their respective form.
5. 3 new test posts were created.
6. Each post was edited and saved.
7. After the changes were verified, the 3 posts were deleted.

With regards to the sort function, the user can sort alphabetically and by the publishing date of the post. The various options were checked and each ordered the blog posts in the correct order.

Lighthouse Report

Desktop

![blog_desktop](https://user-images.githubusercontent.com/72452781/165862718-75d27ce0-c94e-401b-92ca-d46cb28c2822.png)

Mobile

![blog_mobile](https://user-images.githubusercontent.com/72452781/165862792-01ee07ce-2c54-4d2b-8048-697a53595620.png)

To improve the aethetics of the site on mobile devices, a maximum height was set for the blog post images. The card format was also widened slightly on smaller devices to allow for a more comfortable reading experience for the site visitor. 

## Gifts
* User Story: As a user, I would like to be able to easily search the product offerings and sort the product display as appropriate.
* User Story: As a user, I want to see a high quality image of each product so that I picture the object in my mind.
* User Story: As a user, I wish to be able to find out more information about a particular product being offered.
* User Story: As a user, I would like to be able to easily add an item to my shopping cart.

Testing:
* Searchbar
* Gift Images
* Gift modal
* Add items to the shopping cart
* Gift Management CRUD Functionality

As more products are added to the site, users are going to incur more difficulties in finding their desired product. To help the user find their desired product, a searchbar is present at both the top of the homepage and the gifts page. In the event that a user misspells their search term or enters a value that is not present in our gifts data, the user is redirected to the gifts page without any filtering taking place. They will receive a toast message informing them that their search attempt was invalid.

As most users will require a visual reference point to aid them in determining if they want to purchase a particular gift, the administration form to add a gift requires the site administrator to upload a photo. Attempts were made to add products to the site using this form without uploading an image. Each time, the form submission was prevented until an image was uploaded.

To ensure that the user receives as much information as possible to make an informed decision, more information as well as the option to purchase the item, can be accessed by clicking on the "More Info" button. The user is provided with a larger image of the product and a detailed description of the product, including the weight and price. The user is able to use the plus and minus buttons to increase/ decrease the item quantity before adding this their cart. To check that users are able to add products to their carts, various quantities of multiple items were added to the cart. As a user adding a quantity of 0 or less to their cart would not make sense, a check was built-in to prevent users from changing the input quantity to less than 1.

The ability to add, update and delete gifts from the site is critical to the site being successful, as without the products there won't anything to sell. To ensure that CRUD functionality was achieved I logged in as a superuser, created a series of test gifts with various prices, descriptions, etc. Then I proceeded to edit these items before logging out and return to the site as an anonymous user. After checking that I was unable to access the create, update or delete function as a non superuser I attempted to add each of these gifts to the shopping cart. After this successful check, I logged back in as a superuser before deleting each of the test items.

Lighthouse Report

Desktop


![gifts_desktop](https://user-images.githubusercontent.com/72452781/165869639-c56acd31-7295-4bfa-b0e8-741bb57242af.png)


Mobile

![gifts_mobile](https://user-images.githubusercontent.com/72452781/165869661-f18af414-1b22-4154-b58f-ac1219c9c9dd.png)

## Shopping Cart
* User Story: As a user, I would like to be able to view my shopping cart and adjust the quantities as I desire.
* User Story: As a user, I want to be able to view an up to date total of the items in my shopping cart
* User Story: As a user, I would like to be made aware of any applicable discount and/or additional charges, including delivery.

Between adding items to their shopping cart and checking out, customer may change their mind and wish to remove items from their cart or purchase a greater/ lesser quantity of a particular item in their cart. The shopping cart icon in the navigation bar displays a running total of the value of the items in the cart. 

Testing:
* Shopping Cart create, read, update and delete functionality
* Delivery Charge
* Discount Amount

When a user first logs on to the site an empty shopping cart is automatically created. As they add items to their cart, the total displayed next to the shopping cart icon is increased. There is a standard ???5 delivery charge that is added to every cart but only after the first item is added to the cart. To entice customersto spend a little more, there is an automatic 10% discount when the user spends more than ???100 excluding delivery. To test this, items were added to the cart while logged in and also in incognito mode. As expected the delivery charge was only added after the first item was put into the cart. To determine the success of the discount function, various items were added to the cart to reach a total of greater than ???100. Once the cart's total was greater than ???100 (excluding delivery) it automatically deducted 10% from the toal. To ensure complete transparency in the calculations I have created a summary table on the cart summary page. This table clearly explains the total discount(if any), the standard delivery charge and the final payable amount.

To test the update and delete functions of the cart with regards to specific items, various items were added to the shopping cart and their quantities were updated in the shopping cart summary page. To confirm the update, the update text must be clicked. To remove an item, the remove text must be clicked. Various items were removed from the cart both by the "remove quantity" text and by reducing the line item quantity using the minus button. The tests were successful as these functions operated as expected.


Lighthouse Report

Desktop


![shopping_cart_desktop](https://user-images.githubusercontent.com/72452781/165879707-accf543a-65cf-4c8c-968b-c8b04ce3e509.png)


Mobile

![shopping_cart_mobile](https://user-images.githubusercontent.com/72452781/165879799-887e6268-8acc-4657-99a0-f1fc14e3c9cb.png)

To improve the accessibility of the page aria labels were added to the various buttons on the page. This had the effect of slightly improving the accessibility metrics for both Desktop and mobile formats.

## Purchases
* User Story: As a user, I want to be able to purchase my items anonymously, if I so wish at that time.
* User Story: As a user, I wish to be able to purchase the items in my shopping cart in a timely manner.
* User Story: As a user, I want to receive an order confirmation email when I make a purchase.

To encourage repeat business, the payment process should be as quick and easy as possible. To allow for this, the form's layout is simple and straightforward.  Customers must have confidence in the payment process or else they will stop prior to completing the payment process.

Testing:
* Successful Purchase of Cart Items
* Order Confirmation Email

To test the payment function the following steps were take:
1. Numerous shopping carts of varying values were created as a superuser, registered users and anonymous users.
2. A few attempts were made when the form was incorrectly filled out. However, the form successfully picked up on this and instructed the user on the missing/ incorrect fields.
3. Different stripe test cards were used to trigger certain events. For example the recurring 4242 test card is supposed to result in a successful payment.
4. Successful payments were determined to have occurred when the successful payment Stripe webhook event returns a 200 'success value' in the Stripe dashboard and the payment is shown as complete in the test dashboard.
5. To ensure users do not leave/ refresh the page a message appears after clicking on the "Pay Now" button, informing the custoemr that their payment is being process.
6. Finally, the order confirmation email function was tested by setting up a number of email accounts and providing these addresses in the payment form. As expected the order confirmation emails were received at the designated email addresses.

Lightouse Report

![purchases](https://user-images.githubusercontent.com/72452781/165882642-e2b87588-361d-441c-bada-56209461599b.png)


## Profile
As a user, I wish to register for a profile for myself.
As a user, I would like to be able to to view my past purchases on the site, if I have a profile.

Testing:
* Profile Registration
* Profile Destils
* Past Purchase History

To build customer loyalty, users are encouraged to register for a profile on Atlas Gifts. Users are able to save their delivery details securely on their personal profile page to enable faster checkout. By setting up an account on the site, customers will be able to access the records of their past purchases from Atlas Gifts.

To test the profile registration capability, a series of attempts to create profiles were made. Many of these attempts were designed to check for whether 2 profiles could be created using the same username or email address or without an email address at all. The form was successful in preventing users from creating duplicate profiles/ without key details. After each profile was successfully created the personal details form fields were edited and saved to authenticate the profile information uodate function. These tests were determined to be successful.

With regards to accessing past purchase history the following steps were followed:
1. A series of purchases were made using different profiles. 
2. The order summary was copied after the payment had been processed.
3. After a successful webhook event is triggered and an email confirmation order had been received, I logged out of the profile and logged back in. This was to ensure that the past purchase history was correctly allocated to the user who made the purchase.
4. I checked the purchase history of the user against the saved order summaries.


Lighthouse Report

Desktop

![profile_desktop](https://user-images.githubusercontent.com/72452781/165883587-a52a9e45-bdf1-4fc1-9719-c9a77fa68ed8.png)


Mobile

![profile_mobile](https://user-images.githubusercontent.com/72452781/165883570-c8e32e22-3a1b-49f9-9072-0897e57ef05c.png)

To improve the responsiveness of the page, small adjustments were made to the width, padding and font size of the cards.

## Contact Page

* User Story: As a user, I wish to contact the site administrator if an issue occurs or if I have a concern.

Testing:
* Contact Form 

Should a customer require more information about a product, the expected delivery dates or they wish to make a complaint, the contact form provides a medium through which they are able to do so. The form was kept simple to presuade people to reduce the likelihood of a visitor leaving the form and site part of the way through sue to the process being too arduous. The form was created using the django crispy forms package.

The testing process for the contact form was to ensure that the user could not leave any of the four fields (Name, Subject, Email Address and Message) could be left blank and that a record of their form submission is sent to the email address provided. This is give customers some confidence that their query will be dealt with in a timely manner. To determine the contact form's success/ failure I attempted to submit a number of forms while leaving a field blank. The site prevented me from doing so. To ensure that the contact form's email sending process was working I sent submitted a number of forms with different email addresses in the email field. Th e contact form was successful in sending a copy of the submission to each email address.

Lighthouse Report

Desktop

![contact_desktop](https://user-images.githubusercontent.com/72452781/165865590-0c733f7b-054e-43d9-97a9-53938637cdec.png)

Mobile

![contact_mobile](https://user-images.githubusercontent.com/72452781/165865719-8b917e8f-2169-414e-8e37-faa71d82bb95.png)

## Conclusion
From the testing conducted on the areas named in the above sections, it is clear to me that the responsiveness of pages can vary significantly between devices. I notice that the following areas had a significant impact on Performance/ Accessibility Metrics:

 * Utilising tinyng and similar websites to reduce image file sizes. This had an immense impact on the homepage and also the gifts page as both of these areas rely on quality images to retain customers.
 * Naming conventions: Using suitable label names for buttons, forms, links, etc. had a substantial impact of the Accessibility metric.

In terms of areas of improvement, I have noticed opportunities in using more up to image file formats and removing potneital code duplications.
