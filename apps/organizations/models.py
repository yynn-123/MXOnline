from django.db import models
from apps.users.models import BaseModel
from apps.users.models import UserProfile
# Create your models here.
class City(BaseModel):
    name = models.CharField(max_length=20,verbose_name='城市名称')
    desc = models.CharField(max_length=300, verbose_name='城市描述')
    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name
    def __str__(self):
       return self.name

class CourseOrg(BaseModel):
    name = models.CharField(max_length=20, verbose_name='机构名称')
    tag = models.CharField(max_length=300,verbose_name='机构标签')
    degree = models.CharField(verbose_name='机构类别',choices=(("gr", "个人"), ("gx", "高校")),max_length=2)
    click_nums = models.IntegerField(verbose_name='点击数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数',default=0)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=300, verbose_name='机构地址')
    students = models.IntegerField(default=0,verbose_name="学习人数")
    course_nums = models.IntegerField(verbose_name='课程数',default=0)
    is_classics = models.BooleanField(default=False, verbose_name='是否认证')
    is_gold = models.BooleanField(default=False, verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses
    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name
    def __str__(self):
       return self.name



class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    orname = models.CharField(verbose_name="所属机构",max_length=200)
    name = models.CharField(max_length=20, verbose_name='教师名称')
    work_years =models.IntegerField(default=0,verbose_name='工作年限(年)')
    work_company = models.CharField(max_length=200,verbose_name="就职公司")
    position = models.CharField(max_length=200,verbose_name="公司职位")
    features = models.CharField(max_length=200,verbose_name="教学特点")
    click_nums = models.IntegerField(verbose_name='点击数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数',default=0)
    age = models.IntegerField(verbose_name='教师年龄',default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)
    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name
    def __str__(self):
       return self.name

    def course_nums(self):
        return self.course_set.all().count()