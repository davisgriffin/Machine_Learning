require('os')
require('math')

local function _normalized_init(layer_size, next_layer_size)
    return math.sqrt(6.0 / (layer_size + next_layer_size))
end

local function _initialize_wb(layer_size, next_layer_size)
    local bound = _normalized_init(layer_size, next_layer_size)
    local weights = {}
    local biases = {}

    for i = 1, layer_size do
        weights[i] = {}
        for j = 1, next_layer_size do
            weights[i][j] = math.random(-1, 1) * bound
        end
    end
    for i = 1, next_layer_size do
        biases[i] = math.random(-1, 1) * bound
    end

    return weights, biases
end

local function _initialize(self, y, layer_sizes)
    self.num_outputs = #y
    self.num_layers = #layer_sizes

    self.weights = {}
    self.biases = {}
    for i = 1, self.num_layers - 1 do
        local weight_init, bias_init = _initialize_wb(
            layer_sizes[i], layer_sizes[i+1]
        )
        table.insert(self.weights, weight_init)
        table.insert(self.biases, bias_init)
    end
end

local function _check_random_state(self)
    -- TODO: Ensure we can seed train test split with random state later
    if self.random_state == nil then
        math.randomseed(os.time())
        return math.random()
    end
    return self.random_state
end

local MLPClassifier = {}

function MLPClassifier:init(args)
    self.hidden_layer_sizes = args.hidden_layer_sizes or {100,}
    self.learning_rate = args.learning_rate or 0.001
    self.max_iterations = args.max_iterations or 200
    self.random_state = args.random_state or nil
    self.activation = args.activation or 'relu'
    self.loss = args.loss or 'log_loss'
end

function MLPClassifier:fit(X, y)
    local layer_sizes = {#X, table.unpack(self.hidden_layer_sizes), 1}
    self._random_state = _check_random_state(self)

    if self['weights'] == nil then
        _initialize(self, y, layer_sizes)
    end
end

return MLPClassifier