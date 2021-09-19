# MS4

# [Constant Reader](https://github.com/petracili/MS4.git)

## Contents

1. [Summary](#summary)
1. [UX](#ux)
    1. [Strategy](#strategy)
    1. [Scope](#scope)
    1. [Structure](#structure)
    1. [Skeleton](#skeleton)
    1. [Surface](#surface)
1. [Features](#features)
    1. [Existing Features](#existing-features)
    1. [Features left to implement](#left-to)
1. [Bugs](#bugs)
1. [Technologies used](#tech)
1. [Testing](#testing)
1. [Deployment](#deployment)
    1. [Github Pages](#github)
    1. [heroku](#heroku)
1. [Credits](#credits)
    1. [Content](#content)
    1. [Additional Content](#add-cont)
    1. [Acknowledgements](#acks)


# <a name="summary"></a> Summary
This site is an e-commerce store selling plants. The title of the website was inspired by problem with pollution of the planet earth. And the need to preserve the environment and thus the need for new plants due to a large number of cut forests and emissions of harmful gases.

This site provides an array of plants which can be searched, viewed by standard users, favourited by users which create a profile and added to, edited and deleted by store admin.

# <a name="ux"></a> UX
## <a name="Strategy"></a> Strategy
### **New site user's goals:**
* As a new site user, I want to be able to browse and search for plants
* As a new site user, I want to be able to view the details of individual plants
* As a new site user, I want to be able to understand the intent of the page
* As a new site user, I want to understand easily how to navigate the page and access the facilities provided
* As a new site user, I want to be able to make a purchase without needing to create a profile
* As a new site user, I want to be able to be able to easily create a profile
* As a new site user, I want to be able to be able to be able to amend the items in my bag including quantities and removing them entirely

### **Returning user's goals**
* As a returning site user, I want to be able to log in and out
* As a returning site user, I want to be able to recover a forgotten password
* As a returning site user, I want to be able to have a personalised profile
* As a returning site user, I want to be able to view my past orders

### **Site owner'as goals:**
* As a site owner, I want to be able to create, edit and delete plants
* As a site owner, I want to the ability to create, edit and delete plants to be limited to 

## <a name="scope"></a> Scope
**Functional requirements:**
#### For ease of use:
* Navigation bar which is simple and easy to navigate

#### To ensure the database is up to date and editable:
* Function to add a plants
* Function to edit a plants
* Function to delete a plants
* For the plants to be only editable by a superuser

**Content requirements:**
#### To ensure the site is visually appealing and to draw the user's eye:
* Images of plants
* Clear soft colours intending to draw the user into the site and to be soft on the eye whilst not detracting from or make the text unreadable

### For usability
* For links to be clear and for the page to be constructed in a way which is instructive enabling the user to instinctively navigate the page

## <a name="structure"></a> Structure
**Interaction design:**
* User friendly interface to ensure usability and to encourage the user to return
* Responsive and visible links which change on hover to provide user feedback as they navigate the site

**Information Architecture:**
* Navigation bar at the top of the page
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive images to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing
* All information is appropriate and relative to the subject and not misleading or hard to find

## <a name="skeleton"></a> Skeleton
Please click the below link to view the wireframe mock up of the website in mobile, tablet and desktop sizing

[Wireframe](/wireframe/)


## <a name="surface"></a> Surface
The intention of the website is to be whimsycal 

* The font family chosen is 'Segoe UI' as this has a whimsycal touch, close to a typewriter style text whilst also being clear and easy to read
* The colour scheme selected is a shade of green with a consistant cover image throughout the site.
* The cover image was selected as it shows the site is all about plants whilst also providing some clear space for text and not being too distracting as a cover image with content over the top of it

# <a name="features"></a> Features
## <a name="existing-features"></a> Existing Features
Feature | Details
--------|--------
Log in | The user can register and log into their own account with personalised features
Log out | There is a log out functionality on the page - this is especially important for users of a shared device
Add plants | Superusers can add plants to the site 
Edit plants | Superusers are able to edit plants
Delete plants | Superusers are able to delete plants
Search function | The users are able to search the plant database. This function is available whether a user is logged in/registered or not

## <a name="left-to"></a> Features left to implement
Feature | Details
--------|--------
Multipe genres per plant | The fixtures were set up to enable the use of mutiple genres however, due to issues in loading this data to the heroku database, the items needed to have only one genre
A filter for sale items | The fixtures were set up with a plants field showing if the item was on sale or not to enable items to be filtered by whether they are on sale
A facility to save 'favourited' plants | Links on each plant page allowing a user to save plants to their favourite list within their profile

# <a name="bugs"></a> Bugs
Bug | Fix
--------|--------
was unable to load models with multiple genres for an individual plant | Although I was unable to resolve this issue, a fix was to change this so that each plant only had one genre attached to it
An error occured when attempting to deploy the site in Heroku jango.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting | I added STATIC_ROOT to settings.py to solve the collect static error when deploying to Heroku

# <a name="tech"></a> Technologies Used
* [Bootstrap](https://getbootstrap.com/) 
* JavaScript
* https://fonts.google.com/
* www.validator.w3.org
* http://www.css-validator.org/
* Git
* Gitpod
* GitHub
* Google Chrome
* http://www.responsinator.com/
* Chrome Dev Tools
* Python
* Django
* Heroku
* Google Maps Marker Clusterer
* [FontAwesome](https://fontawesome.com/) - for the icons used
* [W3Schools Online Web Tutorials](https://www.w3schools.com) - for easier handling of codes
* [Animate.css](https://animate.style/) - for animating element on the landing page 
* [Google Fonts:](https://fonts.google.com/) - for font on webpage
* [HTML Color Codes:](https://htmlcolorcodes.com/) - for color codes and names
* Code Institute - for reminder of how the element is used
* [Grammarly](https://www.grammarly.com) - to correct grammar

# <a name="testing"></a> Testing
### **New site user testing:**
# <a name="testing"></a> Testing
### **New site user testing:**
* As a new site user, I want to be able to browse and search for plants
    1. Upon entering the site, users are automatically greeted with the page title and sub navigation bar
    1. There is a clear call to action to browse the plants
* As a new site user, I want to be able to view the details of individual plant
    1. Each plant can be opened in an individual page with more information available than on the main page
* As a new site user, I want to be able to understand the intent of the page
    1. Upon entering the page, it is clear the site is designed around plants. The main cover image shows a stack of plants and all links are clear and plant related
* As a new site user, I want I want to understand easily how to navigate the page and access the facilities provided
    1. The navigation bar has clear and easy to understand links
* As a new site user, I want to be able to make a purchase without needing to create a profile
    1. A user can checkout without the need to create a profile
* As a new site user, I want to be able to be able to easily create a profile
    1. A user can create a profile using the link in the nav bar
* As a new site user, I want to be able to be able to sort products on a page
    1. On the nav bar, there is a drop down box which allows the user to select specific genres
* As a new site user, I want to be able to be able to amend the items in my bag including quantities and removing them entirely
    1. The shopping bag has amend and delete buttons and the ability to increase the quantity

### **Returning user testing**
* As a returning site user, I want to be able to log in and out
    1. Upon entering the site, there is the option in the nav bar to register and log in
* As a returning site user, I want to be able to recover a forgotten password
    1. By using the Django all auth packages, this facility is available to users with a profile
* As a returning site user, I want to be able to have a personalised profile
    1. Users have a profile within which they can update their personal details
* As a returning site user, I want to be able to view my past orders
    1.  Within the profile page, there is a list of past orders 
    1. users can click on these orders to view the full details

### **Site owner testing:**
* As a site owner, I want to be able to create, edit and delete plnts
    1. There is a delete button on each plant
    1. There is an edit button on each plant which takes the user to a form where they can edit the content
    1. There is a form available from the nav bar to allow the creation of new plants
* As a site owner, I want to the ability to create, edit and delete plants to be limited to superusers
    1. The create edit and delete function is limited in two ways. Jinja logic is used within the html code and the @login_required decorator is used within the views. py document

### **Performance testing:**
1. Tested website responsiveness using http://www.responsinator.com/
    1. Results: The website is responsive to all device sizes without any unnecessary x-scroll
1. Tested the image size to ensure no image is to large and impacting the website loading times. I used the Google Dev Tools - Network
    1. Results: The site loading time is appropriate. The total website loading time is 1.1s is acceptable
1. Tested the images on the all books page using Google Dev Tools - Lighthouse
    1. Results: It was recommended that the images used were of a smaller size to improve download speed and cause less data consumption.
1. All HTML and CSS were tested using https://jigsaw.w3.org/css-validator/validator
    1. All but the templates resulted in errors that the Lang Doctype and Title were missing. This was to be expected as the details were being extended from the base template to did not need to be added
    1. All HTML pages resulted in errors where the Jinja template language was used
    1. None of these are actual errors within the code
	1. Some CSS errors were observed. However, the items highlighted were added intentionally to the CSS files and did create the desired affect
    1. Tested the website on the Google Chrome browser Version 89.0.4389.90 (Official Build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Microsoft Edge browser Version 89.0.774.63 (Official build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Firefox browser Version 82.0.3 (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested adding items to the bag
    1. Results: Successfully able to add an item to the bag
1. Tested increasing the quantity of items in the bag
    1. Results: Successfully able to increase the quantity of an item in the bag
1. Tested removing items from the bag
    1. Results:Successfully removed an item from the bag
1. Tested the stripe process using 4242 4242 4242 4242 which should be successful
    1. Results: Order completed successfully and the confirmation page appears
1. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - completed authentication
    1. Results: Authorisation screen appears then the order completed successfully and the confirmation page appears
1. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - selected declined
    1. Results: The payment fails and the user is returned to the checkout page. The appropriate error message appears
1. Tested the profile page and that the orders placed above show correctly
	1. Results: The two successful orders made during testing appeared on the right hand side of the screen

# <a name="deployment"></a> Deployment
## <a name="github"></a> Github Pages
1. Create a new repository or access an existing repository
1. Click the green Gitpod button to launch the project in Gitpod
1. Create an index.html file
1. Add the file to the staging area using the git add Functional
1. Commit the file using the git commit function, adding an appropriate commentary
1. Push the file to GitHub using the git commit and git push functions
1. Refresh your GitHub repository and click the 'Settings' tab
1. Scroll to the GitHub Pages section and select a publishing source
1. Click 'Save'
1. Click the URL created within the Settings - GitHub Pages section

**To clone the repository for local deployment:** 
1. On the main page of the repository, click the down arrow Code button
1. Click the download icon under the relevant section to clone with either HTTPS, SSH or GitHub CLI 
1. In Git Bash, change the current directory to the location you want the directory to be stored
1. Type git clone and then paste the URL you copied in step 2
    1. An example for HTTPS: `https://github.com/petracili/MS4.git`
1. Press enter - that's it, your clone has been completed! 


**To fork the repository:**
1. Navigate to the main page of the repository you wish to fork
1. Click the Fork button on the top right hand side of the page

## <a name="heroku"></a> Heroku
### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/petracili/MS4.git), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('recipe-nation') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the settings.py file:

|**Key**|**Value**|
|:-----|:-----|
AWS_ACCESS_KEY_ID|'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY | 'AWS_SECRET_ACCESS_KEY'
|DATABASE_URL|'DATABASE_URL'|
|EMAIL_HOST_PASS|'EMAIL_HOST_PASS'|
|EMAIL_HOST_USER|'EMAIL_HOST_USER'|
|SECRET_KEY|'SECRET_KEY'|
|STRIPE_PUBLIC_KEY|'STRIPE_PUBLIC_KEY'|
|STRIPE_SECRET_KEY|'STRIPE_SECRET_KEY'|
|STRIPE_WH_SECRET|'STRIPE_WH_SECRET'|
|USE_AWS|True|

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

## <a name="acks"></a> Acknowledgements
* Ed Bradley - I also used this readme as an example of how to deploy Heroku
    * https://github.com/Edb83/self-isolution

* My mentor Antonio Rodriguez who has provided me with guidance and support through the project

