module Scratch where

data Bounds = Bounds Double Double

instance Show Bounds where
    show (Bounds a b) =
        "(" ++ show a ++ ", " ++ show b ++ ")"

foo :: Bounds -> Double
foo (Bounds a b) = a

bar :: Int -> Int
bar x =
    if x > 3
    then x * 2
    else x
