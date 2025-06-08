##
📐 Calculadora de Raíces Polinómicas en Django
🧮 Descripción General
La Calculadora de Raíces Polinómicas es una aplicación web desarrollada con el framework Django que tiene como finalidad resolver ecuaciones polinómicas mediante métodos numéricos clásicos, ampliamente utilizados en ingeniería y ciencias aplicadas. Su diseño está enfocado en ser una herramienta educativa, interactiva y de fácil acceso que permita comprender el comportamiento y convergencia de los distintos métodos iterativos para encontrar raíces reales de funciones polinómicas.
##
🔢 Métodos Implementados
Método de Bisección: Basado en el teorema del valor intermedio, divide iterativamente el intervalo hasta aproximar una raíz.

Método de Newton-Raphson: Utiliza la derivada de la función para aproximar la raíz con mayor velocidad, ideal cuando se cuenta con una buena estimación inicial.

Método de Newton-Raphson Modificado: Variante del anterior que mejora la estabilidad de la convergencia en algunos casos particulares.
##
🎯 Objetivo del Proyecto
Diseñar e implementar una plataforma web funcional y educativa que permita a los usuarios:

Ingresar funciones polinómicas personalizadas.

Seleccionar el método numérico deseado.

Introducir los parámetros específicos requeridos para cada método.

Visualizar el proceso iterativo completo a través de una tabla detallada.

Obtener la raíz aproximada de forma clara y estructurada.

Descargar los resultados generados en formato PDF para su documentación o análisis posterior.

El sistema también se encarga de realizar la validación de datos y la gestión de errores comunes para garantizar una experiencia fluida y confiable.
##
🛠️ Tecnologías Utilizadas
Componente	Tecnología
Backend	Python 3.10+, Django Framework
Frontend	HTML5, CSS3, Bootstrap (opcional)
Librerías	- SymPy: para derivación y evaluación simbólica
- NumPy: cálculos numéricos
- ReportLab o xhtml2pdf: generación de PDF
- Matplotlib o Plotly (opcional): visualización gráfica
Entorno	Virtualenv para la gestión del entorno Python
##
🚀 Instalación y Ejecución
1. Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/usuario/raices-polinomicas.git
O descargar el archivo .zip del proyecto y descomprimirlo.

2. Acceder al directorio del proyecto
bash
Copiar
Editar
cd raices-polinomicas
3. Crear y activar el entorno virtual
En Windows:

bash
Copiar
Editar
python -m venv env
env\Scripts\activate
En Linux/macOS:

bash
Copiar
Editar
python3 -m venv env
source env/bin/activate
4. Instalar dependencias
bash
Copiar
Editar
pip install -r requisitos.txt
5. Ejecutar el servidor de desarrollo
bash
Copiar
Editar
python manage.py runserver
Luego, abre tu navegador en http://127.0.0.1:8000
##
✅ Funcionalidades Principales
📥 Formulario amigable para ingresar funciones polinómicas.

🔘 Selección dinámica de métodos numéricos.

⚙️ Parámetros configurables por método:

Bisección: Intervalo [a, b], tolerancia, número máximo de iteraciones.

Newton-Raphson (simple y modificado): Valor inicial x₀, tolerancia, número de iteraciones.

📊 Generación de tabla detallada con iteraciones paso a paso.

📉 Cálculo de errores relativos y convergencia del método.

📄 Exportación de resultados a PDF, con formato limpio y ordenado.

🔐 Validación de entradas y manejo de errores para evitar bloqueos o mal funcionamiento.

📚 Créditos y Reconocimiento
Autor: Freyder José Sequén Urlao
Curso: Métodos Numéricos
Universidad: Universidad Mariano Gálvez de Guatemala
Año: 2025

Proyecto realizado con fines educativos para reforzar el aprendizaje de métodos numéricos aplicados a la resolución de polinomios reales.


