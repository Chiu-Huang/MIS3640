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
 else 1;;


let rec choose (n:int) (k:int):int =
if k>1 then n /(n-k) * choose (n-1) (k-1)  else n;;

(*COME BACK Later*)

let rec choose (n:int) (k:int):int =
   if n = k then  1 else ((choose (n-1) k) * n) / (n-k) ;;


let rec gcd (a:int) (b:int):int  = 
  if b = 0 then a 
  else gcd (b) (a mod b);;

let rec coprimes (n:int):int list = 
  (*Come Back Later*)
  

(* Question 2 *)


let rec tripleUp (xs:'a list):'a list =
  xs + tripleUp (xs)

let rec nth (n:int) (xs:'a list):'a =
 if 


let rec last (xs:'a list):'a = 
  failwith "last not implemented"


let rec appendAll (xss:'a list list):'a list =
  failwith "appendAll not implemented"


let rec split (xs:'a list):('a list * 'a list) =
  failwith "split not implemented"
  


(* QUESTION 3 *)


let rec addV (v:int list) (w:int list):int list =
  failwith "addV not implemented"


let rec scaleV (a:int) (v:int list):int list =
  failwith "scaleV not implemented"


let rec inner (v:int list) (w:int list):int =
  failwith "inner not implemented"


let rec outer (v:int list) (w:int list):int list list =
  failwith "outer not implemented"
