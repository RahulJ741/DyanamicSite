from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
ProjectType = (('I','Individual'), ('Co', 'Company Project'), ('T', 'Test'))


def thumbnail_upload(instance, filename):
    return 'Template/{}'.format(filename)


class TemplateList(models.Model):
    """(TemplateList description)"""
    name = models.CharField(blank=True, max_length=100)
    thumbnail = models.FileField(upload_to=thumbnail_upload)
    type = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return u"TemplateList"

    def __str__(self):
        return "{}/{}".format(settings.MEDIA_ROOT,self.thumbnail)




class Project(models.Model):
    """(Project description)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    template = models.ForeignKey(TemplateList, on_delete=models.SET_NULL, null=True, blank=True)
    project_type = models.CharField(max_length=100, choices=ProjectType, default='I')
    slug = models.SlugField(null=True, blank=True)

    def __unicode__(self):
        return u"Project"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)




class HeaderTypes(models.Model):
    """(HeaderType description)"""
    type = models.CharField(blank=True, max_length=100)


    def __unicode__(self):
        return u"HeaderType"

    def __str__(self):
        return self.type



class HeaderData(models.Model):
    """(HeaderData description)"""
    # type = models.CharField(blank=True, max_length=100)
    type = models.ForeignKey(HeaderTypes, on_delete = models.SET_NULL, null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    url = models.CharField(blank=True, max_length=100)
    color_code = models.CharField(blank=True, max_length=100)
    icon_path = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return u"HeaderData"

    def __str__(self):
        return "{} {}".format(self.name, self.type.type)


class ContactInfo(models.Model):
    """(ContactInfo description)"""
    email_address = models.EmailField()
    contact_number = models.CharField(blank=True, max_length=100, null=True)
    address = models.TextField(blank=True)
    twitter = models.URLField(blank=True)


    def __unicode__(self):
        return u"ContactInfo"

class MainContent(models.Model):
    """(MainContent description)"""
    header = models.ForeignKey(HeaderData, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    url = models.CharField(blank=True, max_length=100)
    header_content = models.CharField(blank=True, max_length=100)
    context = models.TextField(blank=True)

    def __unicode__(self):
        return u"MainContent"
