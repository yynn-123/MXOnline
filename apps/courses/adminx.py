import xadmin
from apps.courses.models import Course, Lesson, CourseTag, Video,CourseResource


# 不用继承admin.ModelAdmin
class CourseAdmin(object):
    list_display = ['id', 'name', 'desc', 'learn_times', 'degree']
    search_fields = ['name']
    list_filter = ['id', 'name', 'desc', 'learn_times', 'degree']


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'learn_times']


class VideoAdmin(object):
    list_display = ['lensson', 'name']
    search_fields = ['lensson', 'name']
    list_filter = ['lensson', 'name']


class CourseTagAdmin(object):
    list_display = ['course', 'tag']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag']


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class CourseResourceAdmin(object):
    list_display = ['course', 'name','file']
    search_fields = ['course', 'name','file']
    list_filter = ['course', 'name','file']






xadmin.site.register(Course, CourseAdmin),
xadmin.site.register(Lesson, LessonAdmin),
xadmin.site.register(CourseTag, CourseTagAdmin),
xadmin.site.register(Video, VideoAdmin),
xadmin.site.register(CourseResource, CourseResourceAdmin),
