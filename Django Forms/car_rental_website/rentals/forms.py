from django import forms

class RentalReview(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'myform'}))
    last_name = forms.CharField(label='Last Name', max_length=100)
    email_address = forms.EmailField(label='Email Address')
    feedback = forms.CharField(label='Please enter your review here:', widget=forms.Textarea(attrs={'class' : 'myform', 'rows' : '2'}))