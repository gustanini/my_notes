user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#use get on teracoder, default = 100k

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

#use get on superstacksmash, default = 100k

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)