function counter(delta)
    local cnt = 0

    function next()
        cnt = cnt + delta
        return cnt
    end

    return next
end


counter1 = counter(2)

counter2 = counter(3)

for i = 0, 10 do
    result1 = counter1()
    result2 = counter2()
    print(i, result1, result2)
end
