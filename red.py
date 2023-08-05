import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Clase para crear la red neuronal
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Inicialización de los pesos sinápticos
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, X):
        # Propagación hacia adelante

        # Capa oculta
        self.z2 = np.dot(X, self.W1)
        self.a2 = sigmoid(self.z2)

        # Capa de salida
        self.z3 = np.dot(self.a2, self.W2)
        y_hat = sigmoid(self.z3)

        return y_hat

    def backward(self, X, y, y_hat, learning_rate):
        # Propagación hacia atrás

        # Cálculo del error
        delta3 = (y_hat - y) * sigmoid_derivative(self.z3)

        # Cálculo del gradiente para W2
        dW2 = np.dot(self.a2.T, delta3)

        # Cálculo del error en la capa oculta
        delta2 = np.dot(delta3, self.W2.T) * sigmoid_derivative(self.z2)

        # Cálculo del gradiente para W1
        dW1 = np.dot(X.T, delta2)

        # Actualización de los pesos sinápticos
        self.W1 -= learning_rate * dW1
        self.W2 -= learning_rate * dW2

    def train(self, X, y, learning_rate, epochs):
        for i in range(epochs):
            # Propagación hacia adelante
            y_hat = self.forward(X)

            # Propagación hacia atrás y actualización de pesos
            self.backward(X, y, y_hat, learning_rate)

    def predict(self, X):
        # Hacer predicciones
        y_hat = self.forward(X)
        return y_hat

# Función derivada de la sigmoide
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Ejemplo de uso
X = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 0, 1]])  # Ejemplos de entrada
y = np.array([[0], [1], [1], [0]])  # Ejemplos de salida esperada

# Crear una instancia de la red neuronal
nn = NeuralNetwork(3, 4, 1)

# Entrenar la red neuronal
nn.train(X, y, learning_rate=0.1, epochs=1000)

# Hacer predicciones
y_pred = nn.predict(X)
print(y_pred)
