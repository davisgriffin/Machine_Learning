import numpy as np
from scipy.special import xlogy

class BaseMultilayerPerceptron:
    def __init__(
        self,
        hidden_layer_sizes,
        learning_rate,
        epochs,
        random_state,
        activation,
        loss
    ):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.random_state = random_state
        self.activation = activation
        self.loss = loss
        # NOTE Incorporate member dictionaries over getter functions?

    def _initialize(self, y, layer_units):
        self.num_outputs = y.shape[1]
        self.num_layers = len(layer_units)

        self.coefs = []
        self.intercepts = []
        for i in range(self.num_layers - 1):
            coef_init, intercept_init = self._init_coef(
                layer_units[i], layer_units[i + 1]
            )
            self.coefs.append(coef_init)
            self.intercepts.append(intercept_init)

    def _init_coefs(self, layer_size, next_layer_size):
        # initialize weights and bias using normalized initialization
        bound = self._normalized_init(layer_size, next_layer_size)

        coefs = self._random_state.uniform(
            -bound, bound, (layer_size, next_layer_size)
        )
        intercepts = self._random_state.uniform(
            -bound, bound, next_layer_size
        )
        return coefs, intercepts

    def _fit(self, X, y):
        hidden_layer_sizes = list(self.hidden_layer_sizes)
        bool_input = not hasattr(self, "coefs")
        self.num_outputs = y.shape[1]
        
        num_samples , num_features = X.shape
        layer_sizes = [num_features] + hidden_layer_sizes + [self.num_outputs]
        self._random_state = self._check_random_state(self.random_state)

        X, y = self._get_np_array(X, y)
        if bool_input: self._initialize(y, layer_sizes)

        # prep forward/back propogation
        # populate later layers with None/empty
        activations = [X] + [None] * (len(layer_sizes) - 1)
        slopes = [None] * (len(activations) - 1)

        grad_coefs = [
            np.empty((layer_in, layer_out), dtype=X.dtype)
            for layer_in, layer_out in zip(layer_sizes[:-1], layer_sizes[1:])
        ]
        grad_intercepts = [
            np.empty(n_fan_out_, dtype=X.dtype) for n_fan_out_ in layer_sizes[1:]
        ]

        batch = min(200, num_samples)
        # for it in self.epochs:



    def _forward_prop(self, layer_activations):
        activation = self._get_activation(self.activation)
        
        for i in range(self.num_layers - 1):
            # layer_activation = sigmoid(dot(X, weight) + bias)
            layer_activations[i + 1] = np.dot(layer_activations[i], self.coefs[i])
            layer_activations[i + 1] += self.intercepts[i]
            activation(layer_activations[i + 1]) # sigmoid
        return layer_activations

    def _grad_loss(
        self, layer, num_samples, activations, slopes, grad_coefs, grad_intercepts
    ):
        # NOTE add alpha?
        grad_coefs[layer] = np.dot(activations[layer].T, slopes[layer])/num_samples
        grad_intercepts[layer] = np.mean(slopes[layer], 0)

    def _back_prop(self, X, y, activations, slopes, grad_coefs, grad_intercepts):
        activations = self._forward_prop(activations)
        # NOTE add L2 regularization?
        # take last activation layer (output) and calculate loss
        last_layer = self.num_layers - 2
        samples = X.shape[0]

        loss = self._get_loss_function(self.loss)(y, activations[-1])
        slopes[last_layer] = activations[-1] - y

        self._grad_loss(
            last_layer, samples, activations, slopes, grad_coefs, grad_intercepts
        )

        prime_activation = self._get_activation_prime(self.activation)
        for i in range(last_layer, 0, -1):
            slopes[i - 1] = np.dot(slopes[i], self.coefs[i].T)
            prime_activation(activations[i], slopes[i - 1])

            self._grad_loss(
                i - 1, samples, activations, slopes, grad_coefs, grad_intercepts
            )
        
        return loss, grad_coefs, grad_intercepts

    def _get_np_array(self, X, y):
        if isinstance(X, np.ndarray) and isinstance(y, np.ndarray):
            return X, y
        if not hasattr(X, "__iter__"):
            X = [X]
        if not hasattr(y, "__iter__"):
            y = [y]
        X = np.array(list(X))
        y = np.array(list(y))
        return X, y

    def _check_random_state(self, random_state):
        if random_state is None:
            return np.random.mtrand._rand
        if not isinstance(random_state, np.random.RandomState):
            return np.random.RandomState(random_state)
        if isinstance(random_state, np.random.RandomState):
            return random_state

    def _get_activation(self, activation):
        if activation == "sigmoid": return self._sigmoid
        elif activation == "tanh": return self._tanh
        elif activation == "normalized": return self._normalized_init

    def _get_activation_prime(self, activation):
        if activation == "sigmoid": return self._sigmoid_prime
        elif activation == "tanh": return self._tanh_prime
        elif activation == "normalized": return self._normalized_init_prime

    def _get_loss_function(self, loss):
        if loss == "squared_error": return self._MSE
        if loss == "log_loss": return self._log_loss
        if loss == "binary_log_loss": return self._b_log_loss

    def _normalized_init(self, layer_size, next_layer_size):
        # 'normalized initialization' from Glorot and Bengio
        return np.sqrt(6.0 / (layer_size + next_layer_size))

    def _normalized_init_prime(self, x):
        raise NotImplementedError

    def _sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))

    def _sigmoid_prime(self, x):
        return self._sigmoid(x)*(1.0-self._sigmoid(x))

    def _tanh(self, x):
        return np.tanh(x)

    def _tanh_prime(self, x):
        return 1.0 - x**2

    # NOTE look at the y passed in, as the training set could be thousands
    # NOTE long while we really only want the length of the output layer
    def _MSE(self, y, pred):
        return ((y - pred)**2).mean() / 2

    def _log_loss(self, y, pred):
        # NOTE may need to clip prediction to (0, 1) based on IEEE754
        return -xlogy(y, pred).sum() / pred.shape[0] # averaging log

    def _b_log_loss(self, y, pred):
        return (
            -(xlogy(y, pred).sum() + xlogy(1 - y, 1 - pred).sum())
            / pred.shape[0]
        )



class MultiLayerPerceptron(BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes=(100,),
        learning_rate=0.001,
        max_iter=200,
        random_state=None,
        activation='sigmoid',
        loss='log_loss'
    ):
        super().__init__(
            hidden_layer_sizes=hidden_layer_sizes,
            learning_rate=learning_rate,
            max_iter=max_iter,
            random_state=random_state,
            activation=activation,
            loss=loss
        )

    def fit(self, X, y):
        super()._fit(X, y)

    def predict(self, X):
        # super()._predict(X)
        raise NotImplementedError

    def score(self, X, y):
        if len(X) != len(y):
            raise Exception("Dimensions do not match")
        y_prime = self.predict(X)
        MSE = 0
        for i in range(len(y)):
            MSE += (y[i] - y_prime[i])**2
        return MSE