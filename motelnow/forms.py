from django.forms import ModelForm

from motelnow.models import Hostal


class HostalForm(ModelForm):
    class Meta:
        model = Hostal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['departamento'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono1'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono2'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio_minimo'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio_maximo'].widget.attrs.update({'class': 'form-control'})
        self.fields['activo'].widget.attrs.update({'class': 'form-control'})

    def is_valid(self):

        valid = super(HostalForm, self).is_valid()

        # we're done now if not valid
        if not valid:
            return valid

        # telefono1 = self.cleaned_data['telefono1']
        # if not telefono1:
        #     self.add_error('telefono1', 'ingresa el campo telefono1')
        #     return False

        return True

