from django.shortcuts import render
from .forms import FuncionForm
from .utils import biseccion, newton_raphson, newton_raphson_modificado
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

def graficar_funcion(f_expr, raiz=None, intervalo=None):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    import numpy as np
    
    if intervalo:
        x_vals = np.linspace(intervalo[0], intervalo[1], 400)
    else:
        x_vals = np.linspace(-10, 10, 400)
    
    y_vals = f(x_vals)
    
    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    
    if raiz is not None:
        plt.scatter([raiz], [0], color='red', label='Raíz aproximada')
    if intervalo:
        plt.axvspan(intervalo[0], intervalo[1], color='yellow', alpha=0.3, label='Intervalo Bisección')
    
    plt.legend()
    plt.grid(True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

def calcular_raiz(request):
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            funcion_str = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            tol = form.cleaned_data['tol']
            max_iter = form.cleaned_data['max_iter']
            
            x = sp.symbols('x')
            try:
                f_expr = sp.sympify(funcion_str)
                f = sp.lambdify(x, f_expr, 'numpy')
            except:
                form.add_error('funcion', 'Función inválida.')
                return render(request, 'calculadora/index.html', {'form': form})
            
            try:
                if metodo == 'biseccion':
                    a = form.cleaned_data['a']
                    b = form.cleaned_data['b']
                    iteraciones, raiz = biseccion(f, a, b, tol, max_iter)
                    img = graficar_funcion(f_expr, raiz=raiz, intervalo=(a,b))
                    context = {'form': form, 'iteraciones': iteraciones, 'raiz': raiz, 'grafica': img, 'metodo': 'Bisección'}
                
                elif metodo == 'newton':
                    x0 = form.cleaned_data['x0']
                    df_expr = sp.diff(f_expr, x)
                    df = sp.lambdify(x, df_expr, 'numpy')
                    iteraciones, raiz = newton_raphson(f, df, x0, tol, max_iter)
                    img = graficar_funcion(f_expr, raiz=raiz)
                    context = {'form': form, 'iteraciones': iteraciones, 'raiz': raiz, 'grafica': img, 'metodo': 'Newton-Raphson'}
                
                elif metodo == 'newton_mod':
                    x0 = form.cleaned_data['x0']
                    df_expr = sp.diff(f_expr, x)
                    ddf_expr = sp.diff(df_expr, x)
                    df = sp.lambdify(x, df_expr, 'numpy')
                    ddf = sp.lambdify(x, ddf_expr, 'numpy')
                    iteraciones, raiz = newton_raphson_modificado(f, ddf, df, x0, tol, max_iter)
                    img = graficar_funcion(f_expr, raiz=raiz)
                    context = {'form': form, 'iteraciones': iteraciones, 'raiz': raiz, 'grafica': img, 'metodo': 'Newton-Raphson Modificado'}
                
                else:
                    context = {'form': form, 'error': 'Método no reconocido.'}
            
            except Exception as e:
                context = {'form': form, 'error': str(e)}
            
            return render(request, 'calculadora/resultados.html', context)
    else:
        form = FuncionForm()
    return render(request, 'calculadora/index.html', {'form': form})

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generar_pdf(request):
    if request.method == "POST":
        iteraciones = eval(request.POST['iteraciones'])  # ⚠️ Solo si los datos son confiables
        raiz = request.POST['raiz']
        metodo = request.POST['metodo']
        
        template = get_template("calculadora/pdf_template.html")
        html = template.render({"iteraciones": iteraciones, "raiz": raiz, "metodo": metodo})
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resultado.pdf"'
        
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse("Error al generar PDF")
        return response
