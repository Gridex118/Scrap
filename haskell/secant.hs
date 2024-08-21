{-# OPTIONS_GHC -Wall #-}

module Secant where

import Text.Printf

-- Interval (a, b)
data Interval = Interval Double Double

-- Step (x_n1, x_n2, x_n, p = f(x_n))
data Step = Step Double Double Double Double
instance Show Step where
    show (Step x_n1 x_n2 x_n p) =
        printf "[% .13f, % .13f] : % .13f -> % .13f" x_n2 x_n1 x_n p
type Equation = Double -> Double

secant :: Equation -> Interval -> Step
secant f (Interval a b) =
    let
        x_n1 = b
        x_n2 = a
        f_x_n1 = f x_n1
        f_x_n2 = f x_n2
        x_n = x_n1 - f_x_n1 * ((x_n1 - x_n2) / (f_x_n1 - f_x_n2))
        p = f x_n
    in
        Step x_n1 x_n2 x_n p

nextInterval :: Step -> Interval
nextInterval (Step x_n1 _ x_n _) =
    Interval a b
    where
        a = x_n1
        b = x_n

methodOfSecant :: Int -> Equation -> Interval -> [Step]
methodOfSecant precision f (Interval a b) =
    go (Interval a b) []
    where
        go (Interval a' b') sol =
            let this_step = secant f (Interval a' b')
                err = (\(Step _ _ _ p) -> abs p) this_step
            in
                if err > 10^^(-precision)
                then go (nextInterval this_step) (sol ++ [this_step])
                else sol ++ [this_step]

solution :: Int -> Equation -> Interval -> IO ()
solution precision f interval = mapM_ print $ methodOfSecant precision f interval
