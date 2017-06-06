#- django + vuejs

#- 0x00 init

$ django-admin startproject django-vuejs

$ cd djangovuejs

$ python manage.py runserver


#- 0x01 backend and frontend scaffold

$ python manage.py startapp backend

$ vue-init webpack frontend

$ cd frontend

$ npm install

$ npm run dev

$ npm run build

# npm run build will build the dist/ directory with index.html and static/

- ./djangovuejs/urls.py
...
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^api/', include('backend.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]
...

- ./djangovuejs/settings.py
...
TEMPLATES = [
    {
        ...,
        'DIRS': ['frontend/dist'],
        ...,
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist/static'),
]
...

$ cd ..

$ python manage.py runserver


#- 0x02 backend apis

- ./djangovuejs/settings.py
...
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'backend.apps.BackendConfig',
]
...

- ./backend/models.py

- ./backend/serializers.py

- ./backend/views.py

- ./backend/urls.py

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

# http://127.0.0.1:8000/api/
# http://127.0.0.1:8000/api/jobs/


#- 0x03 frontend views

- ./frontend/index.html

- ./frontend/src/App.vue

- ./frontend/src/router/index.js

$ cd frontend

$ npm install --save axios

$ cd ..

- ./frontend/src/components/Job.vue
...
<script>
import axios from 'axios'
...
</script>
...

$ cd frontend

$ npm run build

$ cd ..

$ python manage.py runserver


#- 0x04 frontend development with backend apis

$ pip install django-cors-headers

- ./djanovuejs/settings.py
...
MIDDLEWARE = [
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]

# django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True
...

$ python manage.py runserver

# open a new terminal with ctrl + alt + t

$ cd frontend

$ npm run dev

# now, frontend views hot reload in ms at localhost:8080
# with backend apis available at 127.0.0.1:8000, however

# issue is that at axios.get|post() call in frontend <scripts> have to use
# axios.get(http://127.0.0.1:8000/api/jobs) instead of axios.get(/api/jobs)
# which is not reproducible.

# one possible solution is define baseURL which config by dev/prod.

- ./frontend/src/components/Job.vue
...
<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
...
</script>
...

# note: how to make the baseURL config by dev/prod?




