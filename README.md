Digital Footprint Calculation System
Overview

This project is a simple Python-based Digital Footprint Calculation System.
It calculates a user's digital footprint score based on:

Number of social media platforms used
Daily internet usage time
Weekly sharing/post count

The program then determines the user's risk level as:

Low Risk
Medium Risk
High Risk

All user data is also saved into a text file named dijital_ayak_izi.txt.

Features
User-friendly console interaction
Calculates digital footprint score
Determines risk level automatically
Supports multiple users
Saves user information to a file
Error handling with try-except
Technologies Used
Python 3
How the Score is Calculated

The score formula:

puan = (sosyal_medya * 20) + (gunluk_saat * 5) + (paylasim_sayisi * 2)
Risk Levels
Score Range	Risk Level
Less than 50	Low Risk
50 - 99	Medium Risk
100 and above	High Risk
Example Usage
Digital footprint calculation system

your name: John

Enter the number of platforms you use

Platforms: ('Instagram', 'TikTok', 'Twitter', 'Facebook')

How many social media platforms do you use?: 3
How many hours do you spend online daily?: 5
Weekly number of posts: 10

Result:

Digital Footprint Score: 95
Risk Level: Medium Risk
File Saving

User data is automatically saved into:

dijital_ayak_izi.txt

Example saved data:

{'ad': 'John', 'platform sayisi': 3, 'gunluk saat': 5.0, 'paylasim sayisi': 10, 'puan': 95, 'risk': 'Orta Risk'}
Error Handling

The program handles:

Invalid numeric inputs
Unexpected runtime errors

Example:

ERROR: Please enter numeric values!
How to Run
Install Python 3
Save the code as:
digital_footprint.py
Run the program:
python digital_footprint.py
Future Improvements
Add graphical user interface (GUI)
Store data in a database
Add data visualization charts
Improve scoring algorithm
Support more social media platforms
Author

Developed as a beginner-level Python project for practicing:

Functions
Loops
Exception handling
File operations
Dictionaries and lists
