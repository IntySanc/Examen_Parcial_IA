from sklearn.linear_model import LinearRegression
from os import system as system

#Datos de entrenamiento
X_train = [[1],[2],[3],[4],[5],[6],[7],[8]]

#Etiquetas
y_train = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

#Crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(X_train, y_train)

#Limpiar Consola
system("cls")
#Pedir valores en Kilometros
km = int(input("Ingrese Valor en Km: "))

#Realizar predicciones
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#Imprimir resultado
print(f"{km} kilometros equivalen a {predicted_m[0]} metros")