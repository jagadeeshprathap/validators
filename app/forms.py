from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is should not start with a')

class studentform(forms.Form):
    name=forms.CharField(max_length=40,validators=[check_for_a])
    age=forms.IntegerField()