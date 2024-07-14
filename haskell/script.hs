module Script where
import System.IO

main :: IO String
main = do
    hSetBuffering stdout NoBuffering
    putStr "Type your age: "
    age <- readLn :: IO Int
    putStrLn ("You are " ++ show age ++ " years old.")
    if age < 18
    then return "You are a minor"
    else return ""
