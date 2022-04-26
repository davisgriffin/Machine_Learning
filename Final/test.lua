package.path = './Final/?.lua;' .. package.path -- .. concatenates
package.path = 'C:/Program Files/LuaRocks/rocks/share/lua/5.4/?.lua;' .. package.path
local inspect = require('inspect')
local numlua = require('numlua')

local clf = require('multi_layer_perceptron_classifier')

clf:init({ hidden_layer_sizes = { 3, } })
-- clf:initialize({1, 2, 3}, clf.hidden_layer_sizes)

-- local activation = clf:fit({ { 1, 2, 3 } }, { 1 })

-- print(inspect(clf.biases))
-- print()
-- print(inspect(clf.weights))
-- print()
-- print(inspect(clf.weights[1]))
-- print()
-- print(inspect(clf.weights[2]))

-- print(inspect(activation))

print(table.unpack(numlua.get_dimensions({
   {
      { 1, 2, 3, 4 },
      { 1, 2, 3, 4 }
   },
   {
      { 1, 2, 3, 4 },
      { 1, 2, 3, 4 }
   },
   {
      { 1, 2, 3, 4 },
      { 1, 2, 3, 4 }
   },
})))

print(table.unpack(numlua.get_dimensions({
   { 1, 2, 3 }
})))
