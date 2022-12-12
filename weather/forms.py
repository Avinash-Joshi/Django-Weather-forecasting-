# from django import forms
# from .models import Data


# class NameForm(forms.Form):
#     State = forms.CharField(label='State', max_length=100)

#     def clean(self):
#         cleaned_data = super(NameForm, self).clean()
#         State = cleaned_data.get("State")
#         p = Data.objects.all()
#         for i in p:
#             j=0
#             try:
#                 p = Data.objects.get(i.j.State=State)
#             except:
#                 return False
                    
