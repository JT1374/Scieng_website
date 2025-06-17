# Scieng Website

`SciEng Website` is a Django web app for a science and engineering organization. It allows the site owners to showcase projects, provides user authentication and allows the users to view the news on projects announced. Similar to a blog web app.

---

## Table of Contents

1. [Features](#features)
2. [How to Install](#how-to-install)
3. [Usage](#usage)
4. [License](#license)
5. [Contact](#contact)
6. [Images](#images)
7. [Screenshots of Project](#screenshots-of-project)
8. [Credits](#credits)

---

## Features!

- **Home Page**: Introduces the organization.
- **Projects**: Displays a list of projects with details and has images to showcase 
                the projects.
- **User Authentication**: Allows users to sign up, log in, and log out.
- **Responsive Design**: Works on both desktop and mobile devices.

---

## How to Install?

1. **Clone the Project**:
   ```bash
   git clone https://github.com/JT1374/Scieng_website.git
   cd Scieng_website
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For Unix-based systems
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   cd scieng_website
   python manage.py migrate
   ```

5. **Run the App**:
   ```bash
   python manage.py runserver
   ```

6. **Open in Your Browser**:
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t jt1374/scieng_website:latest .
   ```

2. **Run the Docker container**
   ```bash
   docker run -p 80:80 jt1374/scieng_website:latest
   ```

3. **Access the app**
   Open your browser and go to [http://localhost:80](http://localhost:80)

---


## Usage

1. Navigate to the home page to learn about the organization.
2. Explore the **Projects** section to view detailed project information.
3. Use the **Sign Up** or **Log In** options to create an account or access additional features.

### Screenshots

<p text-align="center">
   <img src="screenshots3/Screenshot 1.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 2.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 3.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 4.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 5.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 6.png" width="400px" height="400px" alt="image of project"/>
</p>

---

## Documentation From Sphinx

- Project documentation can be found in the `docs` directory.
- It was made using sphinx.

---

## License

Has no licence.

---

## Contact

Questions or feedback? Email me at [barnesjulian368@gmail.com].

---

## Images

The images in this project are not mine and are for placeholder purposes only.

---

## Credits

This project was created by Julian Barnes.
