from django import forms;
class LoginForm(forms.Form):
	name=forms.CharField();
	surName=forms.CharField();
	fatherName=forms.CharField();
	motherName=forms.CharField();
	dateOfBirth=forms.DateField();

# application-4
from django import forms;
class ItemAddForm(forms.Form):
	name = forms.CharField();
	quantity = forms.IntegerField();




