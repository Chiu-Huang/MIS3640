let rec set_size (xs:'a list):int = 
  match xs with 
  [] -> 0
  | a::b -> (let ref loop = !loop +1) 
  and set_size (b);;
