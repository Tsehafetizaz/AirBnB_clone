#AirBnB Clone version 2  Project

## Description

This project is a simplified clone of AirBnB. It includes a command interpreter for managing the application's data, allowing the creation, modification, and deletion of instances of various classes related to AirBnB, such as users, places, states, cities, amenities, and reviews.

## Command Interpreter

The command interpreter, also known as the console, is a command-line tool that provides a simple interface to manage the data of this project.

### Starting the Command Interpreter

To start the command interpreter, navigate to the project directory and run the file `console.py`:

```bash
./console.py

Using the Command Interpreter
Once the command interpreter starts, you can use the following commands:

create: Creates a new instance of a given class.
show: Shows an instance of a given class and id.
destroy: Deletes an instance based on the class name and id.
all: Displays all instances of a given class, or all classes if none is specified.
update: Updates an instance based on the class name and id by adding or updating an attribute.
Command Examples
Creating a new User:
(hbnb) create User
Showing a User instance:
(hbnb) show User user_id
Deleting a User instance:
(hbnb) destroy User user_id
Listing all User instances:
(hbnb) all User
Updating a User instance:
(hbnb) update User user_id email "user@example.com"
Exiting the Command Interpreter
You can exit the command interpreter by typing quit or by using the EOF signal (Ctrl-D).
