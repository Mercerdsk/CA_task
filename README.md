# CA_task
Task for Customer Analytics


Install the libraries from the requirements.txt file using the below command
 
 pip install -r requirements.txt
 
 
PostgreSQL connection

please change the database connection in the database_credentials.py in myproject directory

To start the application


step 1:
   To start the migrated the schema changed in your PostgreSql Database use the below commands
   
    python3 manage.py makemigrations
    python3 manage.py migrate
    
 step 2: 
    To start the server use the below command
    
    python manage.py runserver 0.0.0.0:8000
    
 Use your prefered browser to view the User interface using the below link
 
 http://0.0.0.0:8000/
 
 For SQLite users, Skip step 1 because the schema are already migrated for sqlite
