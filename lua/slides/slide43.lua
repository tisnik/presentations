--------------------------------------
-- Alternativní způsob deklarace metod
--------------------------------------

-- Asociativni pole obsahujici metody
Complex={}

-- Konstruktor (ve skutecnosti jen vhodne
-- pojmenovana funkce)
function Complex.new(paramReal, paramImag)
    local self={}
    self.real = paramReal
    self.imag = paramImag
    return self
end

-- Metoda print s implicitnim predanim parametru self
function Complex:print()
    print(self.real.."+i"..self.imag)
end

-- Metoda add s implicitnim predanim parametru self
function Complex:add(paramReal, paramImag)
    self.real = self.real + paramReal
    self.imag = self.imag + paramImag
end

-- vytvoreni dvojice objektu
c = Complex.new(1, 2)
c2 = Complex.new(3, 4)

-- tisk hodnot obou objektu
Complex.print(c)
Complex.print(c2)

-- zmena atributu prvniho objektu
Complex.add(c, 10, 20)

-- tisk hodnot obou objektu
Complex.print(c)

