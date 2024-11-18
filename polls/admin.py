from django.contrib import admin
from .models import Question, CustomUser

from django.contrib import admin


# Register your models here.
admin.site.register(Question)
admin.site.register(CustomUser)
#
import csv
from django import forms
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Course

# 自定义 CSV 上传表单
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

# 注册模型到 admin 中
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    change_list_template = "admin/course_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv, name='upload_csv'),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data["csv_file"]
                try:
                    # 读取 CSV 数据
                    data = csv.reader(csv_file.read().decode('utf-8').splitlines())
                    header = next(data)  # 跳过标题行
                    for row in data:
                        Course.objects.create(
                            id=int(row[0]),
                            semester=row[1],
                            primary_instructor=row[2],
                            course_code_new=row[3],
                            department_code=row[4],
                            core_code=row[5],
                            course_group=row[6],
                            grade=row[7],
                            class_group=row[8],
                            course_name_cn=row[9],
                            course_name_en=row[10],
                            instructor_name=row[11],
                            enrollment=int(row[12]),
                            male_students=int(row[13]),
                            female_students=int(row[14]),
                            credits=int(row[15]),
                            weeks=row[16],
                            hours_per_week=float(row[17]),
                            course_type_code=row[18],
                            course_type=row[19],
                            location=row[20],
                            weekday=row[21],
                            class_period=row[22],
                            notes=row[23] if row[23] else None,
                            course_summary_cn=row[24] if row[24] else None,
                            course_summary_en=row[25] if row[25] else None,
                            primary_instructor_code_old=row[26],
                            course_code_old=row[27],
                            schedule_code_old=row[28],
                            schedule_name_old=row[29],
                            instructor_code_old=row[30]
                        )

                except Exception as e:
                    self.message_user(request, f"Error processing CSV file: {e}", level="error")
                else:
                    self.message_user(request, "CSV file successfully uploaded")
                return HttpResponseRedirect("../")

        form = CSVUploadForm()
        context = {
            **self.admin_site.each_context(request),
            'form': form
        }
        return render(request, "admin/csv_upload_form.html", context)
#
# admin.site.register(Course, CourseAdmin)  # 确保只有这一行注册代码
