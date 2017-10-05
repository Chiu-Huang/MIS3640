type 'a fa = { states: 'a list;
alphabet: char list;
delta: ('a * char * 'a) list;
start : 'a;
final : 'a list }


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

(*find element in list function*)
let rec element_in_set e l =
  match l with
  |[]-> false
  |h::t -> if h = e then true else element_in_set e t 

let states (m:'a fa) = m.states
let addTransition t m = {m with delta = t::m.delta}


m qs

start 




qs --> delta 2th element
q::qs' 
match q with 
|(s1,sym,s2)::tl -> 
if (s1 = state && qs =sym) then
s2 else find_state tl
|_-> failwith "nothing"

let hasFinal m qs =
  let a = m.start



let hasFinal (m:'a fa) (qs:'a list):bool =
  let current_state = m.start
  in 
  let rec find_state k (q) = 
    match k with
    |(s1, s2, s3)::t -> if s1= current_state && s2 = q then (current_state = s3) else find_state t
    | _ -> failwith "Not Applicable"
  in
  let rec move (qs) = 
    match qs with 
    [] -> if current_state = m.final then true else false 
    |h::[] -> find_state (m.delta) h 
    |h::t -> find_state m.delta && move (t)
  if find_state m.delta h <> "Not Applicable" then move t else false  
  in
  if (element_in_set final_state m.final) then true else false;;


let accept (m:'a fa) (qs:'a list):bool =
  let transition state q =
    let rec find_state l =
      match l with 
      |(s1,sym,s2)::t -> 
      if (s1 = state && q = sym) then
      s2 else find_state t
      |_-> failwith "nothing"
    in find_state m.delta
  in 
  let final_state =
    let rec helper symbol_list =
      match symbol_list with
      |[h] -> (transition m.start h)
      |h::t -> (transition (helper t) h)
      |_-> failwith "not implemented"
    in 
    helper(List.rev qs)
  in
  if (element_in_set final_state m.final) then true else false;;

  
let hasFinal (m:'a fa) (qs:'a list):bool =
  let current_state = m.start
  in 
  let rec find_state k (q) = 
    match k with
    |(s1, s2, s3)::t -> if s1= current_state && s2 = q then (current_state = s3) else find_state t
    | _ -> failwith "Not Applicable"
  in
  let rec move (qs) = 
    match qs with 
    |[] -> if [] 
    |h::[] -> find_state (m.delta) h
    |h::t -> if find_state m.delta h <> "Not Applicable" then move t else failwith "Not Applicable"  
  in
  if (element_in_set current_state m.final) then true else false;;


  let current_state = faLastThreeB.start
  in 
  let rec find_state k (q) = 
    match k with
    |(s1, s2, s3)::t -> if s1= current_state && s2 = q then (current_state = s3) else find_state (t) q 
    | _ -> failwith "Not Applicable"
  in
  let rec move (qs) = 
    match qs with 
    |[] -> if [] 
    |h::[] -> find_state (m.delta) h
    |h::t -> if find_state m.delta h <> "Not Applicable" then move t else failwith "Not Applicable"  
  in
  if (element_in_set current_state m.final) then true else false;;


  let rec move (qs) = 
    match qs with 
    [] -> if (element_in_set current_state faLastThreeB.final) then true else false 
    |h::[] -> find_state (faLastThreeB.delta) h 
    |h::t ->  move (t)
    find_state faLastThreeB.delta &&
























    let	checkAccepts str dfa	=	
      let	symbols	=	explode	str	in
      let	transi4on	state	symbol	=		
        let	rec	find_state	l	=		
            match	l	with	
            |	(s1,sym,s2)::tl	->	
                if	(s1	=	state	&&	symbol	=	sym)	then		
                s2	else	find_state tl		
            |	_	->	failwith	"no	next	state"	in	find_state dfa.transi4ons		
        in	find_state dfa.transi4ons		
    in		
    let	final_state	=		
      let	rec	h	symbol_list	=		
          match	symbol_list	with	
          |	[hd]	->	(transi4on	dfa.start hd)	
          |	hd::tl	->	(transi4on	(h	tl)	hd)	
          |	_	->	failwith	"empty	list	of	symbols"
      in	
      h	(List.rev	symbols)	
    in	if	(contains	final_state dfa.accep4ng)	then		
            true		
        else		
    false	
    