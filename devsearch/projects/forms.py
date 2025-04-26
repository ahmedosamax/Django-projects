from django.forms import ModelForm
from .models import project,Reviews
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = project
        fields = ['Title','Description','featured_image','Demo_link','Source_link','Tags']
        widgets = {
            'Tags' : forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        
        
        
        # self.fields['Title'].widget.attrs.update({'class':'input', 'placeholder' : 'Add title'})


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['Value','Body']
    
        labels = {
            'Value':"Place your vote",
            'Body':"Add a comment with your vote"
        }
    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args,**kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})