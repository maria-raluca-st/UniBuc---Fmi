paritate :: Integer -> String
paritate n=
    if(n `mod` 2 == 0)
        then "Par"
        else "Impar"
      
sumapatrate :: Integer -> Integer -> Integer
sumapatrate x y= x*x+y*y

factorial :: Integer -> Integer
factorial 0 = 1
factorial n= n * factorial(n-1)

dublu :: Integer -> Integer -> String
dublu x y= 
    if(x > 2*y)
        then "DA"
        else "NU"


