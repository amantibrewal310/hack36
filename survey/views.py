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

        return render(request,'survey/data.html', {'success':'done'})

    return render(request,'survey/create.html', {'form':form})

def fetchData(request):

    total = Survey.objects.all()
    web_dev = Survey.objects.all().filter(skills='Web Development')
    and_dev = Survey.objects.all().filter(skills='Android Development')
    comm_skill = Survey.objects.all().filter(skills='Communication')
    ml = Survey.objects.all().filter(skills='Machine Learning')
    iot =Survey.objects.all().filter(skills='Internet of things')
        
    args = {
        'web_dev':len(web_dev),
        'and_dev':len(and_dev),
        'comm_skill':len(comm_skill),
        'ml':len(ml),
        'iot':len(iot),
        'total':len(total)
    }

    return render(request,'survey/data.html',args)
        