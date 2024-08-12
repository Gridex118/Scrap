module Bisection where

middle :: Floating a => a -> a -> a
middle x y = (x + y) / 2

f :: Floating a => a -> a
f x = x**3 - (4 * x) - 9

nextI :: (Floating a, Ord a)  => a -> a -> (a, a, a)
nextI a b =
    if p > 0 then (a, c, p) else (c, b, p) where
        p = f c
        c = middle a b

methodOfBisection :: (Floating a, Ord a) => (a, a, a)
methodOfBisection = go 2.7 3 0 where
    go a b 15 = (a, b, 0)
    go a b n = do
        go (get0 p) (get1 p) (n + 1) where
            p = nextI a b
            get0 (x, _, _) = x
            get1 (_, x, _) = x
