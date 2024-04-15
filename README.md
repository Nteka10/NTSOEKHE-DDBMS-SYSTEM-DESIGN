This is a repository for a project in CS4430 Distributed Database Management Systems. Involved parties: Mapulane Nteka, Mahase Kuena, 
Morapeli Makhosane, Putsoa Bokang and Khalala Morapeli.
(Instructor): Mr Khobatha Setetemela

Introduction
This project is a Distributed Database Management System (DBMS) called NTSOEKHE, built using Python, Flask, SQLite, and Docker Desktop. 
It provides a web-based CRUD (Create, Read, Update, Delete) interface for managing patient records stored in an SQLite database.
Features
•	CRUD Interface: The application offers a user-friendly interface for creating, reading, updating, and deleting patient records.
•	Flask Web Server: The backend is powered by Flask, a lightweight web framework for Python, providing robust and scalable web services.
•	SQLite Database: Patient records are stored in an SQLite database, which is a lightweight and serverless database engine.
•	Dockerized: The application is containerized using Docker Desktop, enabling easy deployment and portability across different environments.
•	Distributed Architecture: While the current implementation uses SQLite, the architecture is designed to support distributed databases in the future.


Setup Instructions
Prerequisites
•	Install Python (version 3.6 or higher).
•	Install Docker Desktop
•	Install Microsoft Visual Studio Code
INSTALLATIONS
1)	Clone this repository to your local machine:
i)	git clone https://github.com//distributed-dbms.git
ii) Download the README file for use instructions.
iii)	Download the zip file of our scripts on the green “<> code” tab.
iv)	Unzip the folder, and open it in MS Visual Studio code.

3)	Change working directory to Ntsoekhe-image in the terminal.
i)      cd Ntsoekhe-image

4)	Build the Docker image:
i)	docker image build -t patients .  (NB: the period is part of the command)

5)	Define docker ports and host ports, run the image inside the container:
i)	


6)	Navigate to docker: 
i)	Run the container, copy the URL link that appears.

7)	Open Web Browser:
i)      Paste the url and run it, the user interface will pop up.

8)	Navigate the user interface:
i)      Apply CRUD functionalities on the interface so  as to manipulate the database.



