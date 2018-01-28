from django import forms
from inventory.models import inventory

class inventory_form (forms.ModelForm):

    inv_name = inventory.inv_name
    notes = inventory.notes

    class Meta:
        model = inventory
        fields = {
        'inv_name',
        'notes'
        }

    def save (self, commit=True):
        inventory = super(inventory_form, self).save(commit=False)
    

        if commit:
            inventory.save()

        return inventory
