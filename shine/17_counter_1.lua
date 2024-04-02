function counter()
    local cnt = 0

    function next()
        cnt = cnt + 1
        return cnt
    end

    return next
end


counter1 = counter()

counter2 = counter()
counter2()

for i = 0, 10 do
    result1 = counter1()
    result2 = counter2()
    print(i, result1, result2)
end
