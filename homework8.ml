(* 

HOMEWORK 8

Name: Ching Chiu Huang 

Email: chuang2@babson.edu

Remarks, if any:

*)

module AbsStream :
sig
    type 'a stream 
    val cst : 'a -> 'a stream
    val fby : 'a stream -> (unit -> 'a stream) -> 'a stream
    val map : ('a -> 'b) -> 'a stream -> 'b stream
    val map2 : ('a -> 'b -> 'c) -> 'a stream -> 'b stream -> 'c stream
    val filter : ('a -> 'b -> bool) -> 'a stream -> 'b stream -> 'b stream
    val split : 'a stream -> ('a stream * 'a stream)
    val print_stream : ('a -> string) -> int -> 'a stream -> unit
  end = 
struct
  type 'a stream = R of 'a * (unit -> 'a stream)
  let memoize f = 
    let memoized = ref None in
    let new_f () = 
match !memoized with
| None -> let result = f () in memoized := Some result; result
| Some v -> v   in
    new_f
  let f1 h t = R (h, memoize t) 
  let f2 s = let R (h,t) = s in h
  let f3 s = let R (h,t) = s in t ()
  let rec cst v = f1 v (fun () -> cst v)
  let fby s1 ps2 = f1 (f2 s1) ps2
  let rec map f s = f1 (f (f2 s)) (fun () -> map f (f3 s))
  let rec map2 f s1 s2 = f1 (f (f2 s1) (f2 s2)) (fun () -> map2 f (f3 s1) (f3 s2))
  let rec filter p ctl s = if p (f2 ctl) (f2 s) then f1 (f2 s) (fun () -> filter p (f3 ctl) (f3 s)) else filter p (f3 ctl) (f3 s)
  let split s = (cst (f2 s), f3 s)
  let rec zip s1 s2 = f1 (f2 s1, f2 s2) (fun () -> zip (f3 s1) (f3 s2))
  let rec prefix n s = if n > 0 then (f2 s)::(prefix (n-1) (f3 s)) else []
  let print_stream tr n s =
    let rec loop n s = 
      if n > 0 then (print_string ((tr (f2 s))^" "); loop (n-1) (f3 s))
      else (print_string "...>\n") in
    print_string "< " ; loop n s
end


(*
* 
* THESE ARE THE FUNCTIONS YOU GET TO USE
*
*)

type 'a stream = 'a AbsStream.stream
let cst : 'a -> 'a stream = AbsStream.cst
let fby : 'a stream -> (unit -> 'a stream) -> 'a stream = AbsStream.fby
let map : ('a -> 'b) -> 'a stream -> 'b stream = AbsStream.map
let map2 : ('a -> 'b -> 'c) -> 'a stream -> 'b stream -> 'c stream = AbsStream.map2
let filter : ('a -> 'b -> bool) -> 'a stream -> 'b stream -> 'b stream = AbsStream.filter
let split : 'a stream -> ('a stream * 'a stream) = AbsStream.split
let print_stream : ('a -> string) -> int -> 'a stream -> unit = AbsStream.print_stream




(* 
*  Some helper functions to print a stream:
*
*  They are simple wrapper around print_stream
*
*)

let pri s = print_stream string_of_int 20 s
let prip s = print_stream (fun (x,y) -> "("^(string_of_int x)^","^(string_of_int y)^")") 20 s
let prs s = print_stream (fun x -> x) 20 s
let prf s = print_stream string_of_float 20 s


(* Some functions we saw in class *)

let rec mk_nats () = fby (cst 0)
                       (fun () -> (map (fun x -> x+1) (mk_nats ())))

let nats = mk_nats ()

let evens = map (fun x -> 2*x) nats
let odds = map (fun x -> x+1) evens

let drop s = let (_,r) = split s in r
let head s = let (h,_) = split s in h
let add s1 s2 = map2 (fun x y -> x+y) s1 s2
let rec psums s = fby s (fun () -> add (psums s) (drop s))
(* let notdivides c x = x mod c <> 0
let rec sieve s = 
  let (f,r) = split s in
  fby f (fun () -> sieve (filter notdivides f r))

let primes = sieve (map (fun s -> s+2) (nats);; *)



(* test streams *)

let s_ampl =
let transf (v,(d,m)) =
  if d = 1 && v = m then (v-1,(-1,m))
  else if d = -1 && v = -m then (v+1,(1,m+1))
  else if d = 1 then (v+1,(1,m))
  else (v-1,(-1,m))  in
let rec f () = fby (map2 (fun x y -> (x,y)) (cst 0) (cst (1,1)))
                   (fun () -> map transf (f ())) in
map (fun (x,y) -> x) (f ())

let s_as = map (fun n -> "a"^(string_of_int n)) nats


(* 
* QUESTION 1 
* 
*)


let scale (n:int) (s:int stream):int stream =
  map (fun x -> n*x) s;;

let mult (s1:int stream) (s2:int stream):int stream =
  map2 (fun x y -> x*y) s1 s2;; 

let zip (s1:'a stream) (s2:'b stream):('a * 'b) stream = 
  map2 (fun x y -> (x, y)) s1 s2;;

let unzip (s:('a * 'b) stream):('a stream * 'b stream) =
  let s1 = map (fun (x, y) -> x) s in
  let s2 = map (fun (x, y) -> y) s in
  s1, s2;;


let rec fold (f:'a -> 'b -> 'b) (init_s:'b stream) (s:'a stream):'b stream =
  let t = map2 (fun x y -> f y x) init_s s in
  fby t (fun () -> map2 (fun q w -> f w q) (drop(s)) (fold (f) (init_s) (s)));;
  
let running_max (s:int stream):int stream =
  let rec helper xs max = 
    fby max (fun () -> if (head xs) > max
                       then (helper (drop xs) (head xs))
                       else (helper (drop xs) max))
  in
  helper (drop s) (head s);;


let double=
  map (fun x -> if x mod 2 == 0 then 0 else 1) nats;;



let stutter (s:'a stream):'a stream =
  let rec display xs k=
    fby (head xs) (fun () -> if (head k) == cst 1
                       then display (drop xs) (drop k)
                       else display xs (drop k))
  in display s double;;
      

  (* let rec helper hd tl k =
    fby (head k) (fun ()-> if hd == head (tl)
                       then helper (head(drop k)) (drop(drop k)) (drop k)
                       else helper (head k) (head k) k)
  in 
  helper (head s) (drop s) (s)


  let t = head (s) in 
  let k = drop (s) in 
  fby t (fun() -> if t <> head (k)
                  then 

 *)

(*
* QUESTION 2
* 
*)


let rec scalef r s = 
  map (fun x -> r *. x) s;;

let rec neg z = 
  fby z (fun () -> scalef (-1.0) (neg z)) ;;

let rec addf s t = 
  map2 (fun x y -> x +. y) s t;;

let rec psumsf s =
  fby s (fun () -> addf (drop s) (psumsf s));;

let rec arctan (z:float):float stream =
  let t = neg (cst 1.0) in
  let k = cst (z) in
  let p = map2 (fun x y -> x *. y) t k in
  let o = map2 (fun q w -> (q ** float_of_int(w))/.float_of_int(w)) p odds in
  psumsf o;;


let pi ():float stream = 
  let t = scalef (16.0) (arctan (0.2)) in
  let k = scalef (-4.0) (arctan (1.0/.239.0)) in
  addf t k;;

  
let rec newton (f:float -> float) (df:float -> float) (guess:float):float stream =
  let g1 = guess -. (f guess)/. (df guess) in
  fby (cst(guess)) (fun () -> newton f df g1);;




let add1 ns = map (fun x -> x+1) ns 
let divide n d = map2 (fun x y-> x/. y) n d
let floatd ns = map (fun x -> float_of_int(x)) ns
let minus ns ks = map2 (fun x y -> x -. y) ns ks

let helperder f ns = map (fun x -> f x) ns

let derivative (f:float -> float) (x:float):float stream =
  let rec helper func x0 ns =
    let n = floatd(head ns) in 
    let d = (divide (cst(1.0)) (n)) in 
    let der = divide (minus (helperder (func) (addf x0 d)) (helperder (func) (x0))) d in
    fby der (fun () -> helper func x0 (drop ns))
  in
  helper f (cst(x)) (add1 nats);;

let absf xs = map (fun x -> if x > 0. then 1. *. x else -1. *. x) xs

let rec limit (epsilon:float) (s:float stream):float stream =  
  let t = head (s) in
  let p = head (drop(s)) in 
  if absf (minus t p) < (cst epsilon) then (s) else limit epsilon (drop s);;
 
 