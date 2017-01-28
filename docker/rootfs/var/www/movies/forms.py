from django import forms
class video_form(forms.Form):
    video_name = forms.CharField()
    video_type=forms.CharField()
    views=forms.FloatField()
    video_file=forms.FileField()
    video_rate=forms.FloatField()
class comment_form(forms.Form):
    user_comment=forms.CharField(required = True)
    user_email=forms.EmailField(required = True)
