import sympy as sp
import numpy as np

def biseccion(f, a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo [a,b].")
    iteraciones = []
    for i in range(1, max_iter+1):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a)/2
        iteraciones.append({"Iteración": i, "a": a, "b": b, "c": c, "f(c)": fc, "Error": error})
        if abs(fc) == 0 or error < tol:
            break
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return iteraciones, c

def newton_raphson(f, df, x0, tol, max_iter):
    iteraciones = []
    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivada nula en iteración {}".format(i))
        x_new = x - fx/dfx
        error = abs(x_new - x)
        iteraciones.append({"Iteración": i, "x": x, "f(x)": fx, "df(x)": dfx, "x_new": x_new, "Error": error})
        if error < tol:
            x = x_new
            break
        x = x_new
    return iteraciones, x

def newton_raphson_modificado(f, ddf, df, x0, tol, max_iter):
    iteraciones = []
    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        ddfx = ddf(x)
        denominador = dfx**2 - fx*ddfx
        if denominador == 0:
            raise ZeroDivisionError("División por cero en iteración {}".format(i))
        x_new = x - (fx * dfx) / denominador
        error = abs(x_new - x)
        iteraciones.append({"Iteración": i, "x": x, "f(x)": fx, "df(x)": dfx, "ddf(x)": ddfx, "x_new": x_new, "Error": error})
        if error < tol:
            x = x_new
            break
        x = x_new
    return iteraciones, x
