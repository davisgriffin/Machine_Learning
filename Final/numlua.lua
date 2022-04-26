require('math')

local numlua = {}

local function pack(vector)
    local packed_vector = {}
    for i = 1, #vector do
        packed_vector[i] = { vector[i] }
    end
    return packed_vector
end

function numlua.get_dimensions(tbl)
    assert(type(tbl) == "table", "Parameter 'tbl' must be a table")
    local sizes = { #tbl }
    local temp_table = tbl[1]
    while type(temp_table) == "table" do
        table.insert(sizes, #temp_table)
        temp_table = temp_table[1]
    end
    return sizes
end

function numlua.ones(size)
    for i = 1, #size do

    end
end

function numlua.vdot(a, b)
    assert(#a == #b, "vector dimensions must agree")
    local res = 0

    for i = 1, #a do
        res = res + a[i] * b[i]
    end

    return res
end

local function _dot(a, b)
    -- TODO: implement get_dimensions for 3d matrices
    assert(#a[1] == #b, "matrix dimensions must agree")
    local res = {}

    for i = 1, #a do
        res[i] = {}
        for j = 1, #b[1] do
            res[i][j] = 0
            for k = 1, #b do
                res[i][j] = res[i][j] + a[i][k] * b[k][j]
            end
        end
    end

    return res
end

function numlua.dot(a, b)
    if type(a[1]) == "number" and type(b[1]) == "number" then
        return numlua.vdot(a, b)
    elseif type(a[1]) == "number" then
        return _dot({ a }, b)
    elseif type(b[1]) == "number" then
        return _dot(a, pack(b))
    end

    return _dot(a, b)
end

function numlua.vadd(a, b)
    assert(#a == #b, "vector dimensions do not match")
    local res = {}
    for i = 1, #a do
        res[i] = a[i] + b[i]
    end
    return res
end

local function _add(a, b)
    -- TODO: implement get_dimensions for 3d matrices
    assert(#a == #b and #a[1] == #b[1], "matrix dimensions must agree")
    local res = {}
    for i = 1, #a do
        res[i] = {}
        for j = 1, #b[1] do
            res[i][j] = a[i][j] + b[i][j]
        end
    end
    return res
end

function numlua.add(a, b)
    if type(a[1]) == "number" and type(b[1]) == "number" then
        return numlua.vadd(a, b)
    elseif type(a[1]) == "number" then
        return _add({ a }, b)
    elseif type(b[1]) == "number" then
        return _add(a, { b })
    end

    return _add(a, b)
end

function numlua.vsub(a, b)
    assert(#a == #b, "vector dimensions do not match")
    local res = {}
    for i = 1, #a do
        res[i] = a[i] - b[i]
    end
    return res
end

local function _sub(a, b)
    -- TODO: implement get_dimensions for 3d matrices
    assert(#a == #b and #a[1] == #b[1], "matrix dimensions must agree")
    local res = {}
    for i = 1, #a do
        for j = 1, #b[1] do
            res[i][j] = a[i][j] - b[i][j]
        end
    end
    return res
end

local function _csub(a, b)

end

function numlua.sub(a, b)
    if type(a) == "number" then
        return _csub(a, b)
        -- elseif type(b) == "number" then
        --     return _cdot(_csub(b, a))
    elseif type(a[1]) == "number" and type(b[1]) == "number" then
        return numlua.vsub(a, b)
    elseif type(a[1]) == "number" then
        return _sub({ a }, b)
    elseif type(b[1]) == "number" then
        return _sub(a, { b })
    end

    return _sub(a, b)
end

function numlua.sum(a)
    -- TODO: implement get_dimensions for 3d matrices
    local res = 0
    if type(a[1] == "table") then
        for i = 1, #a do
            for j = 1, #a[1] do
                res = res + a[i][j]
            end
        end
    else
        for i = 1, #a do
            res = res + a[i]
        end
    end
    return res
end

function numlua.mean(a)
    -- TODO: implement get_dimensions for 3d matrices
    if type(a[1] == "table") then
        return numlua.sum(a) / (#a * #a[1])
    else
        return numlua.sum(a) / #a
    end
end

function numlua.log(a, base)
    -- TODO: implement get_dimensions for 3d matrices
    local res = {}
    if type(a[1] == "table") then
        for i = 1, #a do
            res[i] = {}
            for j = 1, #a[1] do
                res[i][j] = math.log(a[i][j], base)
            end
        end
    else
        for i = 1, #a do
            res[i] = math.log(a[i], base)
        end
    end
    return res
end

function numlua.xlogy(x, y)
    return numlua.dot(x, numlua.log(y))
end

return numlua
