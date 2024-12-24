###### DNN



###### training a DNN
- basically determining the optimal weights for the neuron!!
- Each neuron in a layer receives connections from all neurons in the previous layer.

Weights per Layer:

- Each neuron in a layer receives connections from all neurons in the previous layer.   
In your example, if we assume each hidden layer has 3 neurons:
- The first layer has 3 neurons, each with 64 weights connecting to the input.
- The second layer has 3 neurons, each with 3 weights connecting to the first layer.
- This pattern continues for all 7 layers.

Let's assume a simplified network with 3 neurons in each layer:

Layer 1: 3 neurons * 64 inputs = 192 weights
Layer 2: 3 neurons * 3 neurons (from Layer 1) = 9 weights
Layer 3: 3 neurons * 3 neurons (from Layer 2) = 9 weights
... and so on for all 7 layers


Training Process:

- The core of training involves adjusting these initial weights.   
- The network processes data, makes predictions, and calculates the error between its predictions and the actual target values.   
- Backpropagation is a key algorithm that calculates how much each weight contributes to the error.   
- Based on these calculations, the weights are gradually updated using optimization algorithms like gradient descent.

*The goal of training is to find the optimal set of weights that minimize the error and enable the network to make accurate predictions on new, unseen data.*

```
layers = nn.Sequential(
            nn.Linear(input_size, hidden_size1),
            nn.ReLU(),
            nn.Linear(hidden_size1, hidden_size2),
            nn.ReLU(),
            nn.Linear(hidden_size2, hidden_size3),
            nn.ReLU(),
            nn.Linear(hidden_size3, num_classes),
        )

        # nn.Linear(input_size, hidden_size1) : input layer which determines the weights for the first hidden layer neurons!
        # nn.ReLU() : activation function
        # nn.Linear(hidden_size1, hidden_size2) : hidden layer which determines the weights for the second hidden layer neurons!

```