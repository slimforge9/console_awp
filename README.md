____________________________________
THIS IS MY FIRST README
____________________________________

AWP - Apka Wsparcia Patrolowca
(eng. patroller support app)

This project supposed to solve the problems I've faced while working as a police officer in Gliwice, Poland.
Becouse of bad organisation in Polish Police me and other police officers many times had problems with collecting 
actual annexes of legal acts (which are forms that have to be filled when arresting someone)

This project solved this problems:
	- current legal acts and their's annexes
	- all in one place
	- data inputes only once - same data copied on different forms that have same fields to be completed
	- reduced time spent on filing all forms one by one
	
I have used python programming language to create this console-based appplication (this project was my first one
to learn programming skills). Also had to use libraries like:
	- FPDF2
	- PyPDF2
	
In this project you chose a forms that you need to fill, then start filing the information fields which
are required in those forms. When information is completed, application create just one PDF file including
merged forms you have chosen from menu.

For example in menu you chose "Kreator" then "Stwierdzenie tożsamości" (list of chosen forms should be listed in yellow
color) and hit enter, and application starts to collect information that is needed in forms it gonna fill.
After complete application creates one PDF file in localization specified in console prompt.

This project is my first project, and it's going to be updated with more forms and Graphical User Interface
with PyQT6 Library - i have plans to monetize this project
