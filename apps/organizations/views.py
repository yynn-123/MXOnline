from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from apps.organizations.models import CourseOrg,City,Teacher
class OrgView(View):
    def get(self,request,*args,**kwargs):
        """
        展示授课机构l列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.all().count()
        all_citys = City.objects.all()

        return render(request,'org-list.html',
                      {'all_orgs':all_orgs,'org_nums':org_nums,'all_citys':all_citys})