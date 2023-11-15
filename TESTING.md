# Test Cases for CodeChef Creations

## User Authentication

### Log In

**Test Case:** Verify that users can successfully log in.
**Preconditions:** Users have valid usernames and passwords.
**Steps to Perform:**

1. Visit the login page.
2. Enter a valid username and password.
3. Click the "Log In" button.
**Expected Result:** The user logs in and is redirected to the home page.

### Register New User

**Test Case:** Ensure that new users can register for an account.
**Preconditions:** The user does not have an existing account.
**Steps to Perform:**

1. Visit the registration page.
2. Provide valid registration details.
3. Click the "Register" button.
**Expected Result:** The user's account is created, and they are redirected to the login page.

## Blog Posts

### Create a New Blog Post

**Test Case:** Confirm that administrators can create new blog posts.
**Preconditions:** The administartor is logged in.
**Steps to Perform:**

1. Navigate to the "Admin" panel.
2. Enter the required details for the new post.
3. Click the "Publish" button.
**Expected Result:** The new blog post is created and visible on the blog.

### Edit an Existing Blog Post

**Test Case:** Verify that administrators can edit their existing blog posts.
**Preconditions:** The administrator has one or more published blog posts.
**Steps to Perform:**

1. Open the "Admin" panel and select post.
2. Modify the content or details.
3. Save the changes.
**Expected Result:** The changes are applied, and the updated post is visible.

### Delete a Blog Post

**Test Case:** Ensure that administrators can delete their own blog posts.
**Preconditions:** The administrator has one or more published blog posts.
**Steps to Perform:**

1. Open the "Admin" page and select a post.
2. Confirm the deletion.
**Expected Result:** The post is deleted and no longer appears on the blog.

## Comments

### Add a Comment

**Test Case:** Test the ability to add comments to blog posts.
**Preconditions:** The user is logged in.
**Steps to Perform:**

1. Navigate to a blog post.
2. Enter a comment in the comment section.
3. Click the "Submit" button.
**Expected Result:** The comment is avaiting approval and visible on the blog post when approved.

## Like Posts

### Like a Blog Post

**Test Case:** Verify that users can like a blog post.
**Preconditions:** The user is logged in.
**Steps to Perform:**

1. Open a blog post.
2. Click the "Like" button.
**Expected Result:** The post is liked, and the like count is incremented. The user can see a visual indicator that the post has been liked in form of a red heart.

### Unlike a Liked Blog Post

**Test Case:** Verify that users can unlike a previously liked blog post.
**Preconditions:** The user is logged in, and there is at least one blog post the user has already liked.
**Steps to Perform:**

1. Open a blog post that the user has previously liked.
2. Click the red heart again.
**Expected Result:** The post is unliked, and the like count is decremented. The visual indicator for liking is removed.

## Categorizing Posts

### Create a New Category

**Test Case:** Verify that administrators can create new categories.
**Preconditions:** The administrator is logged in.
**Steps to Perform:**

1. Go to the "Admin" panel.
2. Navigate to "Categories."
3. Create a new category with valid information.
4. Click "Save."
**Expected Result:** The new category is created and available to associate with blog posts.

### Associate a Category with a Blog Post

**Test Case:** Verify that administrators can associate a category with a blog post.
**Preconditions:** The administrator is logged in, and there is at least one existing category.
**Steps to Perform:**

1. Open the "Admin" panel and select a blog post.
2. Choose or add a new category for the post.
3. Save the changes.
**Expected Result:** The category is associated with the blog post and displayed correctly on the user interface.

### Filter Blog Posts by Category

**Test Case:** Verify that users can filter blog posts by a specific category.
**Preconditions:** There is at least one blog post associated with a category.
**Steps to Perform:**

1. Visit the "All Categories" page.
2. Select a category from the categories list.
**Expected Result:** Only blog posts associated with the selected category are displayed.

## Save Posts

### Save a Blog Post

**Test Case:** Verify that users can save a blog post for later.
**Preconditions:** The user is logged in.
**Steps to Perform:**

1. Open a blog post.
2. Click the "save" button.
**Expected Result:** The post is saved in the "Saved Posts" page and is available for future reference.

### View Saved Posts

**Test Case:** Verify that users can see their saved posts.
**Preconditions:** The user has at least one saved post.
**Steps to Perform:**

1. Visit the "Saved Posts" page.
**Expected Result:** A list of the user's saved posts is displayed correctly.

### Remove a Saved Post

**Test Case:** Verify that users can remove a saved post from the saved posts list.
**Preconditions:** The user has at least one saved post.
**Steps to Perform:**

1. Visit the "Saved Posts" page.
2. Remove a saved post from the list buy clicking the "save" button.
**Expected Result:** The saved post is removed from the list and is no longer available on the "Saved Posts" page.

## User Interface and User Experience

### Responsive Design

**Test Case:** Ensure that the website is responsive across various devices.
**Preconditions:** Access the website from different devices (desktop, tablet, mobile).
**Steps to Perform:**

1. Open the website on a desktop.
2. Open the website on a tablet.
3. Open the website on a mobile phone.
**Expected Result:** The website displays correctly and is user-friendly on all devices.

### Navigation

**Test Case:** Verify that users can easily navigate between different sections of the website.
**Preconditions:** The user is logged in.
**Steps to Perform:**

1. Explore various sections such as home, categorys, saved posts, etc.
2. Click on navigation links and buttons.
**Expected Result:** Navigation is intuitive, and users can quickly access different parts of the website.

## Security

### Authentication Security

**Test Case:** Ensure the security of the authentication process.
**Preconditions:** Users attempt to log in with valid and invalid credentials.
**Steps to Perform:**

1. Attempt to log in with valid credentials.
2. Attempt to log in with invalid credentials.
**Expected Result:** Users with valid credentials can log in, and users with invalid credentials receive appropriate error messages.

### Protection Against Unauthorized Access

**Test Case:** Confirm that unauthorized users cannot perform certain actions.
**Preconditions:** Attempt to access or modify content without appropriate permissions.
**Steps to Perform:**

1. Try to like, comment or save a post without the necessary permissions.
2. Attempt to access the admin panel without admin privileges.
**Expected Result:** Unauthorized actions are prevented, and appropriate error messages are displayed.
