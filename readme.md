# Django Blog Application

This project is a feature-rich Django blog application that allows users to create and share their posts, browse articles, and interact with the content. Below are the steps to set up the application and some of its notable features.

## Features

This Django blog application comes with the following features:

-   User Authentication: Users can sign up, log in, and manage their profiles.
-   CRUD Functionality: Users can create, read, update, and delete their own posts.
-   Post Categories: Posts can be categorized for easy navigation and filtering.
-   Search Functionality: Users can search for specific posts using keywords.
-   Pagination: The post list view is paginated for better user experience.
-   Email Sharing: Users can share posts via email using Django forms.
-   Comments: Registered users can leave comments on posts.
-   Tags: Posts can be tagged using django-taggit.
-   Recommended Posts: A recommendation system suggests similar posts based on user preferences.
-   Custom Template Tags and Filters: Displays the latest posts and most commented posts in the sidebar.
-   Sitemap and RSS Feed: The application generates a sitemap and RSS feed for better SEO and syndication.

## PostgreSQL Support

The application supports PostgreSQL for improved performance and full-text search capabilities.


## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python: Make sure Python is installed on your system.
- Virtual Environment: Set up a Python virtual environment to manage dependencies.
- Django: Install Django in the virtual environment.

### Installation

1. Clone this repository to your local machine:

```bash 
git clone https://github.com/your-username/Django-Blog-App.git
```

2.  Create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```

3. Install Django and other required packages:
``pip install -r requirements.txt``

4.  Set up the database and perform initial migrations:
``python manage.py migrate``

5. Create a superuser to access the admin panel:
``python manage.py createsuperuser``

6. Run the development server:
``python manage.py runserver``

7. Open your browser and go to:
``http://localhost:8000/``



## Contributing

If you have any feedback, suggestions, or would like to contribute, please create a new issue or submit a pull request.

### Thanks
