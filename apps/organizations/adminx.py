import xadmin
from apps.organizations.models import *
class CourseOrgAdmin(object):
    pass
class CityAdmin(object):
    pass
class TeacherAdmin(object):
    pass
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Teacher,TeacherAdmin)