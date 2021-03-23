from django.contrib import admin
from nitc.models import Branch,Course,Register,Teacher,MFY,Course_Part,Sector,ManagerNITS,Skills
from django.contrib.auth.models import User
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display=['id']
class BranchAdmin(admin.ModelAdmin):
    list_display=['id','name','address','contact_number']

class CourseAdmin(admin.ModelAdmin):
    list_display=['id','name','course_time','payment']

class RegisterAdmin(admin.ModelAdmin):
    list_display=['user','contact_number','branch','course','startdate']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['fullname','Branch','phone','Branch_id']

class MFYAdmin(admin.ModelAdmin):
    list_display=['id','name','branch','branch_id','sector']

class Course_PartAdmin(admin.ModelAdmin):
    list_display=['course','name']

class SectorAdmin(admin.ModelAdmin):
    list_display=['branch','name']

class ManagerNITSAdmin(admin.ModelAdmin):
    list_display=['user_id','id','user','branch','branch_id']


class SkillsAdmin(admin.ModelAdmin):
    list_display=['course','course_id','teacher','teacher_id']

admin.site.register(Sector,SectorAdmin)
admin.site.register(Course_Part,Course_PartAdmin)
admin.site.register(MFY,MFYAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(ManagerNITS,ManagerNITSAdmin)
admin.site.register(Register,RegisterAdmin)
admin.site.register(Skills,SkillsAdmin)



