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
i)	git clone https://github.com/Nteka10/NTSOEKHE-DDBMS-SYSTEM-DESIGN
ii)	Download the zip file of our scripts on the green “<> code” icon.
iii)	Unzip the folder, and open it in MS Visual Studio code.

2) set up virsual environment and working directories
i) Install sqlite viewer for easy view of database.db
  -NB: The database(database.db) already has a patient table created.
ii) Create python environment (.venv) inside the working directory (Ntsoekhe-Image) using
    the latest python version installed on your local host.
iii) Open the terminal (Terminal: Create New Terminal) and install flask using the command (python -m pip install flask) inside the virtual environmet create above.
NB: Simply click on database.db to navigate the database and inspects its table elements.

3) Open new terminal to build image and container using the shortcut (Ctrl + Shift + ') in MIcrosoft Visual Studio Code, or simple open the terminal of your IDLE

4) Change working directory using the command (cd Ntsoekhe-image) 

5)	Build the Docker image:
i)	docker image build -t patients .  (NB: the period is part of the command)

6)	Define docker ports and host ports,run the image inside the container: 
i) docker run -p 5000:5000 --name north patients(NB: "north" represents the container name and "patients" represent the image name)  

7)	Navigate to docker: 
i)	Run the container, copy the URL link that appears.

8)	Open Web Browser:
i)      Paste the url and run it, the user interface will pop up.

9)	Navigate the user interface:
i)      Apply CRUD functionalities on the interface so  as to manipulate the database.



