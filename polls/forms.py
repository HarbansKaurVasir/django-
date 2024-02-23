from django import forms
from .models import Student
 
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            "name",
            "phone",
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        phone = cleaned_data.get("phone")
        
        # Example validation: ensure name is not empty
        if not name:
            raise forms.ValidationError("Name cannot be empty")
    
        # Example validation: ensure phone is a valid format
        if phone and not str(phone).isdigit():
            raise forms.ValidationError("Phone must contain only digits")

        return cleaned_data