# App links 

The app was deployed on Digital Ocean.

There are two users, that were loaded from fixtures:

## Superuser

Login: admin

Password: 12345

## Regular user

Login: test

Password: test12345

Login page - https://note-app-xdz2h.ondigitalocean.app/login/ 

Admin panel - https://note-app-xdz2h.ondigitalocean.app/admin/
# Launch the project on your local machine
   1. Download and launch [Docker](https://www.docker.com/).
   2. Clone repository
   3. Open directory with cloned repository
   4. Run the following commands:
      
      To build containers:
      ```python
      docker-compose up --build
      ```
      To run the migration:
      ```python
      docker-compose exec web python manage.py migrate
      ```
      To load fixtures data:
      ```python
      docker-compose exec web python manage.py loaddata
      ```

Admin panel - https://127.0.0.1:8000/admin

Login page - https://127.0.0.1:8000/login

# Env file
  Env file was added to the repository to make the project easier to launch on the local machine. It was done only for time economy during checking test task. 

# Additional features
  In addition to tasks that were described, the next features were added:
  1. User system (login/registration).
  2. Next note fields (word count, unique word count, created at) were added for easier understanding of note filters.
  3. UI was created with help of [Flowbite](https://flowbite.com/) and [TailwindCSS](https://tailwindcss.com/)
  


