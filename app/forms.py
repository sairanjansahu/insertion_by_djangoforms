from django import forms

class Topicform(forms.Form):
    topic_name=forms.CharField(max_length=100)

class Webpageform(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField()

class AccessRecordform(forms.Form):
    name=forms.CharField(max_length=100)
    author=forms.CharField(max_length=100)
    date=forms.DateField()