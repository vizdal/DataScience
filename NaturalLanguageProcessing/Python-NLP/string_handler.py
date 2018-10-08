#!/usr/bin/python

some_list = ["first_name","last_name","age","occupation"]
some_tuple = ("John","Holloway",35,"carpenter");
result = {some_list[i]:v for i,v in enumerate(some_tuple)}
print result #prints an dictionary with first_name set to John , second_name set to Holloway and so on 
