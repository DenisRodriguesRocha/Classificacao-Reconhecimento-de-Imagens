# Importando as bibliotecas necessárias
import tensorflow as tf
from keras import datasets, layers, models
import matplotlib.pyplot as plt

# Baixando e preparando o dataset CIFAR10
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalizando os valores dos pixels para estarem entre 0 e 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Construindo o modelo de convolução
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))

# Adicionando camadas densas em cima
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10))

# Compilando e treinando o modelo
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

history = model.fit(
    train_images, train_labels, epochs=10, validation_data=(test_images, test_labels)
)

# Obtendo as métricas de acurácia do histórico
train_accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]

# Imprimindo as métricas de acurácia ao longo das epochs
for epoch in range(len(train_accuracy)):
    print("Epoch", epoch + 1)
    print("Acuracia de treinamento:", train_accuracy[epoch])
    print("Acuracia de validacao:", val_accuracy[epoch])
    print("--------------------------")
