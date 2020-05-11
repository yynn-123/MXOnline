from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here
class CouView(View):
    def get(self,request,*args,**kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        course = Course.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(course, per_page=3, request=request)
        courses = p.page(page)
        return render(request,'course-list.html',{"course":course,'courses':courses})