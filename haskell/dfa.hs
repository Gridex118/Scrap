module DFA where

type DFAState       = Char
type InitialState   = DFAState
type Transition     = (Char, DFAState)
type Transitions    = [Transition]
type AcceptinStates = [DFAState]
type DFA            = (InitialState, Transitions, AcceptinStates)

matchDFA :: String -> DFA -> Bool
matchDFA s dfa = True
