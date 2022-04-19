package.path = './?.lua;' .. package.path -- .. concatenates
local inspect = require('inspect')

local function dump(o)
   if type(o) == 'table' then
      local s = '{\n\t'
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

local clf = require('multi_layer_perceptron_classifier')

clf:init({hidden_layer_sizes = {3,}})
-- clf:initialize({1, 2, 3}, clf.hidden_layer_sizes)

clf:fit({1, 2, 3}, {1})

print(inspect(clf.weights))