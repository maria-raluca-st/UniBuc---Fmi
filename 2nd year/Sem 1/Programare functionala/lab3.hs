vocale :: String->Int
vocale ls@(hd:tl)
    | null ls = 0
    | elem hd "aeiouAEIOU" = 1 + vocale tl
    | otherwise = vocale tl

f :: Integer -> [Integer]-> [Integer]
f el ls
  | null ls = 0
  | even (head ls)=(head ls) : el : (f el (tail ls))
  | otherwise = (head ls) : (f el (tail ls))

  divizori :: Integer a=> a->[a]
  divizori a = [x | x <-[1..a] , a`mod` x ==0]

  listadiv :: [Integer] -> [[Integer]]
  listadiv ls = [divizori x | x <- ls]

  inIntervalRec :: Integer -> Integer -> [Integer] ->[Integer]
  inIntervalRec x y ls
    | null ls = []
    | x<=x && z<=y = z :: inIntervalRec x y (tail ls) 
    | otherwise - inIntervalRec x y (tail ls)
    where z = head ls

pozitiiImpareComp :: [Int ] -> [Int ]
pozitiiImpareComp ls = [snd x | x<- zip ls [0..] odd (fst x)]