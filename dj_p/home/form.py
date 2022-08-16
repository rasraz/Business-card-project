from django import forms

class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    subject=forms.CharField(max_length=50)
    estimated_budget=forms.CharField(max_length=50)
    enter_your_message=forms.CharField(widget=forms.Textarea)

    def clean_estimated_budget(self):
        estimated_budget=self.cleaned_data['estimated_budget']
        if not isinstance(estimated_budget,int):
            raise forms.ValidationError('Please enter only numbers',code='not_number')
        return estimated_budget