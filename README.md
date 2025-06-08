# Calculadora de Raíces Polinómicas en Django
# 📐 Calculadora de Raíces Polinómicas con Django

Este proyecto implementa una **aplicación web desarrollada en Django** que permite calcular la(s) raíz(ces) de un polinomio utilizando tres métodos numéricos clásicos:

- Método de Bisección
- Método de Newton-Raphson
- Método de Newton-Raphson Modificado

---

## 🎯 Objetivo del Proyecto

Desarrollar una herramienta interactiva y educativa que permita a los usuarios ingresar funciones polinómicas, seleccionar un método de resolución y visualizar el proceso iterativo completo junto con la raíz aproximada. El sistema también genera una **tabla detallada de iteraciones** y permite **exportar los resultados en PDF**.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Django
- **Frontend:** HTML, CSS
- **Librerías:** SymPy (para derivación y evaluación simbólica)
- **Otras:** Matplotlib o Plotly (opcional para gráficas), NumPy

---

## 🚀 Instalación y Ejecución

1. Clona este repositorio o descarga el ZIP.
2. Abre la terminal y ve a la carpeta del proyecto:

   ```bash
   cd /ruta/a/raices-polinomicas
   
3. Crea y activa un entorno virtual:
python -m venv env
env\Scripts\activate      # En Windows
source env/bin/activate   # En Linux/macOS

4. Instala las dependencias:
   pip install -r requirements.txt
   
6. Ejecuta el servidor:
   python manage.py runserver

7. http://127.0.0.1:8000

---

##   ✅ Funcionalidades
Ingreso de función polinómica vía formulario.

- **Selección del método numérico a aplicar.**

- **Parámetros dinámicos según el método elegido:**

- **a, b, tolerancia y número de iteraciones para Bisección.**

- **x₀, tolerancia y número de iteraciones para Newton-Raphson.**

- **Tabla de resultados iterativos.**

- **Cálculo del error relativo.**

- **Exportación de resultados a PDF.**

- **Validación de entrada del usuario y gestión de errores comunes.**

📚 Créditos
Desarrollado por: Freyder José Sequén Urlao
Curso: Métodos Numéricos
Universidad Mariano Gálvez de Guatemala – 2025

