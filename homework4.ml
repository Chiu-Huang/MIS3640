(* 

HOMEWORK 4

Name: Ching Chiu Huang

Email: chuang2@babson.edu

Remarks, if any:

*)


(* QUESTION 1 *)
let rec set_in (e:'a) (xs:'a list):bool = 
  match xs with
  [] -> false 
  | x::xs' -> if e = x then true else set_in e xs'
let rec list_in (xs) (ys) =
  match ys with
  [] -> []
  | y::yss -> if set_in y xs then list_in xs yss else y :: list_in xs yss
let rec nfilter (p) (xs) =
let rec helper ys =
    match xs with
    [] -> []
    |h::t -> if set_in h ys then nfilter p t else h :: nfilter p t
    in helper (List.filter p xs)
let length l = List.fold_left (fun x _ -> x + 1) 0 l
let count (p:'a -> bool) (xs:'a list) : int = 
  length (filter (p) (xs)) 
let max x y =
  if x > y then x else y
let maxp (xs:int list) : int =
  match xs with 
  [] -> 0
  | x::xss -> if List.fold_left max x xss < 0 then 0 else List.fold_left max x xss 
let dbl x = "double "^(string_of_int x)
let neg x = "negation "^(string_of_int x)
let rec list lxs =
  match lxs with
  [] ->[]
  |x::xss -> x @ list xss
let mapf fs xs =
  list (List.map(fun f -> List.map(fun x -> f x) xs) fs)
let pairs (xs:'a list) (ys:'b list) : ('a * 'b) list = 
  List.rev (
    List.fold_left (
      fun acc y-> List.fold_left (
      fun acc2 x ->  (x,y) :: acc2) acc xs )
       [] ys)
(* Question 2 *)

let prepend (x:'a) (xss:'a list list) : 'a list list = 
  List.map(fun xs -> x::xs) xss 
let rec prefixes (xs:'a list) : 'a list list =   
  match xs with
  []   -> [[]]
  | x::xss -> []::List.map (fun k -> x :: k) (prefixes xss)
let rec augment_suffixes (xs:'a list) : ('a * 'a list) list =
  match xs with
  [] -> []
  |x::xss ->  (x , xs) :: augment_suffixes xss
let rec suffixes xs =
  match xs with
  [] -> []
  |x::xss ->  xs :: suffixes xss
let inject (x:'a) (xs:'a list) : 'a list list = 
  helpinject x xs
let helpinject x xs =
  match xs with
  [] -> [[x]]
  |h::t ->  List.map (fun y-> x :: y) (suffixes xs)
let prev xs lys =
  List.map (fun ys -> list_in xs ys) lys









(* BONUS *)

let permutations (xs:'a list):'a list list = 
  failwith "not implemented"

