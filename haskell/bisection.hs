{-# OPTIONS_GHC -Wall #-}

module Bisection where
import Text.Printf

type Equation = Double -> Double
type Iteration = (Double, Double, Double, Double)
type Bounds = (Double, Double)

bisection :: Bounds -> Equation -> Iteration
bisection (a, b) f =
    (a, b, c, f c) where
        c = (a + b) / 2

nextI :: Iteration -> Bounds
nextI (a, b, c, p) =
    if p > 0 then (a, c) else (c, b)

methodOfBisection :: Equation -> Bounds -> Int -> [Iteration]
methodOfBisection f (a, b) precision = go (a, b) []
    where
        go :: Bounds -> [Iteration] -> [Iteration]
        go (a', b') sol =
            let this_iter = bisection (a', b') f
                err = (\(_, _, _, p) -> abs p) this_iter
            in
                if err > 10^^(-precision)
                then go (nextI this_iter) (sol ++ [this_iter])
                else sol ++ [this_iter]

printIteration :: Iteration -> String
printIteration (a, b, c, p) =
    printf "[%.13f, %.13f] : %.13f -> % .13f" a b c p

solution :: Equation -> Bounds -> Int -> IO ()
solution f (a, b) precision =
    mapM_ (print . printIteration) (methodOfBisection f (a, b) precision)
