import math

count = 0
data={}
def test_sqrt():
   num = 25
   x = math.sqrt(num)
   assert math.sqrt(num) == 5
   #out_file = open("myfile.json", "w")     
   #json.dump(math.sqrt(num) == 5, out_file, indent = 6)  

def testsquare():
   num = 7
   y = 7*7
   assert 7*7 == 40

import json  
    
# python object(dictionary) to be dumped  
dict1 ={  
    "0": {  
        "outcome": math.sqrt(25) == 5,  
        "test_case_name": "test_sqrt",  
        "atest_performed": "Suare",  
        "frames_per_second": "0.0",
        "result": [
            "sqaure: 5"
        ]
    },  
    "1": {  
        "outcome": 7*7 == 40,  
        "test_case_name": "testsquare",  
        "test_performed": "square",  
        "frames_per_second": "0.0",
        "result": [
            "sqaure: 49"
        ]
    },  
}  
    
# the json file where the output must be stored  
out_file = open("result.json", "w")  
    
json.dump(dict1, out_file, indent = 6)  
    
out_file.close() 
