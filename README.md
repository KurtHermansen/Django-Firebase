# Overview

Welcome to our Django website that includes a login/signup prompt, contact page, and about page, with stylish design using TailwindCSS. This website is designed to provide a simple and easy-to-use platform for users to create accounts, log in, and contact the website administrator. The website's sleek and modern design is achieved through the use of the popular TailwindCSS framework, which allows for easy customization of the website's appearance.

Our website aims to provide a seamless user experience, with a user-friendly interface and intuitive navigation. Users can easily create an account, log in, and access the website's features, such as the contact and about pages. The contact page allows users to send messages to the website administrator, while the about page provides information about the website and its purpose.

To enhance the functionality of our Django website, we have integrated it with Firebase and Firestore cloud database. Firebase provides a comprehensive suite of backend services, including authentication, real-time database, cloud storage, and more. Firestore is a NoSQL document database offered by Firebase, which allows us to store and sync data in real-time.


[Django Website Demo Video](https://youtu.be/PzsN6X8f1xA)


# Cloud Database

To enhance the functionality of our Django website, we have integrated it with Firebase and Firestore cloud database. Firebase provides a comprehensive suite of backend services, including authentication, real-time database, cloud storage, and more. Firestore is a NoSQL document database offered by Firebase, which allows us to store and sync data in real-time.

When information is submitted Firestore automatically creates a collection and build it to the specifications give by the json model. In this case two collections are created 
* Messages
The form given has inputs for a name, email, and message. This is then POSTED to the Firestore cloud database in real time. 
* Users
The form given has inputs for a First name, Last name, Email, and Password. . This is then POSTED to the Firestore cloud database in real time. 


# Web Pages

Features
This Django website includes the following features:

* Signup
The website includes signup prompt. Users can create an account by entering their name, email address, and password. Once the data is saved it will be stored in Firestore a Google Cloud database. This is updated in real time. 

* Contact Page
The website includes a contact page where users can submit a form with their name, email address, and message. When the user submits the form, the message will be sent to the Firestore Google Cloud database.

* Messages
The website includes a message page where all the messages submitted can be viewed. 

* Users
The website includes a message page where all the messages submitted can be viewed. 

# Development Environment

* Visual Studio Code
* Python 3.9.7 64-bit
* Git / Github
* Django
* Tailwind CSS

# Useful Websites

* [Visual Studio](https://code.visualstudio.com/)
* [Python Documentation](https://docs.python.org/3/library/index.html)
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)
* [Tailwind CSS](https://tailwindcss.com/)
* [FreeCodeCamp.org (YouTube Tutorial)](https://www.youtube.com/watch?v=ZxMB6Njs3ck)



# Future Work

* Database Linking
* Authentication
* Sessions for Login users