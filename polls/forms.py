from django import forms

class XMLUploadForm(forms.Form):
    xml_file = forms.FileField(label="上傳 XML 文件")
