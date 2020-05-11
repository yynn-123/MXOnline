from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from apps.organizations.models import CourseOrg, City, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.forms import AddAskForm
from django.http import JsonResponse


class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
        展示授课机构l列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 获取点击的目录:
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(degree=category)
        # 对所在城市进行筛选
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对课程机构进行排序 -代表倒序排序
        sort = request.GET.get('sort', '')
        if sort == 'student':
            # 根据学生人数排序

            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            # 根据课程数排序
            all_orgs = all_orgs.order_by('-course_nums')

        org_nums = CourseOrg.objects.all().count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=3, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html',
                      {'all_orgs': orgs, 'org_nums': org_nums, 'all_citys': all_citys, 'category': category,
                       'city_id': city_id, 'sort': sort, 'hot_orgs': hot_orgs})


class AddAsk(View):
    """处理用户咨询模块"""

    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success",
                "msg": "提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })
