from django.conf.urls import url, include

from rest_framework import routers
from .views import JobViewSet, JobCountView


router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    url(r'^jobs/count/$', JobCountView.as_view(), name='count'),
    url(r'^', include(router.urls)),
]
