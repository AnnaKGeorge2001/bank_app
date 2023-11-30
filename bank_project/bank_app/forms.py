from django import forms
from bank_app.models import Customer, District, Branch, AccountType, Material

class CustomerForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label="Select Branch")
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(), empty_label="Select Account Type")
    materials_provide = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)
                self.fields['materials_provide'].queryset = Material.objects.all()  # Fetch all materials from the database
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.all()
            self.fields['materials_provide'].queryset = Material.objects.all()
