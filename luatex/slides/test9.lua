function factorial(n)
    if n <= 1 then
        return 1
    else
        return n * factorial(n-1)
    end
end

function poweroftwo(from,to)
    for n = from,to do
        debugprint(n .. "&" .. math.pow(2, n))
        debugprint("\\\\")
    end
end

