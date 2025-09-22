## Image Classification

In this project, labeled input image dataset is fed into a fine-tuned EfficientNet-B4 neural network with cross entropy loss function, softmax activation function and Adam optimizer. The baseline EfficientNet-B4 model is fine-tuned in the classifier layer (i.e. the last layer) to solve a multi-class classification problem. The output from softmax activation function is a probability of each input image belonging to a specific class. In the project, two classes are considered and prediction or inference from the trained model will output a predicted image class probability. The fine-tuned EfficientNet-B4 neural network in this project can be used to train other labeled image datasets.

Image classification is a fundamental task in computer vision followed by image (object) localization, object detection and image segmentation tasks. Refer to projects on object localization and image segmentation in the same repo for more details on those computer vision tasks.

### References

[1] PyTorch Image Model Library for Deep Learning: https://timm.fast.ai

[2] EfficientNet DL Architecture: [a] https://docs.pytorch.org/vision/main/models/generated/torchvision.models.efficientnet_b0.html [b] https://pprp.github.io/timm/models/efficientnet [c] https://arxiv.org/pdf/1905.11946

[3] PyTorch torchvision Library for Computer Vision: https://docs.pytorch.org/vision/stable/index.html

[4] PyTorch Summary for Models: https://pypi.org/project/torch-summary/

[5] PyTorch DataLoader to Wrap Iterable Around the Dataset: https://docs.pytorch.org/docs/stable/data.html

[6] NumPy - Fundamental Package for Scientific Computing in Python: https://numpy.org

[7] Matplotlib - Visualization with Python: https://matplotlib.org

[8] IPython/Jupyter Notebook Progress Bar Decorator for Iterators: https://tqdm.github.io/docs/notebook/

## Citation

Please note that the code and technical details made available are for educational purposes only. The repo is not open for collaboration.

If you happen to use the code from this repo, please use the below citation to cite. Thank you!

balarcode (2025). *GitHub - balarcode/deep-learning: Practical implementation of selected algorithms, concepts and techniques in deep learning applied to various technologies and applications.* GitHub. https://github.com/balarcode/deep-learning

## Copyright

<a href="https://github.com/balarcode/deep-learning">Deep Learning</a> © 2025 by <a href="https://github.com/balarcode">balarcode</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
