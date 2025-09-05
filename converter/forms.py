from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True   # 👈 this enables multiple uploads

class ImageUploadForm(forms.Form):
    images = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True}),
        required=True
    )
