import numpy as np
import pandas as pd

Data = pd.read_excel("Conjunto_datos_tarea2.xlsx")

MedianI = Data["Inicial"].median()
MedianC1 = Data["Primer_cambio"].median()
MedianC2 = Data["Segundo_cambio"].median()

print(MedianI)
print(MedianC1)
print(MedianC2)