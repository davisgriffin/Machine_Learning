package.path = './Final/?.lua;' .. package.path -- .. concatenates
package.path = 'C:/Program Files/LuaRocks/rocks/share/lua/5.4/?.lua;' .. package.path
local inspect = require('inspect')

local function get_dimensions(tbl)
   assert(type(tbl) == "table", "Parameter 'tbl' must be a table")
   local sizes = { #tbl }
   local temp_table = tbl[1]
   while type(temp_table) == "table" do
      table.insert(sizes, #temp_table)
      temp_table = temp_table[1]
   end
   return sizes
end

local clf = require('multi_layer_perceptron_classifier')

clf:init({ hidden_layer_sizes = { 3, } })
-- clf:initialize({1, 2, 3}, clf.hidden_layer_sizes)

clf:fit({ { 1, 2, 3 } }, { 1 })

print(table.unpack(get_dimensions(clf.weights)))

print(inspect(get_dimensions(clf.weights[1])))
print(inspect(get_dimensions(clf.weights[2])))
print()
print()
print(inspect(clf.weights[1]))
print()
print(inspect(clf.weights[2]))
