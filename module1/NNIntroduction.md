###### Introduction

Rooted since 1940
Pioeneers
    Geoffrey Hinton
    John Hopfield
    Yoshua Bengio
ML learning from examples

###### History
nearly 80-year history of deep learning.
- 1943 - McCulloch & Pitts: Physiological Calculus of Neurons
    - Basic neuron, and connections between neurons, based on a biology-inspired model.
    - Weighting (wi), thresholding (θ), and inhibiting (zj) mechanisms that enable computation of many different logical functions.
- 1949 – Hebb: Hebbian Learning Rule
    - Concept of an associative memory with weights between neurons that strengthen based on co-stimulus (positive correlation).
    - Unsupervised learning: Stimuli and local learning rule produce associative memory between those stimuli.
    -  if the ring of a bell accompanies the serving of food, there will a strong weight between nodes representing "bell ring" and "food." Repeated simultaneous exposure to these stimuli enable the network to learn this association. Later, if the "bell ring" stimulus is seen, then there will a strong associated memory for "food" based on that strong weight.
- 1958 Rosenblatt: Perceptron
    - Biology-inspired “Perceptron” structure, combined with algorithm to learn weights for linear classification.
Demonstrated supervised training method on IBM 704 computer and specialized hardware in early 1960s.
- 1969 – Minsky & Papert: Limits of Single Layer Perceptron
    - A single-layer perceptron cannot classify XOR (and other data that is not linearly separable).
- Late 1960s to early 1970s – Multilayer Perceptrons (with Hidden Layers)
    - Various neural network architectures were explored in the 1960s and 1970s, though funding was scarcer due to the "AI Winter." Innovations include the advent of the multilayer perception (MLP), which have a number of important key ideas and discoveries:
    - Go beyond the single layer perceptron by adding one or more "hidden" layers with some number of hidden nodes
    - Consider other nonlinearities functions f(·) besides the "on-off" threshold, such as sigmoid, tanh, and ReLU
    - Universal approximation property: With enough nodes in one hidden layer (two-layer network), one can approximate any bounded continuous function with arbitrary accuracy.
- 1974 – Werbos: Backpropagation for NN Learning
    - Werbos (1974) suggests backpropagation for NN training.
- 1980 – Fukushima: Convolutional Neural Networks (CNN) in Neocognitron
    - Proposes multiple convolution layers combined with downsampling layers, for vision recognition tasks.
    - Hand-designs, and in some cases trains, individual layers to learn particular kinds of features, e.g., curves and components of handwritten digits.
- 2009 - Fei Fei Li: ImageNet Labeled Dataset
    - Contributes a large database with 3.2 million labeled images across 5247 synsets.
    - Sparks competition to create better and better classification models.
    - The three main barriers to deep learning during the "Second AI Winter" were inefficient training, insufficient data, and too-weak computers. A major advance that accompanied the internet age was the growing availability of large amounts of data, particularly textual and image-based. However, substantial work was still needed to "label" that data (i.e., associate a class name with what an image is depicting). The ImageNet dataset contributed a large, publicly-available labeled dataset —marking an important milestone toward overcoming this barrier to deep learning.
    
- 2012 - Krizhevky et al.: AlexNet Deep Neural Network (DNN) with ReLU and Dropout
    - Top the field of submissions on ImageNet 2012 competition top-5 error rate by 10.8% (to 16%).
    - Key enablers:
        - ReLUs as non-saturating neuron activation functions.
        - “Dropout” regularization in fully connected layers: randomly resets neuron output to 0.
        - The mapping of the problem onto GPU (graphical processing unit) hardware, enables training of the large network, and launches ubiquitous use of GPUs in deep learning.
- 2016 - He: ResNet-50 DNN with Residual Connections
    - Deep neural network (DNN): 50 layers for ResNet-50.
    - Addresses vanishing gradient problem with deep networks by using residual connections that enable more efficient learning of difference/residual functions.
    - Breaks the record on ImageNet: Top-5 error of 3.57%.
With the ready availability of labeled data and powerful GPU-based computation, a steady succession of new deep learning architectures, training enhancements, and related innovations begins to flow. The era of Deep Learning blooms.





Machine learning seeks to apply algorithms in software applications in order to predict certain outcomes. It also uses historical data to increase the accuracy of those predictions. There are three main machine learning categories:
- Supervised learning
- Unsupervised learning
- Semi-supervised learning
Deep learning generally falls under the categories of supervised and unsupervised learning. `Deep learning` is a type of machine learning that enables computers to learn and understand a set of concepts and improve that understanding over time. These computers are provided with simple concepts that allow them to make sense of more complex situations.

Research on artificial neural networks was motivated by the observation that human intelligence emerges from highly parallel networks by adjusting the strengths of their connections. 

Linear classifiers
Logistic classifiers
    - an algorithm that directly assigns class labels to instances based on the output of a logistic regression model.
    - applies a threshold to the predicted probability to make a categorical decision.
Deep Neual networks