from django.db import models

# Create your models here.

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
    name = models.CharField(blank=True, max_length=100)
    url = models.CharField(blank=True, max_length=100)
    header_content = models.CharField(blank=True, max_length=100)
    context = models.TextField(blank=True)

    def __unicode__(self):
        return u"MainContent"
