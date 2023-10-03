from django import forms
from .models import Review
from django.forms import ModelForm

'''
class RentalReview(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'myform'}))
    last_name = forms.CharField(label='Last Name', max_length=100)
    email_address = forms.EmailField(label='Email Address')
    feedback = forms.CharField(label='Please enter your review here:', widget=forms.Textarea(attrs={'class' : 'myform', 'rows' : '2'}))
'''

# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/

class RentalReview(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars'] # the fields you wish to interact with
        fields = "__all__" # as above to pass all fields

        # how to overwrite the labels
        labels  = {
            'first_name' : "YOUR_FIRST_NAME",
            'last_name' : "YOUR_LAST_NAME",
            'stars' : "RATING"
        }

        error_messages = {
            'stars': {
                'min_value' : 'You entered a value lower than 1.',
                'max_value' : 'You entered a value higher than 5'
            }
        }