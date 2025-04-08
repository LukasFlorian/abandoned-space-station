# Abandoned Space Station

This is the abondoned space station game, in which the player will explore a space station, trying to discover all safe areas while avoiding the dangers lurking in the dark.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Make sure to have Python 3.13.1 or higher installed on your machine.

Then navigate into the project's root directory and run the following command to install the required dependencies:

~~~
pip install -r requirements.txt
~~~

## Running the Game

To run the game, navigate into the project's root directory and run the following command:
~~~
python source/main.py
~~~

## Running the Tests

To run the tests, navigate into the project's root directory and run the following command:
~~~
python -m unittest discover -s tests
~~~

Or, in order to run coverage tests, run the following command:
~~~
coverage run tests
coverage html
~~~

And then open the `htmlcov/index.html` file in your browser to view the coverage report.