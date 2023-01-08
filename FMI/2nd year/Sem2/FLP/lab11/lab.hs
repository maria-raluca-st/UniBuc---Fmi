import Data.List
import Data.Maybe

type Name = String 

data Value = VBool Bool 
    | VInt Int 
    | VFun (Value -> Value)
    | VError 

data Hask = HTrue 
    | HFalse 
    | HIf Hask Hask Hask 
    | HLet Name Hask Hask 
    | HLit Int 
    | Hask :==: Hask 
    | Hask :+: Hask
    | Hask :*: Hask 
    | HVar Name 
    | HLam Name Hask 
    | Hask :$: Hask 
    deriving Show

-- let x = y + 1 in z = 2 * x 

infix 4 :==:
infixl 6 :+:
infixl 7 :*: 
infixl 9 :$:

type HEnv = [(Name, Value)]

-- env = [("x", VBool False), ("y", VInt 10)]
-- hEval (HVar "y") env 
-- lookup "y" env  intoarce Just $ VInt 10 
-- lookup "z" env  intoarce Nothing 

showV :: Value -> String 
showV (VBool b) = show b 
showV (VInt i) = show i 
showV (VFun _) = "<function>"
showV VError = "<error>"

instance Show Value where 
    show = showV

eqV :: Value -> Value -> Bool 
eqV (VBool b1) (VBool b2) = b1 == b2 
eqV (VInt i1) (VInt i2) = i1 == i2 
eqV _ _ = False 

instance Eq Value where
    (==) = eqV 

hEval :: Hask -> HEnv -> Value
hEval HTrue _ = VBool True 
hEval HFalse _ = VBool False 
hEval (HIf cond sttrue stfalse) env = hif (hEval cond env) (hEval sttrue env) (hEval stfalse env)
    where
        hif (VBool b) st1 st2 = if b then st1 else st2 
        hif _ _ _ = error "if error" 
hEval (HLit i) _ = VInt i 
hEval (exp1 :+: exp2) env = hadd (hEval exp1 env) (hEval exp2 env) 
    where
        hadd (VInt i1) (VInt i2) = VInt $ i1 + i2
        hadd _ _ = error "plus error"
-- 
hEval (exp1 :*: exp2) env = hmul (hEval exp1 env) (hEval exp2 env) 
    where
        hmul (VInt i1) (VInt i2) = VInt $ i1 * i2
        hmul _ _ = error "mul error"
hEval (exp1 :==: exp2) env = heq (hEval exp1 env) (hEval exp2 env) 
    where
        heq (VInt i1) (VInt i2) = VBool (i1 == i2)
        heq (VBool b1) (VBool b2) = VBool (b1 == b2)
        heq _ _ = error "eq error"
-- 
hEval (HLet x valexpr expr) env = hEval expr ((x, hEval valexpr env) : env)
hEval (HVar x) env = fromMaybe (error "not found") $ lookup x env 
hEval (f :$: g) env = happ (hEval f env) (hEval g env)
    where 
        happ (VFun f) v = f v
        happ _ _ = error "aplicare de functie"
hEval (HLam x expr) env = VFun (\v -> hEval expr ((x, v) : env))


run :: Hask -> String 
run pg = showV $ hEval pg []

h0 = (HLam "x" (HLam "y" ((HVar "x") :+: (HVar "y")))) :$: (HLit 3) :$: (HLit 4)
-- = (\x -> \y -> x + y) 3 4 
h1 = HLet "x" (HLit 3) ((HLit 4) :*: HVar "x") 

-- data Hask = HTrue 
--     | HFalse 
--     | HIf Hask Hask Hask 
--     | HLet Name Hask Hask 
--     | HLit Int 
--     | Hask :==: Hask 
--     | Hask :+: Hask
--     | Hask :*: Hask 
--     | HVar Name 
--     | HLam Name Hask 
--     | Hask :$: Hask 
--     deriving Show

-- HLet, HLit, HLam, Hvar, 

h2 = HIf (HFalse :==: HFalse) (HLit 2) (HLit 1)