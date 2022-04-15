from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'sex', 'personID', 'email', 'birth', 'edu', 'school',
                  'major', 'experience', 'position', 'photo')
        sex_list = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )
        edu_list = (
            # ('大专', '大专'),
            ('Bachelor', 'Bachelor'),
            ('Master', 'Master'),
            ('Doctor', 'Doctor'),
            ('others', 'others'),
        )
        widgets = {
            'sex': forms.Select(choices=sex_list),
            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }