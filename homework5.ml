(* 

HOMEWORK 5

Name: Ching Chiu Huang

Email: chuang2@babson.edu

Remarks, if any:

*)



(*
 * Type for deterministic Turing machines
 *
 * Parameterized by type for states
 *)

type symbol = string

type 'a tm = { states : 'a list;
	       input_alphabet : symbol list;
	       tape_alphabet : symbol list;
	       left_marker : symbol;
	       blank : symbol;
	       delta : ('a * symbol) -> ('a * symbol * int);   (* 0 = Left, 1 = Right *)
	       start : 'a;
	       accept : 'a;
	       reject : 'a }

type 'a config = { state : 'a;
		   tape: symbol list;
		   position: int }


(* 
 * Some sample deterministic Turing machines
 *
 * asbs is the regular language {a^m b^n | m,n >= 0}
 * anbn is the non-regular language {a^n b^n | n >= 0}
 * anbncn is the non-regular language {a^n b^n c^n | n >= 0}
 *
 *)

let asbs = { states = ["start"; "q1"; "acc"; "rej"];
	     input_alphabet = ["a";"b"];
	     tape_alphabet = ["a";"b";"_";">"];
	     blank = "_";
	     left_marker = ">";
	     start = "start";
	     accept = "acc";
	     reject = "rej";
	     delta = (fun inp -> match inp with
	                 | ("start", "a") -> ("start", "a", 1)
     			 | ("start", "b") -> ("q1", "b", 1)
			 | ("start", ">") -> ("start", ">", 1)
			 | ("start", "_") -> ("acc", "_", 1)
			 | ("q1", "b") -> ("q1", "b", 1)
			 | ("q1", "_") -> ("acc", "_", 1)
			 | ("acc", "a") -> ("acc", "a", 1)
			 | ("acc", "b") -> ("acc", "b", 1)
			 | ("acc", ">") -> ("acc", ">", 1)
			 | ("acc", "_") -> ("acc", "_", 1)
			 | (_,c) -> ("rej",c,1))}

let anbn = { states = ["start"; "q1"; "q2"; "q3"; "q4"; "acc"; "rej"];
	     input_alphabet = ["a";"b"];
	     tape_alphabet = ["a";"b";"X";"/";"|"];
	     blank = "/";
	     left_marker = "|";
	     start = "start";
	     accept = "acc";
	     reject = "rej";
	     delta = (fun inp -> match inp with
	                 | ("start", "a") -> ("start", "a", 1)
     			 | ("start", "b") -> ("q1", "b", 1)
			 | ("start", "|") -> ("start", "|", 1)
			 | ("start", "/") -> ("q2", "/", 1)
			 | ("q1", "b") -> ("q1", "b", 1)
			 | ("q1", "/") -> ("q2", "/", 1)
			 | ("q2", "|") -> ("q3", "|", 1)
			 | ("q2", "a") -> ("q2", "a", 0)
			 | ("q2", "b") -> ("q2", "b", 0)
			 | ("q2", "X") -> ("q2", "X", 0)
			 | ("q2", "/") -> ("q2", "/", 0)
			 | ("q3", "X") -> ("q3", "X", 1)
			 | ("q3", "/") -> ("acc", "/", 1)
			 | ("q3", "a") -> ("q4", "X", 1)
			 | ("q4", "a") -> ("q4", "a", 1)
			 | ("q4", "X") -> ("q4", "X", 1)
			 | ("q4", "b") -> ("q2", "X", 1)
			 | ("acc", "a") -> ("acc", "a", 1)
			 | ("acc", "b") -> ("acc", "b", 1)
			 | ("acc", "|") -> ("acc", "|", 1)
			 | ("acc", "X") -> ("acc", "X", 1)
			 | ("acc", "/") -> ("acc", "/", 1)
			 | (_,c) -> ("rej",c,1))}


let anbncn = { states = ["start";"q1";"q2";"q3";"q4";"q5";"q6";"acc";"rej"];
	       input_alphabet = ["a";"b";"c"];
	       tape_alphabet = ["a";"b";"c";"X";"_";">"];
	       blank = "_";
	       left_marker = ">";
	       start = "start";
	       accept = "acc";
	       reject = "rej";
	       delta = (fun inp -> match inp with
	                | ("start", "a") -> ("start", "a", 1)
     			| ("start", "b") -> ("q1", "b", 1)
			| ("start", "c") -> ("q6", "c", 1)
			| ("start", ">") -> ("start", ">", 1)
			| ("start", "_") -> ("q2", "_", 1)
			| ("q1", "b") -> ("q1", "b", 1)
			| ("q1", "c") -> ("q6", "c", 1)
			| ("q1", "_") -> ("q2", "_", 1)
			| ("q2", ">") -> ("q3", ">", 1)
			| ("q2", "a") -> ("q2", "a", 0)
			| ("q2", "b") -> ("q2", "b", 0)
			| ("q2", "c") -> ("q2", "c", 0)
			| ("q2", "_") -> ("q2", "_", 0)
			| ("q2", "X") -> ("q2", "X", 0)
			| ("q3", "X") -> ("q3", "X", 1)
			| ("q3", "_") -> ("acc", "_", 1)
			| ("q3", "a") -> ("q4", "X", 1)
			| ("q4", "a") -> ("q4", "a", 1)
			| ("q4", "X") -> ("q4", "X", 1)
			| ("q4", "b") -> ("q5", "X", 1)
			| ("q5", "b") -> ("q5", "b", 1)
			| ("q5", "X") -> ("q5", "X", 1)
			| ("q5", "c") -> ("q2", "X", 1)
			| ("q6", "c") -> ("q6", "c", 1)
			| ("q6", "_") -> ("q2", "_", 1)
		        | ("acc", "a") -> ("acc", "a", 1)
		        | ("acc", "b") -> ("acc", "b", 1)
		        | ("acc", "c") -> ("acc", "c", 1)
		        | ("acc", ">") -> ("acc", ">", 1)
		        | ("acc", "X") -> ("acc", "X", 1)
		        | ("acc", "_") -> ("acc", "_", 1)
			| (_,c) -> ("rej", c,1))}

let explode (str:string):symbol list = 
  let rec acc index result = 
    if (index<0) then result
    else acc (index-1) ((String.sub str index 1)::result) in
  acc (String.length(str)-1) []


let printConfig (m:string tm) (c:string config) (value:'a):'a = 
    let mw = List.fold_right (fun a r -> max (String.length a) r) m.states 0 in
    let padding = max 0 (c.position + 1 - List.length c.tape) in
    let rec mkBlank k = match k with 0 -> [] | _ -> m.blank :: (mkBlank (k -1)) in
    let tape' = c.tape@(mkBlank padding) in
    let _ = print_string (String.sub (c.state^(String.make mw ' ')) 0 mw) in
    let _ = print_string "  "  in
    let _ = List.iteri (fun i sym -> 
                          if (i=c.position) then Printf.printf "[%s]" sym
			  else Printf.printf " %s " sym) tape'  in
    let _ = print_newline ()  in
    value

(* QUESTION 1 *)
let test m c =	
	m.delta (c.state, List.nth (c.tape)	(c.position)) 

let fir m c=
	match test m c with 
	|(a,b,d) -> a
	|_ -> failwith "error"

let sec m c=
	match test m c with 
	|(a,b,d) -> b
	|_ -> failwith "error"

let third m c=
	match test m c with 
	(a,b,d) -> d
	| _ -> -999


let startConfig (m:'a tm) (w:string):'a config = {
	state = m.start;
	tape = m.left_marker :: explode(w);
	position = 0;
}

let acceptConfig (m:'a tm) (c:'a config):bool = 
	if c.state = m.accept then true else false
let rejectConfig (m:'a tm) (c:'a config):bool =
	if c.state = m.reject then true else false
	




let replace_nth (xs:'a list) (n:int) (x:'a):'a list = 
  let rec replace_helper xs k acc =
    match xs with
    | [] -> failwith "error"
    | x' :: xss ->
      if k = 0 then
        List.rev acc @ x :: xss
      else
        replace_helper xss (k - 1) (x' :: acc)
  in replace_helper xs n []

let startConfig (m:'a tm) (w:string):'a config = {
	state = m.start;
	tape = m.left_marker :: explode(w);
	position = 0;
}

let helpreplace m c =
	replace_nth (c.tape) (c.position) (sec m c)
let step (m:'a tm) (c:'a config):'a config = {
	state = fir m c ;
	tape = if c.position = List.length (c.tape)-1 && third m c = 1 
		then helpreplace (m) (c) @ [m.blank]
		else helpreplace m c;
	position = match third m c with 
		|0 -> c.position -1
		|1 -> c.position +1
		|_ -> failwith "error";
}



let run (m:string tm) (w:string):bool =
	let rec help k =
		match (acceptConfig m k, rejectConfig m k) with
		(true,_) -> printConfig m (k) (acceptConfig m k)
		|(false,false) -> printConfig m (k) (help (step m k))
		|(_,true) -> printConfig m (k) (acceptConfig m k)
	in help (startConfig m w)

let tm2a = { states = ["start";"re";"firstc";"secondc";"firstd";"last";"ch";"acc";"rej"];
	       input_alphabet = ["c";"d"];
	       tape_alphabet = ["c";"d";"X";"_";">"];
	       blank = "_";
	       left_marker = ">";
	       start = "start";
	       accept = "acc";
	       reject = "rej";
	       delta = (fun inp -> match inp with
	                | ("start", "c") -> ("start", "c", 1)
     			| ("start", "d") -> ("start", "d", 1)
			| ("start", ">") -> ("start", ">", 1)
			| ("start", "_") -> ("last", "_", 0)
			| ("last", "c") -> ("firstc", "X", 0)
			| ("last", "d") -> ("last", "d", 0)
			| ("last", "X") -> ("last", "X", 0)
			| ("last", ">") -> ("ch", ">", 1)
			| ("firstc", "c") -> ("secondc", "X", 0)
			| ("firstc", ">") -> ("rej", ">", 1)
			| ("firstc", "d") -> ("firstc", "d", 0)
			| ("firstc", "X") -> ("firstc", "X", 0)
			| ("secondc", "c") -> ("secondc", "c", 0)
			| ("secondc", "d") -> ("secondc", "d", 0)
			| ("secondc", "X") -> ("secondc", "X", 0)
			| ("secondc", ">") -> ("re", ">", 1)
			| ("re", "c") -> ("re", "c", 1)
			| ("re", "X") -> ("re", "X", 1)
			| ("re", "_") -> ("rej", "_", 0)
			| ("re", "d") -> ("firstd", "X", 1)
			| ("firstd", "c") -> ("firstd", "c", 1)
			| ("firstd", "X") -> ("firstd", "X", 1)
			| ("firstd", "d") -> ("firstd", "d", 1)
			| ("firstd", "_") -> ("last", "_", 0)
			| ("ch", "X") -> ("ch", "X", 1)
						| ("ch", "_") -> ("acc", "_", 0)
						| ("ch", "d") -> ("rej", "d", 1)
			| (_,c) -> ("rej", c,1))}


let tm2b = { states = ["start";"q1";"t";"toh";"h";"tot";"c";"d";"acc";"rej"];
	       input_alphabet = ["c";"d"];
	       tape_alphabet = ["c";"d";"!";"#";"_";">"];
	       blank = "_";
	       left_marker = ">";
	       start = "start";
	       accept = "acc";
	       reject = "rej";
	       delta = (fun inp -> match inp with
	                | ("start", "c") -> ("q1", "c", 1)
     			| ("start", "d") -> ("q1", "d", 1)
			| ("start", ">") -> ("start", ">", 1)
			| ("q1", "c") -> ("start", "c", 1)
			| ("q1", "d") -> ("start", "d", 1)
			| ("start", "_") -> ("t", "_", 0)
			| ("t", ">") -> ("rej", ">", 1)
			| ("t", "c") -> ("toh", "#", 0)
			| ("t", "d") -> ("toh", "!", 0)
			| ("toh", "c") -> ("toh", "c", 0)
			| ("toh", "d") -> ("toh", "d", 0)
			| ("toh", ">") -> ("h", ">", 1)
			| ("toh", "!") -> ("h", "!", 1)
			| ("toh", "#") -> ("h", "#", 1)
			| ("h", "c") -> ("tot", "#", 1)
			| ("h", "d") -> ("tot", "!", 1)
			| ("tot", "d") -> ("tot", "d", 1)
			| ("tot", "c") -> ("tot", "c", 1)
			| ("tot", "!") -> ("t", "!", 0)
			| ("tot", "#") -> ("t", "#", 0)
			| ("t", "#") -> ("c", "#", 1)
			| ("t", "!") -> ("d", "!", 1)
			| ("c", "#") -> ("acc", "#", 0)
			| ("c", "!") -> ("rej", "!", 0)
			| ("d", "!") -> ("acc", "!", 0)
		        | ("d", "#") -> ("rej", "#", 0)
			| (_,c) -> ("rej", c,1))}
let tm_q2_a : string tm = tm2a


let tm_q2_b : string tm = tm2b



