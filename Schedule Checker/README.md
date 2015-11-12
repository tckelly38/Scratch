# Schedule Checker
This python script is meant as a notification tool for FSU class schedules. It is by no means meant 
for any malicious purposes.

There are a couple dependencies needed to make this all work properly, I will assume the user has python and pip
installed on their machine.

Run the followoing commands from the command line (assuming your path variables are correctly set)

`pip install selenium`

and

`pip install time`

and 

`pip install smtplib`

as well as

`pip install beautifulsoup4`


After setting up the appropriate dependencies, copy the code from navigateToPage.py over to your notepad and then fill in the 
variables at the top with your data.


Run the navigateToPage.py by issuing the command:

`python navigateToPage`

And that's it! Leave this guy running in the background and you will be notified via email when your class is available

List of assumptions:

* python and pip installed

* selenium, time, smtplib, and beautifulsoup4 installed

* firefox installed(can switch to driver of your choice if you so desire)

* have valid credentials

* have gmail account
