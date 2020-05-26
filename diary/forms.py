from django import forms
from .models import Day
# models.pyから自動的に読み取ってFormを作成してくれる
class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__' #('title','text')で個々に指定もできる