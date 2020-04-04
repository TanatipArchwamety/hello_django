
Time explained

First day: 28Mar2020 21:00 - 04:00
- Read Heroku.
- Read Django version 3.0.4.
- Build local environment, facing postgresql problems on Cygwin (MySQL works, but will not match the test).
- Try Heroku and found that it has very slow response.
- Build personal droplet of Digital Ocean cloud server, Ubuntu18.04.3.
- Build Django-postgres application.
- Stuck with the configuration of "supervisor" module to be integrated with gunicorn, nginx.
- Mistakes from using virtualenv, decide to rebuild droplet, application.
- Read pipenv.
- Rebuild Django-postgres application, customize settings, models, admin. Test adding some records with pic.
- First commit git.

Second day: 29Mar2020 17:00 - 19:15,  22:00 - 01:00
- Revise and go over Django Rest Framework.
- Try function-based view version.
- Read generic views.
- Read serializer.
- Try generic view version.
- Read model views set.
- Try model set view version.
- Add feature unique uuid hex.
- Add feature checking student amount not exceeding school max_student capacity on serializer, model-save, model-create.
- Manually test multiple times, debugging.
- Read simple router.
- Try simple router.
- Read nested router.
- Try nested router.

Third day: 4Apr2020 20:00 - 22:00
- Improve: Student filter by first_name, last_name, nationality (?first_name=, ?last_name=, ?nationality=,)
- Improve: Data populate method as initial data with fixtures, utils-script using python-faker
- Improve: Implement pagination max=10 after populated hundreds of students

Note:
This application still not included these following topics:
- Bonus topics:  Heroku
- Proper design of foreignkey-relation such as nationality, more attributes such ah birthdate + age calculation.
- Front end template.
- Nginx, Gunicorn, Supervisor integration.
