from django import forms
from home.models import QuickContact


class  QuickContactForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="User name",
        widget=forms.TextInput({"paceholder" : "Name *"}
        )
    )
    email = forms.EmailField(
        label="User email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email *"},
        ),
    )
    massage = forms.CharField(
        widget=forms.Textarea(
            attrs={"paceholder" : "Massage *",
            "row": 3,
                }
            )
        )


    def save(self):
        QuickContact.objects.create(**self.cleaned_data)



    def clean(self):
        return self.changed_data

class QuickContactForm(forms.ModelForm):


    class Meta:
        model=QuickContact
        fields = "__all__"

    