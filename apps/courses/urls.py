from django.conf.urls import url
from apps.organizations.views import OrgView, AddAsk
from apps.courses.views import CouView,CouDetailView,CourseLessonView,VideoView,CourseCommentsView
urlpatterns = [
    url(r'^list/$', CouView.as_view(), name='list'),
    url(r'^(?P<course_id>\d+)/$', CouDetailView.as_view(), name='detail'),
    url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
    url(r'^(?P<course_id>\d+)/comments/$', CourseCommentsView.as_view(), name='comments'),
    url(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)$', VideoView.as_view(), name='video'),

]