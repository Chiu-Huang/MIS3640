(* 

HOMEWORK 1

Name: Ching Chiu Huang

Email: chuang2@babson.edu 

Remarks, if any:

*)


(*
 *
 * Please fill in this file with your solutions and submit it
 *
 * The functions below are stubs that you should replace with your
 * own implementation.
 *
 * PLEASE DO NOT CHANGE THE TYPES IN THE STUBS BELOW.
 * Doing so risks making it impossible for me to test your code.
 *
 * Always make sure you can #use this file in a FRESH OCaml shell
 * before submitting it. It has to load without any errors.
 *
 *)



(* Question 1 *)


let rec expt (a:int) (b:int):int = 
  if b<>0 
  then 
      (if b>1 
      then a * (expt (a) (b-1))  
      else a) 
  else 1
 
 
 let rec choose (n:int) (k:int):int =
    if n = k then  1 else ((choose (n-1) k) * n) / (n-k) 
 
 
 let rec gcd (a:int) (b:int):int  = 
   if b = 0 then a 
   else gcd (b) (a mod b)
 
 
 let n = ref 10
 let k = n 
 
 let rec coprimes (n:int):int list =
 match n with 
 0 -> []
 |_ ->  
   if gcd !k n = 1 then [n] @ coprimes (n-1) else coprimes (n-1);;

  
(* Question 2 *)

   let rec tripleUp xs =
    match xs with 
    []-> []
    |h::r -> if r = [] then [h] @ [h] @ [h] else [h] @ [h] @ [h] @ tripleUp r  
    
  
  
  let rec nth (n:int) (xs:'a list):'a =
   if n = 0 
   then (match xs with [] -> failwith "last not implement" |h::r -> h)
   else nth (n-1) (match xs with [] -> failwith "last not implement" | h::r -> r)
  
  
  
  let rec last (xs:'a list):'a = 
    match xs with 
    [] -> failwith "last not implement"
    |h::r -> if r =[] then h else last r  
  
  
  let rec appendAll (xss:'a list list):'a list =
    match xss with 
    [] -> []
    |h::r -> h @ (appendAll r);;

(*Fail*
let rec length k = 
  match k with 
  [] -> 0
  | _::tk -> 1 + length tk 

let rec split (xs:'a list):('a list * 'a list) =
match xs with 
[] -> ([],[])
|a::b -> 
if length (xs) mod 2 = 0 
  then ([a],[]) @ split b

  
  else ([],[a]) @ split b;; 
  *)


(* QUESTION 3 *)

let rec addV (v:int list) (w:int list):int list =
  match (v,w) with
    ([],[]) -> [] 
    | (vh::vt,[]) -> [] 
    | ([],wh::wt) -> []
    | (vh::vt,wh::wt) -> [vh + wh] @ addV (vt) (wt)
  
  
  
  let rec scaleV (a:int) (v:int list):int list =
    match v with
    [] -> []
    | h::t -> [h * a] @ scaleV a t
  
  
  
  
  let rec inner (v:int list) (w:int list):int =
    match (v,w) with
    ([],[]) -> 0
    | (vh::vt,[]) -> 0 
    | ([],wh::wt) -> 0
    | (vh::vt,wh::wt) -> (vh * wh) + inner (vt) (wt)  ;;  



(*Fail*

let rec outer (v:int list) (w:int list):int list list=
match (v,w) with
 ([],[]) -> []
| (a::b,[]) -> []
| ([],c::d) -> []
| (a::b,c::d) -> if d = []  
 then [a * c] @ outer (v) (d) , outer (b) (w))
 else [a * c] @ outer (v) (d);;

*)


 (*Testing
 let rec outer (v:int list) (w:int list):int list  =
  match (v,w) with
   ([],[]) -> []
   | (a::b,[]) -> []
   | ([],c::d) -> []
   | (a::b,c::d) -> [a * c] @ outer (v) (d);;
 *)
 