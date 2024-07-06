module Script where

ifEvenAdd2 :: Integer -> Maybe Integer
ifEvenAdd2 n = if even n then Just (n + 2) else Nothing

data Sounds =
    Screech
    | Wail
    deriving Eq

instance Show Sounds where
    show Screech = "*Screeeeech*"
    show Wail = "*Waaaaa*"
