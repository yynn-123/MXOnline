from django.conf.urls import url
from apps.organizations.views import OrgView, AddAsk
from apps.courses.views import CouView,CouDetailView
urlpatterns = [
    url(r'^list/$', CouView.as_view(), name='list'),
    url(r'^(?P<course_id>\d+)/$', CouDetailView.as_view(), name='detail'),

]