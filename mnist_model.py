import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Загрузка и подготовка данных MNIST
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Определение модели
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Тренировка модели
model.fit(train_images, train_labels, epochs=10, batch_size=32)

# Сохранение модели
model.save('/results/mnist_model.keras')