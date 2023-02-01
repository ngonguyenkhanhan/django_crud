from django import forms
from .models import GeeksModel

# creating a form with
class GeeksForm(forms.ModelForm):
    
    # create meta class
    class Meta:
        # Specify model to be used
        model = GeeksModel
        
        # Specify fields to be used
        fields = [
            'title',
            'description',
        ]