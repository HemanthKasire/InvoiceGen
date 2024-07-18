-Better use a Virtual Environment 
-Install the Softwares from requirements.txt 
-Make sure you have all the files and you are at the present working directory 
-Run the Server
    python manage.py runserver

//For Admin Page and Controls of the page
To be able to log into the admin application, we need to create a user. This is done by typing this command in the command view:
                      python manage.py create superuser
Which will give this prompt:
Username:
Here you must enter: username, e-mail address, (you can just pick a fake e-mail address), and password:


start the server again:
                      python manage.py runserver
In the browser window, type localhost:8000/admin/ in the address bar, and fill in the form with the correct username and password:
