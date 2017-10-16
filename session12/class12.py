def histogram(s):
    d = dict()
    for c in s.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram(s):
    d = dict()
    for letter in s.lower():
        d[letter] = d.get(letter, 0) + 1
    return d


def print_hist (s):
    for key in histogram(s):
        print (key, histogram(s)[key])


# for k,v in d.items(): # for loop can use tuples
    # print (k,v)


# d.dict_keys()




t = [3,1,2,4]
t2 = t.copy () 
t2 = t[:]   # pointing to different ts

t = ['a','b','c','d']
t.pop ()  # delete and return the last element 
t.pop (1) # delete and return 2nd element in t

del t[1:3]


names =['ching','chiu','Huang']
scores = [95,96,97]


grades = dict()
grades = {}

type(grades)

grades["ching"] = 95

grades = {'Zach':85, 'ALex': 84, 'Jullian':95}
grades ['Xiang'] = 88


# number_of_e = h.get('e', 0)    # get values of key from dictionary
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)



example = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "231",
               "short_name" : "231",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Forest Street",
               "short_name" : "Forest St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Babson Park",
               "short_name" : "Babson Park",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Wellesley",
               "short_name" : "Wellesley",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Norfolk County",
               "short_name" : "Norfolk County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Massachusetts",
               "short_name" : "MA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "02457",
               "short_name" : "02457",
               "types" : [ "postal_code" ]
            },
            {
               "long_name" : "0310",
               "short_name" : "0310",
               "types" : [ "postal_code_suffix" ]
            }
         ],
         "formatted_address" : "231 Forest St, Babson Park, MA 02457, USA",
         "geometry" : {
            "location" : {
               "lat" : 42.2993708,
               "lng" : -71.2659951
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 42.3007197802915,
                  "lng" : -71.26464611970849
               },
               "southwest" : {
                  "lat" : 42.2980218197085,
                  "lng" : -71.26734408029149
               }
            }
         },
         "place_id" : "ChIJ7xQZi0GB44kRiWrnmTgf904",
         "types" : [ "establishment", "point_of_interest" ]
      }
   ],
   "status" : "OK"
}

print (example['results'][0]["address_components"][5]['short_name'])
print (len(example['results']))



t.sort(reverse=True)

