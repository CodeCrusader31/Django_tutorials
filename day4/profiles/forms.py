from django import forms

# class ProfileForm(forms.Form):
#     user_image = forms.FileField()

class ProfileForm(forms.Form):
    user_image = forms.ImageField()
