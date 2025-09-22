## Handwritten Digit Recognition using a Neural Network

Handwritten digit recognition is a multiclass classification problem in machine learning. The objective is to detect the handwritten numbers 0 to 9 from the input images obtained via scans or photography. Handwritten digit recognition problem can be solved using a deep neural network by using a softmax regression algorithm to generate output probabilities for all possible numbers 0 through 9 and then choosing the probability that is close to 1.0 in order to successfully classify or detect the handwritten digit as one of 0 through 9.

In this project, a labeled dataset is considered as a training dataset in order to build a sequential model in the neural network. The neural network is architected to include two hidden layers with ReLU activation and one output layer with linear activation.

For the given dataset of size = N x D, "N" is the number of data points or training examples in the dataset and "D" is the dimension of the data point in the dataset. For the handwritten digit recognition problem, the dimension of the dataset will be sqrt(D) pixels X sqrt(D) pixels for each of the images in the dataset.

### Training Dataset with Labels

![Training Dataset](results/labeled_data.png)

### Label v/s Prediction (yhat) of Handwritten Digit Recognition Model using a Neural Network

![Model Prediction](results/prediction.png)

### Cost v/s Epoch for the Neural Network

![Cost](results/cost.png)

### References

[1] Keras Sequential Model: https://keras.io/guides/sequential_model/

[2] TensorFlow API for Python: https://www.tensorflow.org/api_docs/python/tf

## Citation

Please note that the code and technical details made available are for educational purposes only. The repo is not open for collaboration.

If you happen to use the code from this repo, please use the below citation to cite. Thank you!

balarcode (2025). *GitHub - balarcode/deep-learning: Practical implementation of selected algorithms, concepts and techniques in deep learning applied to various technologies and applications.* GitHub. https://github.com/balarcode/deep-learning

## Copyright

<a href="https://github.com/balarcode/deep-learning">Deep Learning</a> © 2025 by <a href="https://github.com/balarcode">balarcode</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
