# Talent Portal

A simplified implementation of a recruitment portal.

## Requirements

[Requirements.txt](/requirements.txt)

## Running

1. git clone [https://github.com/bravin99/talentportal.git](https://github.com/bravin99/talentportal.git)
2. ``` cd talentportal ```
3. ``` python -m venv venv ```
4. ``` source venv/bin/activate ```
5. ``` pip install -r requirements.txt ```
6. ``` python manage.py makemigrations ```
7. ``` python manage.py migrate ```
8. ``` python manage.py createsuperuser ```
9. ``` python manage.py runserver 8000 ```
10. Navigate to 127.0.0.1:8000 or 127.0.0.1:8000/admin



## Design

### Job App

![Job listing page](/static/img/jobpage.png)
![My applications](/static/img/application-listing-30.png)


### Resume page

![Resume page: education](/static/img/resume-education.png)
