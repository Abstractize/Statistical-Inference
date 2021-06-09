from operator import le
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats as st

# Cargar datos y separar en muestras (de cada configuración)
df = pd.read_excel("Conjunto_datos_tarea2.xlsx")
data1 = df["Inicial"].to_numpy()
data2 = df["Primer_cambio"].to_numpy()
data3 = df["Segundo_cambio"].to_numpy()

# Calcular media muestral de cada configuración
mean1 = np.mean(data1)
mean2 = np.mean(data2)
mean3 = np.mean(data3)

print("\n*********** Calculo de promedios ***********")
print("Promedio de configuración Inicial: ", mean1)
print("Promedio de configuración Primer_cambio: ", mean2)
print("Promedio de configuración Segundo_cambio: ", mean3)

# Calcula la varianza muestral de cada configuración.
var1 = np.var(data1, ddof = 0)
var2 = np.var(data2, ddof = 0)
var3 = np.var(data3, ddof = 0)

print("\n*********** Calculo de varianza muestral ***********")
print("Varianza en configuracón Inicial: ", var1)
print("Varianza en configuración de Primer_cambio: ", var2)
print("Varianza en configuración de Segundo_cambio: ", var3)

# MLE analitico de deviacion estandard.
print("\n*********** Estimación MLE de varianza y desviación estándar poblacional por método analítico/teórico ***********")
std1MLE = np.std(data1)
std2MLE = np.std(data2)
std3MLE = np.std(data3)

print("\nEstimación de desviación estandar para configuración Inicial: ", std1MLE)
print("Estimación de varianza para configuración Inicial: ", math.pow(std1MLE, 2))

print("\nEstimación de desviación estandar para configuración Primer_cambio: ", std2MLE)
print("Estimación de varianza para configuración Primer_cambio: ", math.pow(std2MLE, 2))

print("\nEstimación de desviación estandar para configuración Segundo_cambio: ", std3MLE)
print("Estimación de varianza para configuración Segundo_cambio: ", math.pow(std3MLE, 2))

# MLE empírico de desviación estándar
print("\n*********** Estimación MLE de varianza y desviación estándar poblacional por método empirico/practico ***********")
#MLE Configuracion inicial
Dist1 = st.norm(loc = mean1, scale = math.sqrt(np.var(data1, ddof = 1)))
x = np.linspace(Dist1.ppf(0.001),
                Dist1.ppf(0.999), 100)
plt.hist(data1, density = True, label = "Muestra")
plt.title("Configuración inicial")
plt.xlabel("Porcentaje de rendimiento (%)")
plt.ylabel("Frecuencia relativa")
plt.plot(x, Dist1.pdf(x), "r-", label="PDF teorico")
plt.legend()
plt.show()

loc1, scale1 = st.norm.fit(data1, floc = mean1)
print("\nEstimación para la desvación estándar en la configuración Inicial: ", scale1)
print("Estimación Varianza para configuración Inicial: ", math.pow(scale1, 2))

#MLE Primer_cambio
Dist2 = st.norm(loc = mean2, scale = math.sqrt(np.var(data2, ddof = 1)))
x = np.linspace(Dist2.ppf(0.001),
                Dist2.ppf(0.999), 100)
plt.hist(data2, density = True, label = "Muestra")
plt.title("Configuración Primer_cambio")
plt.xlabel("Porcentaje de rendimiento (%)")
plt.ylabel("Frecuencia relativa")
plt.plot(x, Dist2.pdf(x), "r-", label="PDF teorico")
plt.legend()
plt.show()

loc2, scale2 = st.norm.fit(data2, floc = mean2)
print("\nEstimación de la desvación en la configuración Primer_cambio: ", scale2)
print("Estimación de la Varianza en la configuración Primer_cambio: ", math.pow(scale2, 2))

#MLE Segundo_cambio
Dist3 = st.norm(loc = mean3, scale = math.sqrt(np.var(data3, ddof = 1)))
x = np.linspace(Dist3.ppf(0.001),
                Dist3.ppf(0.999), 100)
plt.hist(data3, density = True, label = "Muestra")
plt.title("Configuración Segundo_cambio")
plt.xlabel("Porcentaje de rendimiento (%)")
plt.ylabel("Frecuencia relativa")
plt.plot(x, Dist3.pdf(x), "r-", label="PDF teorico")
plt.legend()
plt.show()

loc3, scale3 = st.norm.fit(data3, floc = mean3)
print("\nEstimación para desvación estándar en la configuración Segundo_cambio: ", scale3)
print("Estimación de Varianza para configuración Segundo_cambio: ", math.pow(scale3, 2))

# Estimacion insesgada de varianza poblacional
print("\n********** Estimación insesgada de la varianza poblacional **********")
var1 = np.var(data1, ddof = 1)
var2 = np.var(data2, ddof = 1)
var3 = np.var(data3, ddof = 1)

print("Varianza en configuracón Inicial: ", var1)
print("Varianza en configuración de Primer_cambio: ", var2)
print("Varianza en configuración de Segundo_cambio: ", var3)

f1 = var1/var2
f2 = var1/var3
f3 = var2/var3
print("\nEstadisticos")
print("F1: {0}, F2: {1}, F3: {2}".format(f1, f2, f3))

alpha = 0.05
fdistribution = st.f(dfn = len(data1)-1, dfd = len(data2)-1)
f_critical1 = fdistribution.ppf(alpha/2)
f_critical2 = fdistribution.ppf(1 - alpha/2)

print("\n")
print("Valor izquierdo: {0}, Valor derecho: {1}".format(f_critical1, f_critical2))
if ((f1 > f_critical1)^(f1 < f_critical2)):
    print("var1 no igual a var2")
    if (f1 > f_critical1):
        print("f1 mayor que izquierdo")
    else:
        print("f1 menor que derecho")
else:
    print("var1 igual a var2")

if ((f2 > f_critical1)^(f2 < f_critical2)):
    print("var1 no igual a var3")
    if (f2 > f_critical1):
        print("f2 mayor que izquierdo")
    else:
        print("f2 menor que derecho")
else:
    print("var1 igual a var2")

if ((f3 > f_critical1)^(f3 < f_critical2)):
    print("var2 no igual a var3")
    if (f3 > f_critical1):
        print("f3 mayor que izquierdo")
    else:
        print("f3 menor que derecho")
else:
    print("var2 igual a var3")
