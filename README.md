# 📐 Calculadora de Raíces Polinómicas en Django

## 🧮 Descripción General

La **Calculadora de Raíces Polinómicas** es una aplicación web desarrollada con el framework **Django** que permite resolver ecuaciones polinómicas utilizando **métodos numéricos clásicos**. Su objetivo principal es ser una herramienta **educativa e interactiva** para la comprensión de algoritmos iterativos de búsqueda de raíces reales.

### Métodos Implementados

- 🔹 **Método de Bisección**
- 🔹 **Método de Newton-Raphson**
- 🔹 **Método de Newton-Raphson Modificado**

---

## 🎯 Objetivo del Proyecto

Desarrollar una plataforma web intuitiva que permita:

- Ingresar funciones polinómicas.
- Seleccionar el método numérico a utilizar.
- Introducir parámetros específicos según el método.
- Visualizar paso a paso el proceso iterativo en una tabla.
- Obtener la raíz aproximada.
- Descargar los resultados en **PDF**.

Además, se implementa validación de entradas y manejo de errores para evitar inconsistencias.

---

## 🛠️ Tecnologías Utilizadas

| Componente      | Tecnología                                                                 |
|-----------------|----------------------------------------------------------------------------|
| **Backend**     | Python 3.10+, Django Framework                                              |
| **Frontend**    | HTML5, CSS3, Bootstrap (opcional)                                           |
| **Librerías**   | SymPy, NumPy, ReportLab/xhtml2pdf (para PDF), Matplotlib/Plotly (opcional) |
| **Entorno**     | Virtualenv para entorno Python aislado                                     |

---

## 🚀 Instalación y Ejecución

Sigue los siguientes pasos para instalar y ejecutar el proyecto en tu máquina local:

```bash
# 1. Clona el repositorio
git clone https://github.com/usuario/raices-polinomicas.git
cd raices-polinomicas

# 2. Crea y activa el entorno virtual

## En Windows
python -m venv env
env\Scripts\activate

## En Linux/macOS
python3 -m venv env
source env/bin/activate

# 3. Instala las dependencias
pip install -r requisitos.txt

# 4. Ejecuta el servidor de desarrollo
python manage.py runserver

# 5. Abre tu navegador y ve a:
http://127.0.0.1:8000
## ✅ Funcionalidades

- 📥 **Ingreso de funciones polinómicas** mediante un formulario web amigable.

- 🔘 **Selección del método numérico deseado**:  
  &nbsp;&nbsp;&nbsp;&nbsp;• Bisección  
  &nbsp;&nbsp;&nbsp;&nbsp;• Newton-Raphson  
  &nbsp;&nbsp;&nbsp;&nbsp;• Newton-Raphson Modificado

- ⚙️ **Parámetros configurables según el método**:  
  - **Bisección**: intervalo \[a, b\], tolerancia, número de iteraciones.  
  - **Newton-Raphson**: valor inicial x₀, tolerancia, número de iteraciones.

- 📊 **Tabla detallada de resultados** por cada iteración.

- 📉 **Cálculo del error relativo** en cada paso del proceso.

- 📄 **Exportación de resultados en formato PDF** con diseño limpio y profesional.

- ❌ **Gestión de errores comunes y validación** de entradas del usuario.

- 🌐 **Interfaz responsiva y simple**, ideal para fines educativos.

---

## 📚 Créditos

- **Autor**: Freyder José Sequén Urlao  
- **Curso**: Métodos Numéricos  
- **Proyecto académico de**: Universidad Mariano Gálvez de Guatemala  
- **Año**: 2025
