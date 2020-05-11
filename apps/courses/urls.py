from django.conf.urls import url
from apps.organizations.views import OrgView, AddAsk
from apps.courses.views import CouView
urlpatterns = [
    url(r'^list/$', CouView.as_view(), name='list'),

]