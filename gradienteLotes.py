import os
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

os.chdir('datos')
datos = pd.read_csv("tirosL.csv")

datos=shuffle(datos.iloc[0:50000])
#clases
Y=datos.iloc[:,7].values
#caracteristicas
X=datos.iloc[:,0:7].values

# Re-etiquetar las clase de cada vector ejemplo en [-1,1]
yAd = np.where(Y == 0, -1, 1)
# Normalizar los datos
xAd = (X - X.mean()) / X.std()
#datos para entrenamiento y prueba
train_x=xAd[:25000]
test_x=xAd[25000:]
train_y=yAd[:25000]
test_y=yAd[25000:]
# Tasa de aprendizaje
eta=0.01


##ADALINE
# Número de iteraciones
niter = 200

# Vector de pesos inicial
w = np.zeros(train_x.shape[1] + 1)

# Number of misclassifications
errors = []

# Entrenamiento
for i in range(niter):
    output = np.dot(train_x, w[1:]) + w[0]
    errors = train_y - output
    w[1:] += eta * train_x.T.dot(errors)
    w[0] += eta * errors.sum()

# Prueba
errores = 0
for xi, target in zip(test_x, test_y) :
    activation = np.dot(xi, w[1:]) + w[0]
    output = np.where(activation >= 0.0, 1, -1)
    if (target != output) :
        errores += 1
print("{} vectores mal clasificados de {} ({}%)".format(errores, len(test_x), 
                                                        errores/len(test_x)*100))


