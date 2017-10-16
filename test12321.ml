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



let k = test tm2a (startConfig tm2a "ccccccddd");;
sec tm2a (startConfig tm2a "ccccccddd")