# CodeChef Creations

Welcome to CodeChef Creations! This Django-based blogging website offers a unique blend of programming and culinary delights. Explore posts and recipes curated by the **CodeChef** community. Our blog is designed for coding enthusiasts who seek to maintain a healthy lifestyle while spending long hours in front of their screens. The recipes are not only delicious but also infused with programming references and style, making them a delightful read for those familiar with coding.

![Screenshot of the website on different screen sizes]()

## Getting Started

Using CodeChef Creations is a breeze! While an account is not mandatory for browsing, creating one allows you to engage with the community, leave comments, save posts, and like posts.

### Steps to get started

1. Navigate to the CodeChef Creations website.
2. Browse through the diverse range of available posts.
3. Click on any post that piques your interest to delve deeper into its contents.
4. To actively engage with the community, sign up for an account and unlock the ability to leave comments, save posts, and like posts.
5. Explore specific interests by navigating through categories such as Healthy Salads to find posts that align with your preferences.

## Features

* **No login required for browsing:** Explore posts without the need for an account.
* **User authentication system:** Engage with the community by leaving comments and liking posts.
* **Categories menu:** Filter posts by relevant topics and interests, making it easy to find content that suits your preferences.

### Navigation

* At the top of the page, you'll find the blog's name: CodeChef Creations. Clicking it redirects you to the homepage.
* On the right side of the logo, you have navigation links to the Homepage, All Categories, Register, and Login. If you're logged in, additional links include Saved Posts and Logout.
* The navigation employs a clean and modern font, with a color that contrasts the background.
* Clear navigation guides users to easily find what they are looking for.

## User Guide

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

### Saving Posts

To save posts, follow these steps:

1. Navigate to the post you want to save.
2. Scroll to the end of the blog post.
3. Click the bookmark icon to save the blog post for later.
4. Access all your saved posts by clicking the **Saved Posts** link in the navbar.
5. To unsave a blog post, click the bookmark icon again.

### Liking Posts

To like posts, follow these steps:

1. Navigate to the blog post you want to like.
2. Scroll to the end of the blog post.
3. Click the heart icon to like the post.
4. The heart icon will turn red, indicating your like.
5. The like count will increase with each like.

## Post Detail Page

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

## Categories Page

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

## Testing

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

## Solved Bugs

List of bugs that have been successfully resolved:

#### 1. Issue with Image Sizes

* **Description:** Images appeared distorted on smaller screen sizes.
* **Resolution:** Implemented media queries for responsive design.
* **Status:** Closed.

#### 2. Issue with Icons on Smaller Screens

* **Description:** Icons for like, comment, and save actions appeared distorted on smaller screen sizes.
* **Resolution:** Implemented responsive design updates and adjusted CSS styles.
* **Status:** Closed.

## Remaining Bugs

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

## Validator Testing

[WAVE](https://wave.webaim.org/report#/https://codechef-creations-aedba97ffd5b.herokuapp.com/)

### HTML
[W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcodechef-creations-aedba97ffd5b.herokuapp.com%2F)

### CSS
[(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcodechef-creations-aedba97ffd5b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)


## Deployment

CodeChef Creations is deployed using Code Institute's terminal for Heroku, ensuring a smooth and accessible experience for users.

* **Steps for deployment:**
  1. Fork or clone this repository.
  2. Create a new Heroku app.
  3. Link the Heroku app to the repository.
  4. Click on **Deploy** to make your app live.

## Credits
