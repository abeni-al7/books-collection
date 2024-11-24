# Book Collections

Book Collections is a Django-based web application that allows users to manage their personal book collections. Users can add, view, update, and delete books, as well as receive book recommendations.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add Books**: Create new book entries with details like title, author, ISBN, and published year.
- **View Books**: Retrieve a list of all books in the collection.
- **Update Books**: Edit existing book details.
- **Delete Books**: Remove books from the collection.
- **Book Recommendations**: Get random book recommendations from your collection.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python package installer. It typically comes with Python.
- **Git**: For version control. Download from [git-scm.com](https://git-scm.com/).
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

## Installation

Follow these steps to set up and run the Book Collections application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-collections.git
cd book-collections
```

### 2. Create a Virtual Environment

```bash
python3 -m venv env
```

### 3. Activate the Virtual Environment

```bash
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 5. Set Up Environment Variables
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Run the app
```bash
python manage.py runserver
```
