# Atlas Gifts Testing Document

## Contents
* Code Validators
* Homepage
* Navigation Bar
* Footer
* Blog
* Gifts
* Shopping Cart
* Purchases
* Profile
* Contact Page

## Code Validators
* The HTML code was passed through the W3C Validator. One error found was the incorrect use of a p element as a child of a button element.
* The CSS code was passed through the Jigsaw Validator and the three errors found were that of missing semi-colons.
* The JavaScript code was passed through the JSHint Validator and the minor syntax mistakes were corrected.
* The Python code files adhere to the PEP8 styling guidelines.

Devices used to test Atlas Gifts Site: HP Laptop (15" Screen), HP Desktop (23" Screen), Samsung Galaxy Tablet (10" Screen), Samsung Phone (5" screen)

## Homepage
User Story: As a user, I would appreciate a high-quality, aesthetically pleasing homepage to welcome me to the site.

When a user accesses the site, I wish for them to be excited by the homepage. They should feel instantly welcome and have a desire to explore the rest of the site. To encourage this, warm, bright colours were primarily used for the site. 

Tests:
 * Test Carousel Display 
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

To test the homepage's responsiveness and performance, the page was accessed using a variety of devices and a Lighthouse report was run for both desktop and mobile formats. Initially the site's dekstop performance was 80 and its accessiblity was 87. After looking at the performance issues identified I utilised the [Tinypng](https://tinypng.com/) to reduce the storage size of the homepage background image. Without compromising on the image, the size of the file was reduced by approximately 65%. In addition I added labels to the buttons on the homepage. As a result of these changes the Lighthouse performance rating increased to 91 and the accessibility increased to 91.

![homepage_desktop](https://user-images.githubusercontent.com/72452781/165378805-8ea99e7a-62c1-4416-91d6-b1f9b55696fc.png)
