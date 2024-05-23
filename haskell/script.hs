module Scripts where

nonsense :: Bool -> Integer
nonsense True = 805
nonsense False = 31137

typicalCurriedFunction :: Integer -> Bool -> Integer
typicalCurriedFunction i b = i + nonsense b

uncurriedFunction :: (Integer, Bool) -> Integer
uncurriedFunction (i, b) = i + nonsense b

anonymous :: Integer -> Bool -> Integer
anonymous = \i b -> i + nonsense b

f :: Num a => (a, a) -> a
f (x, y) = x * y
