import xadmin
from apps.courses.models import Course
#不用继承admin.ModelAdmin
class CourseAdmin(object):
    list_display = ['id','name','desc','learn_times','degree']
    search_fields = ['name']
    list_filter = ['id','name','desc','learn_times','degree']
xadmin.site.register(Course,CourseAdmin)