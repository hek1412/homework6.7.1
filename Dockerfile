FROM tensorflow/tensorflow:2.10.0

WORKDIR /app

COPY mnist_model.py /app/mnist_model.py

CMD ["python", "/app/mnist_model.py"]