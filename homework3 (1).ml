(* 

HOMEWORK 3

Name: Ching Chiu Huang

Email: chuang2@babson.edu

Remarks, if any:

*)



(* 
 * String <-> characters utility functions:
 *
 *   explode : string -> char list
 *      returns the list of characters making up a string
 *
 *   implode : char list -> string
 *      concatenates the list of characters into a string
 *
 *)

let explode (str) = 
  let rec acc (index,result) = 
    if (index<0) then
      result
    else
      acc(index-1, (String.get str index)::result)
  in
    acc(String.length(str)-1, [])

let implode cs = 
  List.fold_right (fun a r -> (String.make 1 a)^r) cs ""



(*
 *  The type of a finite automaton
 * 
 *)

type 'a fa = { states: 'a list;
               alphabet: char list;
               delta: ('a * char * 'a) list;
               start : 'a;
               final : 'a list }


(* 
 * Sample FAs
 *
 * The first accepts the language of all strings over {a,b} 
 * with a multiple-of-3 number of a's.
 *
 * The second accepts the language of all strings over {a,b,c} 
 * whose last three symbols are b's.
 *
 * Notes that states can be of any type -- the first example
 * uses strings as states, while the second uses integers.
 *
 *)

let faThreeA = { 
  states = ["start";"one";"two"];
  alphabet = ['a';'b'];
  delta = [ ("start",'a',"one");
	    ("one",'a',"two");
	    ("two",'a',"start");
	    ("start",'b',"start");
	    ("one",'b',"one");
	    ("two",'b',"two") ];
  start = "start";
  final = ["start"]
} 

let faLastThreeB = {
  states = [0;1;2;3];
  alphabet = ['a';'b';'c'];
  delta = [ (0,'a',0);
	    (0,'b',0);
	    (0,'c',0);
	    (0,'b',1);
	    (1,'b',2);
	    (2,'b',3); ];
  start = 0;
  final = [3]
} 


(* let list_break (qs:(int * char * int) list): (int * char * int) =
  match qs with
  q::s -> q *)
(* QUESTION 1 *)
let rec set_in (e:'a) (xs:'a list):bool = 
  match xs with
  [] -> false 
  | x::xs' -> if e = x then true else set_in e xs'

let rec element_in_set e l =
  match l with
  |[]-> false
  |h::t -> if h = e then true else element_in_set e t




let rec listelement_in_set k l =
  match k with
  |[] -> false
  |h::t -> if element_in_set h l then true else listelement_in_set t l

let rec list_to_set (xs:'a list):'a list = 
  match xs with
  [] -> []
  |x::xs' -> if set_in x xs' == false then x:: list_to_set (xs') else  list_to_set (xs')
  

let rec hasFinal (m:'a fa) (qs:'a list):bool =
  match qs with 
  [] -> false
  |q::qs' -> if element_in_set q m.final then true else hasFinal m qs'  


let reachableStates (m:'a fa) (q:'a) (a:char):'a list =
  let rec helper (l) =
    match l with
    [] -> []
    |(s1,s2,s3)::t -> if s1 = q && s2 = a then [s3] @ helper (t) else helper t
  in helper (m.delta)


let rec follow (m:'a fa) (qs:'a list) (a:char):'a list = 
  match qs with 
  [] -> []
  |q::qs'-> reachableStates (m) (q) (a) @ follow (m) (qs') (a)
  
let rec followAll (m:'a fa) (qs:'a list) (syms:char list):'a list = 
  match syms with
  [] -> qs
  |s::syms' -> followAll (m) (follow m qs s) syms'

  

let accept (m:'a fa) (input:string):bool =
  if listelement_in_set (m.final) (followAll m [m.start] (explode input)) then true else false




(* let accept (m:'a fa) (input:string):bool = 
  if listelement_in_set m.final (followAll m qs explode (input)) then true else false 
  in s = m.final && qs = [m.start] *)
(* QUESTION 2 *)

(* Right now, these are dummy finite automata -- replace by your own *)

let dummya = { states = [1;2;3];
			alphabet = ['x';'y';'z'];
      delta = [ (0,'x',0);
          (0,'y',0);
          (0,'z',0);
          (0,'z',1);
          (1,'x',2);
          (1,'y',2);
          (1,'z',2);
          (2,'x',3);
          (2,'y',3);
          (2,'z',3)];
			start = 0;
      final = [3]}
      
let dummyb = { states = [1;2;3];
			alphabet = ['x';'y';'z'];
      delta = [ (0,'x',1);
          (0,'y',1);
          (0,'z',1);
          (1,'x',2);
          (1,'y',2);
          (1,'z',2);
          (2,'y',0);
          (2,'z',0);]
			start = 0;
			final = [2]}

let dummyc = { states = [0;1;2;3];
			alphabet = ['x';'y';'z'];
      delta = [ (0,'x',1);
          (0,'y',2);
          (0,'z',3);
          (1,'z',3);
          (2,'x',1);
          (2,'z',3);
          (3,'z',3);
          (3,'y',2);
          (3,'x',1);];
			start = 0;
      final = [0;1;2;3];}

let dummyd = { states = [0;1;2;3];
			alphabet = ['x';'y';'z'];
      delta = [ (0,'x',1);
          (1,'x',0);
          (1,'y',2);
          (2,'y',1);
          (3,'x',2);
          (2,'x',3);
          (3,'y',0);
          (0,'y',3);]
			start = 0;
			final = [3]}
let dummye = { states = [1;2;3;4;5;6;7;8];
			alphabet = ['x';'y';'z'];
      delta = [ (1,'x',2);
          (1,'z',3);
          (1,'y',5);
          (2,'z',4);
          (2,'y',6);
          (2,'x',1);
          (3,'y',7);
          (3,'x',4);
          (4,'x',3);
          (4,'y',8);
          (5,'z',7);
          (5,'x',6);
          (5,'y',1);
          (6,'z',8);
          (6,'y',2);
          (6,'x',5);
          (7,'y',3);
          (7,'x',8);
          (8,'x',7);
          (8,'y',4);
          ];
			start = 1;
			final = [4];}


let fa_q2_a : 'a fa = dummya

let fa_q2_b : 'a fa = dummyb

let fa_q2_c : 'a fa = dummyc

let fa_q2_d : 'a fa = dummyd

let fa_q2_e : 'a fa = dummye    



(* QUESTION 3 *)
let helper_change k m = 
  let rec helper_help_change p = 
    match p with 
    |[] -> [] 
    |(s1,s2,s3)::t -> if s1 = m.start then (k,s2,s3) :: (helper_help_change t) else (s1,s2,s3) :: (helper_help_change t)
  in (helper_help_change m.delta)



let unionM (m1:'a fa) (m2:'a fa):'a fa = {
  states = (list_to_set (m1.states @ m2.states));
  alphabet = (list_to_set (m1.alphabet @ m2.alphabet));
  start = m1.start;
  final = (list_to_set (m1.final @ m2.final));
  delta = list_to_set (m1.delta @ (helper_change m1.start m2)); }



(* let unionM (m1:'a fa) (m2:'a fa):'a fa = {
  states = (list_to_set (m1.states @ m2.states));
  alphabet = (list_to_set (m1.alphabet @ m2.alphabet));
  start = [];
  final = (list_to_set (m1.final @ m2.final));
  delta = ([],'p',m1.start):: ([],'p',m2.start)::(m1.delta @ m2.delta); } *)





(* 

let unionM (m1:'a fa) (m2:'a fa):'a fa = {
  states = (m1.states @ m2.states);
  alphabet = m1.alphabet @ m2.alphabet;
  start = m1.start;
  final = (m1.final @ m2.final);
  delta = m1.delta @ (helper_change (m1.start) (m2)); }
 *)


let concatM (m1:'a fa) (m2:'a fa):'a fa = 
  failwith "not implemented"


let interM (m1:'a fa) (m2:'a fa):('a * 'a) fa = 
  failwith "not implemented"







(* This function is the base function that basically loops through all
 * strings  
 * of length up to n, and prints those that are accepted by the
 * finite automaton.
 *
 * This is being way too clever to try to not blow the stack 
 * while enumerating all strings up to a given length. Basically.
 * we enumerate all integer, convert them to base K (where K is the
 * size of the alphabet) and then replace every digit base K by the
 * letter of the alphabet at the corresponding index in the alphabet. 
 *
 * The key is that we can enumerate integers super easily
 *
 *)

let lang m n = 

  let rec expt a n = if n <= 0 then 1 else a*(expt a (n-1)) in
  
  let rec take n default l = 
    if n <= 0 then []
    else (match l with
          | [] -> default::(take (n-1) default l)
          | x::xs -> x::(take (n-1) default xs)) in
  
  let to_base_n base size n = 
    let rec loop n = 
      if n <= 0 then []
      else if n mod base = 0 then 0::(loop (n / base))
      else (n mod base)::(loop ((n - n mod base) / base))  in
    take size 0 (loop n)  in
  
  let to_string alphabet size n = 
    let base = List.length alphabet in
    let num_base = to_base_n base size n in
    implode (List.map (fun i -> List.nth alphabet i) num_base) in
  
    if n < 0 then ()
    else
      let print_str s = if s = "" then print_string "  <epsilon>\n"
  	              else print_string ("  "^s^"\n")  in
      let rec loop i = 
        if i <= n then 
  	  let ts = to_string m.alphabet i  in
  	  let bound = expt (List.length m.alphabet) i in
  	  let rec loop2 j = 
  	    if j < bound then (if accept m (ts j) 
                                 then print_str (ts j)
                               else ();
  			       loop2 (j+1))
  	    else ()  in
  	  (loop2 0; loop (i+1))
        else ()  in
      loop 0

