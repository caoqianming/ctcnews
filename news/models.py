from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class News(models.Model):
    ZT_CHOICES = (
       (1, '发布中'),
       (2, '精选待发布'),
       (3, '精选已发布'),
       (0, '已发布'),
       )
    id = models.IntegerField('编号',primary_key=True, blank=True)  # AutoField?
    wxname = models.CharField('微信名称', blank=True, null=True, max_length =50)  # This field type is a guess.
    wxzb = models.CharField('文章标题', blank=True, null=True, max_length =200)  # This field type is a guess.
    wxsj = models.DateTimeField('发布时间', blank=True, null=True)
    wxread = models.IntegerField('阅读数', blank=True, null=True)
    wxhref = models.CharField('阅读地址', blank=True, null=True, max_length =500)  # This field type is a guess.
    imgurl = models.CharField('图片地址', blank=True, null=True, max_length =200)
    ispublished = models.IntegerField('状态', choices = ZT_CHOICES)
    wxzan = models.IntegerField('赞', blank=True, null=True)
    wxdetail = models.TextField('副标题',blank=True, null=True)
    '''def colored_ispublished(self):
        if self.ispublished == 1:
            color_code = 'read'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.ispublished,
            )'''
        
    class Meta:
        verbose_name = 'A微信公众号文章'
        verbose_name_plural = 'A微信公众号文章'
        db_table = 'news'

class Video(models.Model):
    id = models.IntegerField('编号',primary_key=True, blank=True, null=False)  # AutoField?
    videoname = models.CharField('视频标题',blank=True, null=True, max_length =200)  # This field type is a guess.
    video = models.FileField('视频', upload_to = 'uploadVideos')
    poster = models.ImageField('配图',upload_to = 'uploadVideos',default = 'uploadVideos/work1.jpg')
    info = models.TextField('视频介绍',blank=True, null=True)
    author = models.CharField('作者',blank=True, null=True, max_length =200)
    zan = models.IntegerField('赞')
	#videohref = models.CharField('播放地址',blank=True, null=True, max_length =200)  # This field type is a guess.

    class Meta:
        verbose_name = 'B安全环保视频'
        verbose_name_plural = 'B安全环保视频'
        db_table = 'video'
class Dep(models.Model):
    name = models.CharField('小组名称',primary_key=True, blank=True, null=False, max_length =200)
    detail = models.TextField('详情',blank=True, null=True)
    class Meta:
        verbose_name = 'F部门小组'
        verbose_name_plural = 'F部门小组'
        db_table = 'dep'
    def __str__(self):
        return self.name

class Main(models.Model):
    id = models.IntegerField('编号',primary_key=True, blank=True, null=False)
    title = models.CharField('资讯标题',blank=True, null=True, max_length =200)
    href = models.CharField('阅读地址', blank=True, null=True, max_length =200)
    pic = models.ImageField('配图', upload_to = 'uploadImages')
    #dep = models.CharField('发布部门',blank=True, null=True, max_length =200)
    dep = models.ForeignKey(Dep,verbose_name='发布部门')
    pubtime = models.DateField('首发日期',default = timezone.now)
    edittime = models.DateField('最后修改日期', auto_now = True)
    detail = models.TextField('视频介绍',blank=True, null=True, max_length =500)
    class Meta:
        verbose_name = 'C主页资讯'
        verbose_name_plural = 'C主页资讯'
        db_table = 'main'

class Oper(models.Model):
    id = models.IntegerField('编号',primary_key=True, blank=True, null=False)
    title = models.CharField('标题',blank=True, null=True, max_length =200)
    detail = models.CharField('详情',blank=True, null=True, max_length =400)
    href = models.CharField('链接', blank=True, null=True, max_length =200)
    pic = models.ImageField('配图', upload_to = 'uploadImages')
    class Meta:
        verbose_name = 'D系统链接'
        verbose_name_plural = 'D系统链接'
        db_table = 'oper'

class Picshow(models.Model):
    id = models.IntegerField('编号',primary_key=True, blank=True, null=False)
    title = models.CharField('标题',blank=True, null=True, max_length =200)
    href = models.CharField('链接', blank=True, null=True, max_length =200)
    pic = models.ImageField('配图', upload_to = 'uploadImages')
    class Meta:
        verbose_name = 'E主页切换图'
        verbose_name_plural = 'E主页切换图'
        db_table = 'picshow'




