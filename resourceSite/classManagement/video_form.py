__author__ = 'samuel'

from django import forms

class VideoForm(forms.Form):
    content = forms.CharField(error_messages={
        'required': u'请填写回复内容',})