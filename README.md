# est3lmat

Super User Data:
username: MohammedMaher
password: maher

send POST request to "http://127.0.0.1:8000/auth/token/login" with valid user name and password to get access token

send POST request to "http://127.0.0.1:8000/api/person" with the information to add a new person(استعلام) (don't forget the acess token)

send GET request to "http://127.0.0.1:8000/api/person" to get all persons(استعلامات كلها)

send GET, PUT, PATCH or DELETE requests to "http://127.0.0.1:8000/api/person/id" to get, remove or update person(استعلام)

send POST request to "http://127.0.0.1:8000/api/approval" with the information to add a new Approval(اسم المستشفى ونوع اللجنة)

send GET request to "http://127.0.0.1:8000/api/approval" to get all Approvals

send GET, PUT, PATCH or DELETE requests to "http://127.0.0.1:8000/api/approval/id" to get, remove or update Approval

---

install this version of python https://www.python.org/downloads/release/python-390/
install pipenv using this command "pip install pipenv"
go to the backend folder in vs code and run this command "pipenv install"
then run this command "pipenv shell"
then go the Inquireis folder and run this command to run the server "python manage.py runserver"
