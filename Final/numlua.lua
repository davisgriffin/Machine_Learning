local numlua = {}

local function pack(vector)
    local packed_vector = {}
    for i = 1, #vector do
        packed_vector[i] = { vector[i] }
    end
    return packed_vector
end

function numlua.vdot(a, b)
    assert(#a == #b, "vector dimensions must agree")
    local res = 0

    for i = 1, #a do
        res = res + a[i] * b[i]
    end

    return res
end

local function dot(a, b)
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
        return dot({ a }, b)
    elseif type(b[1]) == "number" then
        return dot(a, pack(b))
    end

    return dot(a, b)
end

return numlua
