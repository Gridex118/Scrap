{-# LANGUAGE RankNTypes #-}
module Rank where

rankN :: ((forall n. Num n => n -> n) -> (Int, Double))
rankN f = (f 1, f 1.0)

type Nat f g = forall a. f a -> g a
maybeToList :: Nat Maybe []
maybeToList Nothing = []
maybeToList (Just a) = [a]
