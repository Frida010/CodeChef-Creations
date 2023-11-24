# CodeChef Creations

Welcome to CodeChef Creations! This Django-based blogging website offers a unique blend of programming and culinary delights. Explore posts and recipes curated by the **CodeChef** community. Our blog is designed for coding enthusiasts who seek to maintain a healthy lifestyle while spending long hours in front of their screens. The recipes are not only delicious but also infused with programming references and style, making them a delightful read for those familiar with coding.

For a live demonstration of CodeChef Creations, visit [this link](https://codechef-creations-aedba97ffd5b.herokuapp.com/).

## Table of Contents

- [Getting Started](#getting-started)
- [Design Philosophy](#design-philosophy)
- [Features](#features)
- [User Guide](#user-guide)
- [Post Detail Page](#post-detail-page)
- [Categories Page](#categories-page)
- [Responsive Design](#responsive-design)
- [Object-Based Software Concepts](#object-based-software-concepts)
- [Admin Panel](#admin-panel)
- [Testing](#testing)
- [Solved Bugs](#solved-bugs)
- [Remaining Bugs](#remaining-bugs)
- [Validator Testing](#validator-testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Content](#content)
- [Media](#media)

## Getting Started

Using CodeChef Creations is a breeze! While an account is not mandatory for browsing, creating one allows you to engage with the community, leave comments, save posts, and like posts.

### Steps to get started

1. Navigate to the CodeChef Creations website.
2. Browse through the diverse range of available posts.
3. Click on any post that piques your interest to delve deeper into its contents.
4. To actively engage with the community, sign up for an account and unlock the ability to leave comments, save posts, and like posts.
5. Explore specific interests by navigating through categories such as Healthy Salads to find posts that align with your preferences.

![Screenshot of the websites homepage](https://user-images.githubusercontent.com/129947589/284567988-f6865f1c-9c4b-4dd4-9b90-b5d25dd9ae54.png)

# Design Philosophy

CodeChef Creations prioritizes a user-centric design to ensure a seamless and enjoyable experience for coding enthusiasts exploring our blogging platform. Here's a detailed overview of my UX design principles:

### Color Palette and Styling Choices

I opted for a calm color palette to instill peace and tranquility into the platform while maintaining readability. Subtle gradients and clean typography enhance the overall aesthetics. For example, categories and links feature a soothing green color to provide a sense of familiarity and calmness.

### Iconography

Our iconography is thoughtfully selected to intuitively convey actions and features. The heart icon represents liking a post, creating a familiar social media interaction, while the bookmark signifies saving a post for later reference.

### User-Centered Approach

Design decisions are meticulously crafted with a deep understanding of users' needs. The goal is to create an environment where coding enthusiasts can effortlessly access valuable content and actively engage with the community.

### Responsive Design

CodeChef Creations is meticulously crafted with a responsive design, ensuring a seamless experience across various devices. Whether browsing on a desktop, tablet, or smartphone, users can expect a consistent and visually pleasing layout.

### Intuitive Navigation

Clear and concise navigation lies at the core of the design. The user interface is meticulously designed to guide users easily through the website, simplifying the process of discovering posts, engaging with the community, and exploring diverse categories.

### Technical Challenges and Solutions

During the development phase, I faced several technical challenges that required innovative solutions to enhance the overall performance and user experience of CodeChef Creations.

#### 1. Optimizing Image Loading

One significant challenge revolved around optimizing image loading for different screen sizes. To address this, I implemented responsive design techniques. By leveraging media queries and adaptive image loading strategies, we achieved not only improved performance but also ensured visual consistency across a diverse range of devices.

#### 2. Icon Clustering on Smaller Screens

Another noteworthy issue arose concerning icon clustering, negatively impacting the user experience on smaller screens. Icons for actions like liking, commenting, and saving posts were prone to overlap and become visually cluttered. To rectify this, I applied responsive design updates and adjusted CSS styles. These refinements ensure that icons now display appropriately on all screen sizes, maintaining clarity, proper spacing, and legibility. As a result, users can enjoy a visually pleasing and functional interface, regardless of their device's screen dimensions.

#### 3. Making Images Clickable Links

I identified a usability issue where users had to click specifically on the blog post text beneath an image on the homepage to be redirected to the corresponding blog post. This suboptimal experience prompted me to implement a solution that significantly improves user interaction.

To enhance the user experience:

1. **Whole Blog Post View as a Link:**
   I modified the design to make the entire view of the blog post on the homepage act as a clickable link. Now, users can click anywhere within the blog post preview, not just on the text, to navigate to the respective blog post.

2. **Hover Effect for Clarity:**
   To provide a visual cue to users, I added a hover effect to the blog post preview. When users hover over the blog post section, it subtly indicates that it is clickable, reinforcing the idea that interacting with this area will lead them to the detailed blog post.

These adjustments contribute to a more intuitive and seamless browsing experience on CodeChef Creations, eliminating the need for users to pinpoint a specific area to access detailed content.

# Features

* **No login required for browsing:** Explore posts without the need for an account.
* **User authentication system:** Engage with the community by leaving comments and liking posts.
* **Categories menu:** Filter posts by relevant topics and interests, making it easy to find content that suits your preferences.

### Navigation

* At the top of the page, you'll find the blog's name: CodeChef Creations. Clicking it redirects you to the homepage.
* On the right side of the logo, you have navigation links to the Homepage, All Categories, Register, and Login. If you're logged in, additional links include Saved Posts and Logout.
* The navigation employs a clean and modern font, with a color that contrasts the background.
* Clear navigation guides users to easily find what they are looking for.

![Screenshot of the header](https://user-images.githubusercontent.com/129947589/284935409-cdfe9bcc-b104-4d98-8773-24b16334b338.png)

# User Guide

### Creating an Account

To create an account, follow these steps:

1. Navigate to the **Register** page.
2. Enter your preferred username, optional email, password, and repeat the password.
3. Click the **Sign Up** button.

### Leaving Comments

To leave comments, follow these steps:

1. Navigate to the post you want to comment on.
2. Scroll to the bottom of the blog post.
3. In the "Leave a Comment" text input, write your comment.
4. Click the **Submit** button.
5. Your comment is awaiting approval from the admin.
6. Once approved, the comment will be displayed on the blog, and the comment count will increase under the comment icon next to the heart and save icons.

![Screenshot of leaving a comment](https://user-images.githubusercontent.com/129947589/284568114-7c51f980-5185-4120-9bd0-509aecfd3963.png)
![Screenshot of comment awaiting approval](https://user-images.githubusercontent.com/129947589/284568141-268753f8-7dc8-4f78-97a8-a0d9c32d244f.png)
![Screenshot of comment approved and live on the blog](https://user-images.githubusercontent.com/129947589/284568212-597718ce-041b-4890-9c1b-19e7cf7d5954.png)

### Saving Posts

To save posts, follow these steps:

1. Navigate to the post you want to save.
2. Scroll to the end of the blog post.
3. Click the bookmark icon to save the blog post for later.
4. Access all your saved posts by clicking the **Saved Posts** link in the navbar.
5. To unsave a blog post, click the bookmark icon again.

![Screenshot of saving a post](https://user-images.githubusercontent.com/129947589/284568275-cf568a49-a652-4d53-9bd9-44d8a3e4fe6f.png)

### Liking Posts

To like posts, follow these steps:

1. Navigate to the blog post you want to like.
2. Scroll to the end of the blog post.
3. Click the heart icon to like the post.
4. The heart icon will turn red, indicating your like.
5. The like count will increase with each like.

![Screenshot of liking a post](https://user-images.githubusercontent.com/129947589/284568308-cd64e616-afcd-4ef0-8f29-9cd6fe2d3138.png)

# Post Detail Page

The Post Detail page provides users with a comprehensive view of an individual blog post, offering a rich and immersive experience. Here's a breakdown of the key components:

### Blog Post Content

The main body of the page displays the entire blog post, allowing users to read through the content seamlessly. It includes text, images, and any other media that contributes to the post.

### Featured Image

Each blog post is accompanied by a visually appealing featured image. This image serves as a preview and sets the tone for the content within the post.

### Comments Section

Users can engage in discussions and share their thoughts by scrolling down to the comments section. Here, they can read existing comments, post their own, and interact with other community members.

### Likes and Bookmarks

For user engagement, the page displays the number of likes the post has received. Users can express their appreciation for the content by clicking the heart icon. Additionally, the bookmark icon allows users to save the post for later reference.

### Responsive Design

Ensuring a consistent and visually pleasing experience across various devices, the Post Detail page is designed with responsiveness in mind. Whether viewed on a desktop, tablet, or smartphone, users can enjoy an optimized layout and readability.

### Interaction Features

The page incorporates interactive elements, such as the ability to like a post, leave comments, and bookmark content. These features aim to foster community engagement and make the user experience more dynamic.

# Categories Page

![Screenshot of categories page](https://user-images.githubusercontent.com/129947589/284569392-fbe0997e-aa48-4838-aa19-ca2dbc9b0d56.png)

The All Categories page serves as a centralized hub where users can discover and explore the diverse range of topics covered on the blog. Here's a more detailed overview of the key features:

### Category Listing

The page prominently displays a list of all available categories, each clickable and leading to a dedicated page showcasing blog posts exclusively within that category. This ensures a streamlined and organized approach to content discovery.

### Category-Specific Navigation

Once a user clicks on a specific category, they are redirected to a dedicated page displaying all blog posts associated with that category. This page maintains consistent navigation options, allowing users to seamlessly switch between categories or return to the All Categories page.

### Responsive Design

Similar to other pages on the site, the Categories page is designed to be responsive, ensuring a visually appealing and user-friendly experience across various devices.

### Call to Explore

Conclude the description with a call to action, prompting users to dive into the categories that pique their interest. Encourage them to explore, engage, and discover the wealth of content available on CodeChef Creations.

In summary, the Categories Page is a gateway to a world of diverse topics, offering users an organized and visually engaging way to navigate through the blog's extensive content.

# Responsive Design

Ensuring a seamless viewing experience on a variety of devices is a top priority for my website. Employing a combination of Bootstrap and custom CSS code, I've implemented responsive design principles to enhance usability. Here's an overview of how the website adapts to different screen sizes:

### Media Queries

Media queries are instrumental in tailoring styles to accommodate diverse screen dimensions. Consider this example where the height of the .image-container is adjusted for screens with a maximum width of 767 pixels:

```css
@media screen and (max-width: 767px) {
    .image-container {
        max-height: 500px;
    }
}
```

By combining Bootstrap's responsive features with my custom media queries, the website delivers a visually appealing and user-friendly experience across a spectrum of devices.

### iPhone SE
Screenshots showcasing the blog on an iPhone SE:

![Screenshot of the blog on a iPhone SE](https://user-images.githubusercontent.com/129947589/284940345-b4967f0e-abc8-445a-9131-252166689a2b.png)
![Screenshot of the blog on a iPhone SE](https://user-images.githubusercontent.com/129947589/284940389-b5788543-5e0c-4d74-a371-888f5e222276.png)

### iPad Air
Screenshots showcasing the blog on an iPad Air:

![Screenshot of the blog on an iPad Air](https://user-images.githubusercontent.com/129947589/284940439-7bbe47a4-392e-43c9-bf41-bf2f67b4d819.png)
![Screenshot of the blog on an iPad Air](https://user-images.githubusercontent.com/129947589/284940679-1f5e3b10-6c99-4e47-bc50-350a7bb2a41e.png)

### Nest Hub Max
Screenshots showcasing the blog on a Nest Hub Max:

![Screenshot of the blog on a Nest Hub Max](https://user-images.githubusercontent.com/129947589/284940601-9017e4c8-80cf-428c-b3f9-ddae1a354d9f.png)
![Screenshot of the blog on a Nest Hub Max](https://user-images.githubusercontent.com/129947589/284940637-3c64bf1e-e75b-4e80-bf32-08c1afb2d562.png)

# Object-Based Software Concepts

### Category Model:
#### Usage of Categories in the Application:
The Category model is employed to organize and categorize blog posts. Each blog post can be assigned one or more categories, facilitating structured and easy navigation for users and aiding them in finding content of interest.

#### Specific Rules or Logic for Categories:
Currently, there are no specific rules or logic governing categories. They are primarily used as labels to organize content and enhance the user experience of the website.

### Post Model:
#### Handling and Display of featured_image in Views:
The featured_image field is part of the Post model and is used to store an image representing the blog post. In views, the selected image is displayed prominently in the blog post interface, contributing to making the post more visually appealing.

#### Special Requirements or Characteristics of the content Field:
The content field contains the textual content of the blog post. There are no specific requirements for the field, but it can include formatted text, links, and other media elements to make the content rich and engaging.

#### Purpose of the likes Relationship and How It Is Used:
The likes relationship is a Many-to-Many relation between users and blog posts. It is used to keep track of which users have liked a particular blog post. This enables features such as displaying the number of likes for a post and allowing users to express their interest in specific posts.

### Comment Model:
#### Handling and Display of Comments in the Application:
The Comment model is used to store user comments on a specific blog post. In the application, comments are displayed under each blog post, and users can engage in discussions by leaving their own comments.

#### Significance of the approved Field and How It Affects Comment Display:
The approved field is used to indicate whether a comment has been approved by the administrator to be displayed publicly. If approved is True, the comment is visible on the website. If it is False, the comment is not shown to other users until it has been approved by the administrator.

### SavedPost Model:
#### Purpose of the SavedPost Model and How It Is Used in the Application:
The SavedPost model is used to keep track of which posts a user has saved for future reference. Each post that a user saves is created as a new instance of SavedPost. This allows users to easily find and revisit their favorite posts without having to browse through the entire website.

# Admin Panel

![Screenshot of the admin panel](https://user-images.githubusercontent.com/129947589/284569448-e3897f60-51d2-43f5-bfca-b37d2d07f271.png)

The Admin Panel is a powerful tool for managing and overseeing various aspects of the website. Below is a brief overview of how the Admin Panel works on my website:

### Category

- **Name:** The name of the category.
- **Description:** A detailed description of the category.

### Post

- **Title:** The title of the blog post.
- **Slug:** A unique identifier for the post in the URL.
- **Categories:** Assign one or more categories to the post.
- **Author:** The author of the post.
- **Featured Image:** The main image associated with the post (using CloudinaryField).
- **Excerpt:** A brief summary or teaser of the post.
- **Content:** The main content of the post.
- **Status:** Draft or Published.
- **Likes:** Users who have liked the post.

### Comment

- **Post:** The post to which the comment belongs.
- **Name:** The name of the commenter.
- **Email:** The email address of the commenter.
- **Body:** The actual comment text.
- **Created On:** Date and time when the comment was created.
- **Approved:** Whether the comment has been approved for display.

### SavedPost

- **User:** The user who saved the post.
- **Post:** The post that has been saved by the user.

Admins can efficiently manage, create, edit, and delete instances of these models through the intuitive Django Admin Panel. This ensures smooth control and organization of the website's content and user interactions.

# Security

Ensuring the security of my application is a top priority, and I have implemented the following measures to safeguard sensitive information:

#### 1. Password Security

I securely store user passwords using industry-standard cryptographic hashing algorithms. Leveraging Django's built-in authentication system, passwords are hashed and verified.

#### 2. Key Management

Sensitive keys and credentials, such as API keys, are stored in environment variables and never hard-coded in the source code. This prevents accidental exposure of sensitive information in version control or public repositories.

#### 3. HTTPS Usage

My application enforces the use of HTTPS to encrypt data in transit, providing a secure connection between users and my server.

#### 4. User Permissions

I utilize Django's built-in permission system to control access to different parts of the application. Users are granted specific permissions based on their roles.

By implementing these security measures, I aim to provide a secure environment for my users and their data. If you have any security concerns or discover a potential vulnerability, please contact me immediately at **fridaholmlund@icloud.com** .

# Testing

For detailed information about testing, please read the [Testing Documentation](TESTING.md). The document contains test cases for the CodeChef Creations website, covering user authentication, blog post management, comments, likes, post categorization, saving posts, user interface and experience, as well as security aspects such as authentication security and protection against unauthorized access. The tests also include responsive design and easy navigation.

## Bugs

List of bugs and issues identified during development:

#### 1. Issue with Image Sizes

* **Description:** Images appear distorted and unattractive on smaller screen sizes, impacting the overall aesthetics of the website.
* **Steps to Reproduce:** Replicate the issue by viewing the website on devices with smaller screens and in Devtools.
* **Resolution:** Implemented media queries for responsive design and applied appropriate styles to ensure images adapt seamlessly to different screen sizes.
* **Expected Behavior:** Images should dynamically adjust based on screen size, transitioning from a three-in-a-row layout to two and finally a single column as the screen size decreases.
* **Actual Behavior:** Prior to the fix, images were not responsive, resulting in distortion and reduced visibility on smaller screens.
* **Status:** Closed.

#### 2. Issue with Icons on Smaller Screens

* **Description:** Icons for like, comment, and save actions appear distorted and clustered on smaller screen sizes, significantly impacting the overall visual appeal and usability of the website.
* **Steps to Reproduce:** Experience the issue by accessing the website on devices with smaller screens and in Devtools to simulate various screen sizes.
* **Resolution:** Implemented responsive design updates and adjusted styles in the CSS file to ensure icons display appropriately on all screen sizes.
* **Expected Behavior:** Icons should maintain clarity, proper spacing, and legibility, providing users with a visually pleasing and functional interface, regardless of the screen size.
* **Actual Behavior:** Prior to resolution, the icons failed to adapt effectively to smaller screens, resulting in clustering where icons overlapped, leading to a diminished user experience.
* **Status:** Closed.

#### 3. Issue with Save Icon State

* **Description:** The save functionality works as intended; however, there is an issue with the save icon state not updating as expected.
* **Steps to Reproduce:**
   1. Navigate to a post on the website.
   2. Click on the save icon to save the post.
   3. Observe the state of the save icon.
* **Expected Behavior:** The save icon should change to a filled state upon clicking, indicating that the post has been saved. The filled icon should persist as long as the user has the post saved.
* **Actual Behavior:** After clicking the save icon, the filled state is not consistently applied. Additionally, the filled state does not persist when navigating away from the post or upon refreshing the page.
* **Status:** Open.

# Solved Bugs

List of bugs that have been successfully resolved:

#### 1. Issue with Image Sizes

* **Description:** Images appeared distorted on smaller screen sizes.
* **Resolution:** Implemented media queries for responsive design.
* **Status:** Closed.

#### 2. Issue with Icons on Smaller Screens

* **Description:** Icons for like, comment, and save actions appeared distorted on smaller screen sizes.
* **Resolution:** Implemented responsive design updates and adjusted CSS styles.
* **Status:** Closed.

# Remaining Bugs

List of bugs that still need attention:

#### 1. Issue with Save Icon State

* **Description:** The save icon state does not consistently update as expected.
* **Steps to Reproduce:**
   1. Navigate to a post on the website.
   2. Click on the save icon to save the post.
   3. Observe the state of the save icon.
* **Expected Behavior:** The save icon should change to a filled state upon clicking, indicating that the post has been saved. The filled icon should persist as long as the user has the post saved.
* **Actual Behavior:** After clicking the save icon, the filled state is not consistently applied. Additionally, the filled state does not persist when navigating away from the post or upon refreshing the page.
* **Status:** Open.

# Validator Testing
While the website has undergone thorough testing and validation, there is an ongoing commitment to maintaining high standards. Continuous checks using tools such as Devtools Lighthouse and [WAVE](https://wave.webaim.org/report#/https://codechef-creations-aedba97ffd5b.herokuapp.com/) ensure that the website remains accessible, performant, and compliant with web standards.

![Screenshot of lighthouse testing](https://user-images.githubusercontent.com/129947589/285160333-aec670c7-4601-4771-9226-623a999982c9.png)

### HTML

- During the validation process with the official W3C validator, reported errors were related to missing `alt` attributes for the images. Initially, I consciously chose not to address this issue due to the unique rendering process involving Django code, making it challenging to assign specific `alt` attributes to the images.

After conducting further research, I've successfully implemented `alt` attributes for Django-rendered images, resolving the reported problem. As a result, there are no longer any errors returned from the validator testing.

```html
<img class="post-card-img-top" src="{{ post.featured_image.url }}" alt="{{ post.title }} Featured Image" width="100%">
```
This adjustment ensures that each image now has a descriptive alt attribute, contributing to improved accessibility.

For detailed validation results, you can review the [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcodechef-creations-aedba97ffd5b.herokuapp.com%2F).

### CSS

- No errors were returned from the official CSS validator[(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcodechef-creations-aedba97ffd5b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### Python & Django

Python, in conjunction with the Django web framework, is at the core of CodeChef Creations' backend development. The project harnesses the power of Python and Django to build a robust and scalable web application.

#### Key Components

#### 1. Django Models, Views, Controllers, Forms, and Templates

Django models define the database structure, while views and controllers handle user interactions and logic. Forms simplify user input validation, and templates enable dynamic HTML content generation with embedded Python code.

#### 2. Testing

A suite of Python tests ensures the correctness of functionalities, covering models, user authentication, comments, likes, post categorization, saving posts, responsive design, and overall user interface and experience.

#### 3. Features

Django's rich feature set enhances CodeChef Creations:

* **Model-View-Controller (MVC) Architecture:** Django adopts the MVC architecture through its Model-View-Template (MVT) pattern.
  
* **Object-Relational Mapping (ORM):** Django's ORM simplifies database interactions, minimizing the need for raw SQL queries.

* **Django Admin Panel:** The built-in Admin Panel provides a powerful interface for efficient management of categories, posts, comments, and other entities.

* **User Authentication:** Django's user authentication system is utilized for user registration, login, and other authentication-related functionalities.

* **Forms and Templates:** Django's forms and templates simplify the handling of user input and dynamic content generation.

* **Testing with Django:** The Django testing framework facilitates the creation of comprehensive tests, ensuring a well-structured and maintainable codebase.

With Python and Django, CodeChef Creations delivers a feature-rich blogging platform for the CodeChef community.

# Deployment

CodeChef Creations is deployed using Code Institute's terminal for Heroku, ensuring a smooth and accessible experience for users.

**Steps for deployment:**

1. Create a new external database on ElephantSQL.
2. Create the Heroku app.
3. Attach the database.
4. Prepare our environment and settings.py file.
5. Get our static and media files stored on Cloudinary.

# Technologies Used

This project leverages a range of technologies to deliver its functionality:

* **Django**: A high-level Python web framework that facilitates rapid development and clean, pragmatic design. In this project, Django serves as the backbone for handling backend logic, routing, and database interactions.

* **Django Libraries**:
  * `gunicorn`: A WSGI HTTP server for deploying Django applications.
  * `psycopg`: A PostgreSQL adapter for Python.
  * `crispy-forms`: A Django package that helps with rendering elegant and consistent HTML forms. It enables easy styling and layout customization for forms in Django projects.

* **Cloudinary**: An image and video management service that enhances media handling in web applications. Cloudinary is seamlessly integrated into this project to efficiently manage and serve images, ensuring a seamless user experience.

* **ElephantSQL**: A PostgreSQL-as-a-Service provider used for hosting the external database.

# Content

Throughout the development of this webpage, I drew inspiration and guidance from various sources to enhance my skills and create a robust blogging platform. Here are some key resources that played a pivotal role:

1. [Code Institute](https://codeinstitute.net/): Code Institute provided a structured learning path with comprehensive video content and course materials. The lessons on Full Stack Farmeworks greatly aided in implementing the website.

2. [W3Schools](https://www.w3schools.com/): W3Schools served as a valuable reference for mastering HTML, CSS, JavaScript, Python, Django and Bootstrap. I particularly found their explanations on Django to be clear and practical when working on this project.

3. [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/): Bootstrap's official documentation was instrumental in creating a responsive and visually appealing design.

4. [Django Documentation](https://docs.djangoproject.com/en/4.2/): Django's documentation proved indispensable for building the backend of the blog. The sections on [authentication](https://docs.djangoproject.com/en/4.2/topics/auth/) and [models](https://docs.djangoproject.com/en/4.2/topics/db/models/) offered valuable insights that directly influenced the structure of the website.

5. [Real Python](https://realpython.com/): Real Python's articles provided in-depth explanations on [specific topic], which greatly contributed to the efficiency and readability of the codebase. The practical examples were particularly helpful in implementing this website.

6. [Django GitHub Repository](https://github.com/django/django): Exploring Django's GitHub repository offered a deep dive into the framework's source code. This not only provided inspiration but also guided decisions when working on this project.

# Media
The aesthetic elements of this website are enriched by resources from the following:

**Icons:** All icons featured on the website are sourced from [Font Awesome](https://fontawesome.com/), contributing to a visually appealing and consistent design.

**Images:** The visual content on the website is curated from [Pexels](https://www.pexels.com/), ensuring high-quality and captivating visuals that enhance the overall user experience.

**Recipes:**
The collection of recipes showcased on this platform originates from reputable culinary sources, namely [Köket.se](https://www.koket.se/), [Arla.se](https://www.arla.se/), [Ica.se](https://www.ica.se/recept/), and [Coop.se](https://www.coop.se/recept/). To make these recipes accessible to a broader audience, they have undergone a process of translation from Swedish to English. Additionally, an AI-driven adaptation ensures that they align seamlessly with the platform's distinctive code style.

(Note: Recipes and images are unrelated)