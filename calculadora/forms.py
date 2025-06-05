from django import forms

class FuncionForm(forms.Form):
    funcion = forms.CharField(label='Función f(x)', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: x**3 - x - 2'}))
    metodo = forms.ChoiceField(choices=[('biseccion', 'Bisección'), ('newton', 'Newton-Raphson'), ('newton_mod', 'Newton-Raphson Modificado')])
    
    a = forms.FloatField(required=False, label='Extremo a')
    b = forms.FloatField(required=False, label='Extremo b')
    
    x0 = forms.FloatField(required=False, label='Valor inicial x0')
    
    tol = forms.FloatField(label='Tolerancia', min_value=0)
    max_iter = forms.IntegerField(label='Máximo número de iteraciones', min_value=1)
    
    def clean(self):
        cleaned_data = super().clean()
        metodo = cleaned_data.get('metodo')
        
        if metodo == 'biseccion':
            if cleaned_data.get('a') is None or cleaned_data.get('b') is None:
                raise forms.ValidationError("Para Bisección debe ingresar los extremos a y b.")
            if cleaned_data.get('a') >= cleaned_data.get('b'):
                raise forms.ValidationError("El extremo a debe ser menor que b.")
        else:
            if cleaned_data.get('x0') is None:
                raise forms.ValidationError("Para Newton debe ingresar valor inicial x0.")
