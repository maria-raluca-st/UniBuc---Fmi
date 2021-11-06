factori :: Int -> [Int]
factori n = [d | d <- [1..n], rem n d == 0]


prim :: Int -> Bool
prim n
    | n == 1 = False
    | length (factori n) <= 2 = True
    | otherwise = False
 
numerePrime :: Int -> [Int]
numerePrime n = [a | a <- [2..n], prim a]




myzip3 :: [a1] -> [a2] -> [a3] -> [(a1, a2, a3)]
myzip3 ls1 ls2 ls3
    | (null ls1) || (null ls2) || (null ls3) = []
    | otherwise = ((head ls1), (head ls2), (head ls3)) : myzip3 (tail ls1) (tail ls2) (tail ls3)
 
myzip3' :: [a] -> [b] -> [c] -> [(a, b, c)]
myzip3' ls1 ls2 ls3 = [(fst x, fst y,fst z) | x <- (zip ls1 [1..]),
                         y <- (zip ls2 [1..]),z <- (zip ls3 [1..]), snd x == snd y && snd y == snd z ]
 
myzip3'' :: [a] -> [b] -> [c] -> [(a, b, c)]
myzip3'' ls1 ls2 ls3 = [(x,y,z) | (x, (y, z)) <- zip ls1 (zip ls2 ls3)]


ordonatNat :: Ord a => [a] -> Bool
ordonatNat [] = True
ordonatNat ll@(l:ls) = and [x <= y | (x,y) <- zip ll ls]


ordonataNatRec :: [Int] -> Bool
ordonataNatRec [] = True
ordonataNatRec [x] = True
ordonataNatRec (x : y: xs) = ordonataNatRec (y : xs) && (x < y)


ordonataNatRec :: [Int] -> Bool
ordonataNatRec [] = True
ordonataNatRec [x] = True
ordonataNatRec (x : xs) = ordonataNatRec xs && (x < head xs)


-- 7
ordonata :: [a] -> (a -> a -> Bool) -> Bool
ordonata [] rel = True
ordonata [x] rel = True
ordonata (x : y : xs) rel = rel x y && ordonata (y : xs) rel



fncMod :: Integral a => a -> a -> Bool
fncMod x y = x `mod` y == 0
ordonata :: [t] -> (t -> t -> Bool) -> Bool
ordonata ll@(l:ls) fnc = and [fnc x y | (x,y) <- zip ll ls]


(*<*) :: (Integer, Integer) -> (Integer, Integer) -> Bool
(x, y) *<* (z, t) = x <= z && y <= t




compuneList :: (a -> b) -> [b -> c] -> [a -> c]
compuneList fnc lsFnc = [f . fnc | f <- lsFnc]
 
aplicaList :: t -> [t -> a] -> [a]
aplicaList nr lsFnc = [f nr | f <- lsFnc]


