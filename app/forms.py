from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is should not start with a')

class studentform(forms.Form):
    name=forms.CharField(max_length=40,validators=[check_for_a])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=50,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']

        if e!=r:
            raise forms.ValidationError('not matched')

    def clean_age(self):
        age=self.cleaned_data['age']

        if age>9:
            raise forms.ValidationError('not valid')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
    
        if len(bot)>0:
            raise forms.ValidationError('no such data')

        
