from django.contrib import admin
from . models import *
class AdminLearniMaterials(admin.ModelAdmin):
    list_display=['Document_name','Course_name','Year','Semester','Document','date_added']

class AdminVideo(admin.ModelAdmin):
    list_display=['id','author','vid_description','video_file','date_added']

class AdminSoftware(admin.ModelAdmin):
    list_display=['id','author','Software_description','Software_file','date_added']

admin.site.register(LearniMaterials,AdminLearniMaterials),
admin.site.register(Video,AdminVideo)
admin.site.register(Software,AdminSoftware)

# Register your models here.
