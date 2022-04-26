package.path = './Final/?.lua;' .. package.path

require('os')
require('math')
local numlua = require('numlua')

local function _normalized_init(layer_size, next_layer_size)
    return math.sqrt(6.0 / (layer_size + next_layer_size))
end

local function _relu(z)
    local res = z
    return math.max(0, z)
end

local function _relu_prime(z)
    if z > 0 then return 1 else return 0 end
end

local function _sigmoid(z)
    return 1.0 / (1.0 + math.exp(-z))
end

local function _sigmoid_prime(z)
    return _sigmoid(z) * (1.0 - _sigmoid(z))
end

local function _tanh(z)
    return math.atan(z)
end

local function _tanh_prime(z)
    return 1.0 - z ^ 2
end

local function _MSE(y, pred)
    return numlua.mean(numlua.sub(y, pred) ^ 2) / 2
end

local function _log_loss(y, pred)
    return -numlua.sum(numlua.xlogy(y, pred)) / #pred
end

local function _b_log_loss(y, pred)
    return (numlua.sum(numlua.xlogy(y, pred)) +
        numlua.sum(numlua.xlogy(
            numlua.sub(1, y), numlua.sub(1, pred)
        ))) / #pred
end

local function _get_activation_function(activation)
    local activations = {
        sigmoid = _sigmoid,
        tanh = _tanh,
        relu = _relu
    }

    return activations[activation]
end

local function _get_loss_function(loss)
    local losses = {
        MSE = _MSE,
        log_loss = _log_loss,
        binary_log_loss = _b_log_loss
    }

    return losses[loss]
end

local function _check_random_state(self)
    if self.random_state == nil then
        return os.time()
    end
    return self.random_state
end

local function _initialize_wb(layer_size, next_layer_size)
    local bound = _normalized_init(layer_size, next_layer_size)
    local weights = {}
    local biases = {}

    for i = 1, layer_size do
        weights[i] = {}
        for j = 1, next_layer_size do
            weights[i][j] = -bound + math.random() * 2 * bound
        end
    end
    for i = 1, next_layer_size do
        biases[i] = -bound + math.random() * 2 * bound
    end

    return weights, biases
end

local function _initialize(self, y, layer_sizes)
    self.num_outputs = #y
    self.num_layers = #layer_sizes
    self._random_state = _check_random_state(self)
    math.randomseed(self._random_state)

    self.weights = {}
    self.biases = {}
    for i = 1, self.num_layers - 1 do
        local weight_init, bias_init = _initialize_wb(
            layer_sizes[i], layer_sizes[i + 1]
        )
        table.insert(self.weights, weight_init)
        table.insert(self.biases, bias_init)
    end
end

local function _initialize_activations(self, X, layer_sizes)
    local activations = { X, {} }
    for i = 1, #layer_sizes - 1 do
        table.insert(activations[2], {})
    end
    return activations
end

local function _feed_forward(self, layer_activations)
    local activation = _get_activation_function(self.activation)
    for i = 1, self.num_layers - 1 do
        local z = numlua.dot(layer_activations[i], self.weights[i])
        z = numlua.add(z, self.biases[i])
        layer_activations[i + 1] = activation(z)
    end
end

local function _backprop(self, X, y, layer_activations)
    _feed_forward(self, layer_activations)
end

local MLPClassifier = {}

function MLPClassifier:init(args)
    self.hidden_layer_sizes = args.hidden_layer_sizes or { 100, }
    self.learning_rate = args.learning_rate or 0.001
    self.max_iterations = args.max_iterations or 200
    self.random_state = args.random_state or nil
    self.activation = args.activation or 'relu'
    self.loss = args.loss or 'MSE'
end

function MLPClassifier:fit(X, y)
    assert(type(y[1]) ~= "table", "y must be 1-dimensional")
    local layer_sizes = {
        numlua.get_dimensions(X)[2],
        table.unpack(self.hidden_layer_sizes),
        numlua.get_dimensions(y)[1]
    }

    if self['weights'] == nil then
        _initialize(self, y, layer_sizes)
    end

    local activations = _initialize_activations(self, X, layer_sizes)
    _backprop(self, X, y, activations)
    return activations
end

return MLPClassifier
