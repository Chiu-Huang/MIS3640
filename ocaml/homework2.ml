(* 

HOMEWORK 2

Name: Ching Chiu Huang

Email: chuang2@babson.edu 

*)
(* Q1: Set operations *)




let rec set_in (e:'a) (xs:'a list):bool = 
  match xs with
  [] -> false 
  | x::xs' -> if e = x then true else set_in e xs'

let rec set_sub (xs:'a list) (ys:'a list):bool = 
  match xs with 
  [] -> true
  |x::xs' -> if set_in (x) (ys) = true then set_sub (xs') (ys) else false

let rec list_to_set (xs:'a list):'a list = 
  match xs with
  [] -> []
  |x::xs' -> if set_in x xs' == false then x:: list_to_set (xs') else  list_to_set (xs')

let rec set_eq (xs:'a list) (ys:'a list):bool = 
  if set_sub (list_to_set xs) (list_to_set ys) && set_sub (list_to_set ys) (list_to_set xs) then true else false 
  
let rec set_union (xs:'a list) (ys:'a list):'a list = 
  match (list_to_set xs,list_to_set ys) with
  ([],[]) -> []
  |(x::xs',[]) -> list_to_set xs
  |([],y::ys') -> list_to_set ys
  |(x::xs',y::ys') -> if set_in x ys = false then x::set_union xs' ys else set_union xs' ys

let rec set_inter (xs:'a list) (ys:'a list):'a list = 
  match (list_to_set xs,list_to_set ys) with
  ([],[]) -> []
  |(x::xs',[]) -> []
  |([],y::ys') -> []
  |(x::xs',y::ys') -> if set_in x ys = true then x::set_inter xs' ys else set_inter xs' ys  
  
let rec set_helpsize xs index =
  match list_to_set xs with
  [] -> index
  |x::xs' -> set_helpsize xs' (index+1) 

and set_size (xs:'a list):int = set_helpsize xs 0

(* Q2: Language operations *)

(*how does it differ from 1D set_union?, check*)
let rec lang_union (xs:string list) (ys:string list):string list = 
  match (xs,ys) with
  ([],[]) -> []
  | (a::b,[]) -> xs
  | ([],c::d) -> ys
  | (a::b,c::d) -> [a] @ [c] @ lang_union (b) (d)
  
let rec scaleL (x:string) (ys:string list):string list =
  match ys with
  [] -> []
  |y::ys' -> [x ^ y] @ scaleL x ys'
  
let rec lang_concat (xs:string list) (ys:string list):string list = 
  match (list_to_set xs,list_to_set ys) with
  ([],[]) -> []
  |(x::xs',[]) -> []
  |([],y::ys') -> []
  |(x::xs',y::ys') -> scaleL x ys @ lang_concat xs' ys



let rec lang_helpnstar (n:int) (xs:string list) result:string list = 
  if n > 0 then lang_concat xs result @ lang_helpnstar (n-1) xs (lang_concat (xs) (result)) else [""]

let rec lang_nstar (n:int) (xs:string list):string list = lang_helpnstar n xs [""]

(* Q3: regular expressions *)

type re = 
    Empty 
  | Unit 
  | Letter of string 
  | Plus of re * re 
  | Times of re * re 
  | Star of re

let compute_lang n s = 
  let fromChar c = String.make 1 c in
  let explode s = 
    let rec loop i result = 
      if i < 0 then result
      else loop (i-1) (s.[i]::result) in
    loop (String.length s - 1) []  in
  let isalpha = function 'A'..'Z'|'a'..'z' -> true | _ -> false in
  let expect c cs = 
    match cs with 
      f::cs when f = c -> Some cs
    | _ -> None in
  let expect_alpha cs = 
    match cs with
      f::cs when isalpha f -> Some (f,cs)
    | _ -> None  in
  let rec parse_R cs = 
    match parse_R1 cs with
      None -> None
    | Some (r1,cs) -> 
        (match expect '+' cs with
           None -> Some (r1,cs)
         | Some cs -> 
             (match parse_R cs with
                None -> None
              | Some (r2,cs) -> Some (Plus(r1,r2),cs)))
  and parse_R1 cs = 
    match parse_R2 cs with
      None -> None
    | Some (r1,cs) -> 
        (match parse_R1 cs with
           None -> Some (r1,cs)
         | Some (r2,cs) -> Some (Times(r1,r2),cs))  
  and parse_R2 cs = 
    match parse_R3 cs with
      None -> None
    | Some (r1,cs) -> 
        (match expect '*' cs with
           None -> Some (r1,cs)
         | Some cs -> Some (Star(r1),cs))
  and parse_R3 cs = 
    match expect_alpha cs with
      Some (a,cs) -> Some (Letter(fromChar(a)),cs)
    | None -> 
        (match expect '1' cs with
           Some cs -> Some (Unit, cs)
         | None -> 
             (match expect '0' cs with
                Some cs -> Some (Empty,cs)
              | None -> parse_parens cs))
  and parse_parens cs = 
    match expect '(' cs with
      None -> None
    | Some cs -> 
        (match parse_R cs with
           None -> None
         | Some (r,cs) -> 
             (match expect ')' cs with
                None -> None
              | Some cs -> Some (r,cs)))  in
  let parse s = 
    let cs = explode s in
    match parse_R cs with
      Some (re,[]) -> re
    | _ -> failwith ("Cannot parse "^s)  in
  let rec eval re k = 
    match re with
      Empty -> k []
    | Unit -> k [""]
    | Letter (a) -> k [a]
    | Plus (r1,r2) -> eval r1 (fun l1 -> eval r2 (fun l2 -> k (lang_union l1 l2)))
    | Times (r1,r2) -> eval r1 (fun l1 -> eval r2 (fun l2 -> k (lang_concat l1 l2)))
    | Star r -> eval r (fun l -> k (lang_nstar n l))  in
  eval (parse s) (fun x -> x)




let lang r n ml = 

  let l = List.filter (fun s -> String.length s <= ml) (compute_lang n r)  in

  let cmp a b = if String.length a < String.length b then -1
                else if String.length b < String.length a then 1
                else String.compare a b   in

  let sl = List.sort cmp l in

  let rec loop l seen = 
    match l with
    | [] -> ()
    | s::rest -> if List.mem s seen 
                   then loop rest seen 
                 else (match s with 
                       | "" -> let _ = print_string "  <epsilon>\n" in loop rest (""::seen)
                       | s -> let _ = print_string ("  "^s^"\n") in loop rest (s::seen)) in
  loop sl []
    



(* QUESTION 3 *)
let regexp_a : string = "(e+d)(e+d)(e+d)(e+d)" 
let regexp_b : string = "(ed)*(de)*(dd)*(ee)*(e+d)"
let regexp_c : string = "e*(d)(e)*(d)(e)*"   
let regexp_d : string = "e*d(dd)*e*";;
let regexp_e : string = "(e)*(dee)*(e)*";;


