# TendCheck

Goals and Requirements of the Application:
Goal: To create a browser-based application that assists in preparing proposals for participants in government procurements, in accordance with the requirements of the customer and the law.
Requirements:

Functionality for analyzing customer documentation
Functionality for preparing template documents
Functionality for generating a final folder for proposal submissions
Design and Architecture:
Development of the overall application architecture.
Functionality of the Home Page and Navigation:
Creation of the application's main page with descriptions and information about the application.
Creation of a navigation menu.
Creation of page designs for the application.
Functionality of the Personal Account:
Development of user registration and authentication functionality to create a personal account.
Creation of a form for receiving company data from the client.
Implementation of the ability to fill out customer forms with information from a template.
Implementation of a repository for statutory documents.
Document Management:
Development of a mechanism for receiving text documentation.
Development of a mechanism for parsing text by keywords.
Creation of functionality for categorizing documents into one-time and permanent categories (references and documents).
Implementation of a feature to list all necessary documents.
Implementation of generating references from one-time categories using templates.
Implementation of creating a general archive with proposal documents and recommendations.
Implementation of functionality for selecting similar contracts based on the subject of procurement.
Testing and Debugging:
Conducting functionality testing to ensure compliance with requirements and debugging errors.
Adjusting and correcting functionality based on feedback from users and testers.
Release and Support:
Preparing the application for release.
Deploying the application on a server and launching it.
Ongoing application support after release, responding to user feedback, and developing updates.








!!!!!


To launch the application, follow these steps:
Clone the repository:
Open the terminal (command line) on your computer and execute the git clone command with the repository URL:те терминал (командную строку) на вашем компьютере и выполните команду git clone с URL-адресом репозитория:
git clone "repository URL"

Navigate to the project directory:
Move to the directory that was created after cloning the repository:

cd "folder name"

Start the server:
Launch the Django development web server using the command:

python manage.py runserver 
or
python3 manage.py runserver

After this, the application will be available at http://127.0.0.1:8000/ in your browser.
