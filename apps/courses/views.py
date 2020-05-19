from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operations.models import UserFavorite,UserCourse


# Create your views here
class CouView(View):
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        course = Course.objects.all()
        hot_course = course.order_by('-click_nums')[:3]
        sort = request.GET.get('sort', '')
        if sort == 'hot':
            course = course.order_by('-click_nums')
        elif sort == 'students':
            course = course.order_by('-students')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(course, per_page=3, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html',
                      {"course": course, 'courses': courses, 'sort': sort, 'hot_course': hot_course})


class CouDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        has_fav_course = False
        has_fav_org = False
        # 获取收藏状态
        if request.user.is_authenticated:
        # 查询用户是否收藏了该机构
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=2):
                has_fav_org = True
        # tag = course.tag
        # related_courses = []
        # if tag:
        #     related_courses = Course.objects.filter(tag= tag).exclude(id__in = [course.id])[:3]


        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]
        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id = course.id)
        related_courses = set()
        for course_tag in course_tags:
            related_courses.add(course_tag.course)
        return render(request, 'course-detail.html', {
            'course': course,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
            'related_courses':related_courses
        })



class CourseLessonView(View):
    """
    章节信息
    """
    login_url = '/login'
    def get(self,request,course_id,*args,**kwargs):
        course = Course.objects.get(id = int(course_id))
        course.click_nums += 1
        course.save()

        user_course = UserCourse.objects.filter(course = course)
        user_ids = [user_course.user.id for user_course in user_course]
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # 过滤掉当前课程
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)



        course_resource = CourseResource.objects.filter(course=course)
        return render(request,'course-video.html', {
            'course': course,
            'course_resource':course_resource,
            'related_courses':related_courses
        })