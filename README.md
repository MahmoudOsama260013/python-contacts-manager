Python Contacts Manager
A simple command-line contact management application built with Python.
The program allows users to add, search, delete, and display contacts directly from the terminal. It also supports fuzzy name searching using Python's built-in difflib module.
Features
* Add a new contact
* Add multiple phone numbers for the same contact
* Categorize contacts as:
o Family
o Personal
o Work
o Other
* Search for contacts by name
* Fuzzy name matching for similar names
* Search for contacts by phone number
* Delete contacts by name
* Delete contacts by phone number
* Display all saved contacts
* Prevent duplicate phone numbers
* Basic input validation
Technologies Used
* Python
* Python Standard Library
* difflib
How It Works
The application stores contact information using three lists:
* list_Name stores contact names
* list_Num stores phone numbers
* list_Type stores contact categories
The corresponding positions in the three lists represent one contact record.
For example:
Name: Mahmoud
Number: 0591234567
Type: Personal
Fuzzy Search
The project uses Python's difflib.get_close_matches() function when searching by name.
This means that if the user enters a name that is slightly different from a stored contact name, the program can still suggest matching contacts.
Running the Project
Make sure Python is installed on your computer.
Clone the repository:
git clone https://github.com/MahmoudOsama260013/python-contacts-manager.git
Move into the project directory:
cd python-contacts-manager
Run the program:
python Mahmoud_120255986.py
Example Menu
Welcome to our Address book, please to find what you want

1. Add new contact.
2. Search by name.
3. Search by number.
4. Delete contact by name.
5. Delete contact by number.
6. Show all contacts.
7. Exit
What I Learned
Through this project, I practiced:
* Python functions
* Lists and data manipulation
* Loops
* Conditional statements
* User input validation
* Searching and deleting data
* Handling duplicate values
* Using Python standard-library modules
* Building a menu-driven command-line application
Future Improvements
Possible improvements include:
* Store contacts permanently using JSON, CSV, or a database
* Replace parallel lists with classes or dictionaries
* Add contact editing
* Improve phone-number validation
* Improve duplicate-number handling
* Add automated tests
* Build a graphical user interface
Author
Mahmoud Osama

