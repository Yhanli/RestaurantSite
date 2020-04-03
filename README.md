# Restaurant-Site
Restaurant site build in Django framework. With Admin control panel. 

After clone, follow the steps below. 

install python3.7, pipenv then install the require dependencies with virtual environment: 

`pipenv --python3`

`pipenv sync`

Enter the virtual environment:

`pipenv shell`

All the codes below should run under the virtual environment with the depencies installed.

in the project directory, 

run the code below to migrate model to database. 

`python manage.py makemigrations`

`python manage.py migrate`
    



To run the server:

`python manage.py runserver`

visit 127.0.0.1:8000 for the site. 
visit 127.0.0.1:8000/admin to add/change restaurant webpage details.

To add superadmin:
`python manage.py createsuperuser` then follow the steps.

Create and complete a MainPage object in the admin page. tick is_active if you want show the page information.

Visit http://preciousstone.top/ to see demo

