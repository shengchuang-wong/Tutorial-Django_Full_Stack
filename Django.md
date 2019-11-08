
# Conda
- `conda create --name myEnv django` < create environment named "myEnv" with latest django
- `activate myEnv` < `source activate for macos`
- `deactive myEnv`
- `conda info --envs` < list all the environment
- `conda install [packageName]` or `pip install django` < after active environment

# django commands
- `django-admin startproject first_project` <<< instantiate new project named "first_project"
- `python manage.py runserver` = start server

# Steps to install django app into django project
- `python manage.py startapp [appName]` = create app
- Go to project settings.py INSTALLED_APPS, add the [appName]

# Migration
- `python manage.py migrate`
- `python manage.py makemigrations [appName]`

# Admin Interface
- `python manage.py createsuperuser`

# Database
- `python manage.py shell`
When inside
- `from [appName].models import [tableName]`
- `print([tableName].objects.all())` = get all data in the table
- `[variableName] = [tableName]([fieldName]="[fieldValue]")`
- `[variableName].save()`