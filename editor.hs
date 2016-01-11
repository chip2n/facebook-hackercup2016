import Data.List
import Control.Monad
import Control.Applicative hiding (many, (<|>))
import Text.Parsec hiding (getInput)
import Text.Parsec.String
import System.Environment

main :: IO()
main = do
    args <- getArgs
    solve (head args)

inputFile :: Parser [([String], Int)]
inputFile = do
  input <- many chunk
  eof
  return input

chunk :: Parser ([String], Int)
chunk = do
  (c, a) <- infoLine 
  result <- count c line
  return (result, a)

infoLine :: Parser (Int, Int)
infoLine = do
    [x, y] <- number `sepBy` (char ' ' *> spaces)
    try $ char '\n'
    return (x,y)

line :: Parser String
line = do
    l <- many $ noneOf "\n"
    try $ char '\n'
    return l

number = read <$> many digit

getInput :: FilePath -> IO [([String], Int)]
getInput fp = do
    contents <- liftM lines $ readFile fp
    let chunkCount = head contents
        contents' = tail contents
    case parse inputFile "(unknown)" (unlines contents') of
        Right x -> return x
        Left x -> error $ show x

solve :: FilePath -> IO ()
solve fp = do
    input <- getInput fp
    putStrLn $ unlines $ answers input
  where render n value = "Case #" ++ show n ++ ": " ++ show value
        answers input = map (\(n, a) -> render n $ uncurry solve2 a) (zip [1..] input)

wordDiff :: String -> String -> Int
wordDiff (x:xs) (y:ys) | x == y = wordDiff xs ys
wordDiff xs     ys              = length xs + length ys

cheapestNextWord :: String -> [String] -> (String, Int)
cheapestNextWord word words = minimumBy lowestCost costs
  where words' = delete word words
        lowestCost (_, a) (_, b) = compare a b
        costs = map (\w -> (w, wordDiff word w)) words'

solve2 :: [String] -> Int -> Int
solve2 words count = minimum $ map (\w -> length w + solve' words count w) words
  where solve' _     1     word = 1 + length word -- print cost & cost to clear
        solve' words count word =
            let words' = delete word words
                (nextWord, cost) = cheapestNextWord word words
                newCost = 1 + cost   -- print cost & cost for next word
            in  newCost + solve' words' (count - 1) nextWord
