module Bisection where

f :: Float -> Float
f x = x**3 - (4 * x) - 9

nextI :: (Float, Float, Float) -> (Float, Float)
nextI (a, b, p) =
    let c = (a + b) / 2 in
        if p > 0 then (a, c) else (c, b)

bisection :: (Float, Float) -> (Float, Float, Float)
bisection (a, b) =
    let c = (a + b) / 2 in
        (a, b, f c)
