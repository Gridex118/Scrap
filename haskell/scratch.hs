module Scratch where

data Bounds = Bounds
    { a :: Double
    , b :: Double}

instance Show Bounds where
    show (Bounds a b) =
        "(" ++ show a ++ ", " ++ show b ++ ")"

bar :: Int -> Int
bar x =
    if x > 3
    then x * 2
    else x
