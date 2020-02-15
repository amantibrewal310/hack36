from django.shortcuts import render
from django.forms import ModelForm
from django import forms


from survey.models import Survey

class SurveyForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Name",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Name'",
            'required':"",
            'type':"text"
    }))
    skills = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Skills yo want to learn",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Skills yo want to learn'",
            'required':"",
            'type':"text"
    }))
    age = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':"Age",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Age'",
            'required':"",
            'type':"text"
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"City",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'City'",
            'required':"",
            'type':"text"
    }))

    class Meta:
        model = Survey
        fields = ['name', 'skills','age','city']

def survey_create(request):
    form = SurveyForm(request.POST or None)
    if form.is_valid():
        form.save()

        return render(request,'survey/create.html', {'success':'done'})

    return render(request,'survey/create.html', {'form':form})

def fetchData(request):

    a = Survey.objects.all()
    web_dev = 0 
    and_dev = 0
    comm_skill = 0
    ml = 0
    iot =0
    others =0
    for i in a:
        pass