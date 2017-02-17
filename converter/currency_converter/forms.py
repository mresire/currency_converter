from django import forms
from currency_converter.models import history

class historyform(forms.ModelForm):
	class Meta:
		model = history
		fields = '__all__'