#from django.contrib.admin import AdminSite
from django.contrib import admin
from news.models import News
from news.models import Video
from news.models import Main,Oper,Picshow,Dep
import datetime
# Register your models here.

def make_jxdfb(modeladmin, request, queryset):
    queryset.update(ispublished = '2')

    
make_jxdfb.short_description = "设为精选待发布" 

def make_jxyfb(modeladmin, request, queryset):
    queryset.update(ispublished = '3')

make_jxyfb.short_description = "设为精选已发布" 

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','wxname','ispublished', 'wxzb', 'wxdetail','wxsj','wxread', 'wxzan')
    list_filter = ('wxsj','ispublished')
    list_editable = ['ispublished']
    list_display_links = ('id', 'wxzb')
    list_per_page = 50
    search_fields =('wxzb',) #搜索字段
    date_hierarchy = 'wxsj'
    actions = [make_jxdfb,make_jxyfb]  


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'videoname', 'video', 'zan')
    list_display_links = ('id', 'videoname')


#class MyAdminSite(AdminSite):
    #site_header = 'ctc微信爬虫后台管理系统'
    #site_title = '管理后台'
class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'href')
    list_display_links = ('id', 'title')

class OperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'href', 'pic')
    list_display_links = ('id', 'title')
    list_editable = ['pic']

class PicshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'href', 'pic')
    list_display_links = ('id', 'title')
    list_editable = ['pic']


class DepAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')

admin.site.site_header = 'ctc微信爬虫后台管理'
admin.site.site_title = '管理后台'
admin.site.register(Oper, OperAdmin)
admin.site.register(News, NewsAdmin)   
admin.site.register(Video, VideoAdmin)
admin.site.register(Main, MainAdmin)
admin.site.register(Picshow, PicshowAdmin)
admin.site.register(Dep, DepAdmin)





