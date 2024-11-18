import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')#date
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#foreignkey
    choice_text = models.CharField(max_length=200)#choice,[choice_text] is columnＮame
    votes = models.IntegerField(default=0)# votes integer default=0
    def __str__(self):
        return self.choice_text
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)  # 自動加密密碼
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Course(models.Model):
        id = models.AutoField(primary_key=True)  # 編號
        semester = models.CharField(max_length=50)  # 學期
        primary_instructor = models.CharField(max_length=255)  # 主開課教師姓名
        course_code_new = models.CharField(max_length=50)  # 科目代碼(新碼全碼)
        department_code = models.CharField(max_length=50)  # 系所代碼
        core_code = models.CharField(max_length=50)  # 核心四碼
        course_group = models.CharField(max_length=50)  # 科目組別
        grade = models.CharField(max_length=50)  # 年級
        class_group = models.CharField(max_length=50)  # 上課班組
        course_name_cn = models.CharField(max_length=255)  # 科目中文名稱
        course_name_en = models.CharField(max_length=255)  # 科目英文名稱
        instructor_name = models.CharField(max_length=255)  # 授課教師姓名
        enrollment = models.IntegerField()  # 上課人數
        male_students = models.IntegerField()  # 男學生上課人數
        female_students = models.IntegerField()  # 女學生上課人數
        credits = models.IntegerField()  # 學分數
        weeks = models.CharField(max_length=50)  # 上課週次
        hours_per_week = models.FloatField()  # 上課時數/週
        course_type_code = models.CharField(max_length=50)  # 課別代碼
        course_type = models.CharField(max_length=100)  # 課別名稱
        location = models.CharField(max_length=100)  # 上課地點
        weekday = models.CharField(max_length=20)  # 上課星期
        class_period = models.CharField(max_length=50)  # 上課節次
        notes = models.TextField(blank=True, null=True)  # 課表備註
        course_summary_cn = models.TextField(blank=True, null=True)  # 課程中文摘要
        course_summary_en = models.TextField(blank=True, null=True)  # 課程英文摘要
        primary_instructor_code_old = models.CharField(max_length=50)  # 主開課教師代碼(舊碼)
        course_code_old = models.CharField(max_length=50)  # 科目代碼(舊碼)
        schedule_code_old = models.CharField(max_length=50)  # 課表代碼(舊碼)
        schedule_name_old = models.CharField(max_length=100)  # 課表名稱(舊碼)
        instructor_code_old = models.CharField(max_length=50)  # 授課教師代碼(舊碼)

        def __str__(self):
            return self.course_name_cn