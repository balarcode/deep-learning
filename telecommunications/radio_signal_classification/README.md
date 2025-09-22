## Radio Signal Classification

In this project, an input spectrogram of a radio signal is fed to EfficientNet (a Convolutional Neural Network (CNN) architecture) particularly EfficientNet-B0 which is the baseline model to perform radio signal classification. The input spectrogram is formed by applying Short-Time Fourier transform (STFT) to the segmented IQ sequences. Window functions such as Kaisar-Bessel window, Hamming window or Rectangular window can be used to perform STFT. The spectrogram represented as a 3D tensor along with a ground truth label is used to train and validate the model prior to using it for inference or prediction on real-world dataset. As an example, radio signals such as narrow band radio signals (consisting of two variants), a squiggle radio signal and a noisy signal are used to train and validate the classification model in this project.

A squiggle radio signal could be AM or FM signal whose complex envelope looks like a squiggle OR an interference/noise contributing to an undefined squiggle radio signal.

### References

[1] PyTorch Image Model Library for Deep Learning: https://timm.fast.ai

[2] EfficientNet DL Architecture: [a] https://docs.pytorch.org/vision/main/models/generated/torchvision.models.efficientnet_b0.html [b] https://pprp.github.io/timm/models/efficientnet [c] https://arxiv.org/pdf/1905.11946

## Citation

Please note that the code and technical details made available are for educational purposes only. The repo is not open for collaboration.

If you happen to use the code from this repo, please use the below citation to cite. Thank you!

balarcode (2025). *GitHub - balarcode/deep-learning: Practical implementation of selected algorithms, concepts and techniques in deep learning applied to various technologies and applications.* GitHub. https://github.com/balarcode/deep-learning

## Copyright

<a href="https://github.com/balarcode/deep-learning">Deep Learning</a> © 2025 by <a href="https://github.com/balarcode">balarcode</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
