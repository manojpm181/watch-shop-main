
from .models import WatchesUploads
from django import forms

class UploadForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    price = forms.DecimalField(
        widget= forms.NumberInput(attrs={'class':'form-control'}),
        required=True
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}),
        required=True
    )

    image = forms.CharField(
        widget=forms.ClearableFileInput(attrs={'class':'form-control'}),
        required=True
    )
    class Meta:
        model = WatchesUploads
        fields = ['name','price','description','image']