#***********************************************************Basic Dictionary Programs********************************************
# Python | Sort Python Dictionaries by Key or Value

inp = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#
# o/p = {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

#Sort by key or values
print(sorted(inp.items()))



#Sort by values only
#print(sorted(inp.items(), key=lambda item: item[1]))

#Sort by keys
#print(sorted(inp.items(), key=lambda item: item[0]))

# Handling missing keys in Python dictionaries

missing_key="name"
dic={"age":23,"address":"ind"}
for i in dic:
    if i=='name':
        print("Yes present")
    else:
        print("missing")




# Python program to find the sum of all items in a dictionary

Input = {'a': 100, 'b':200, 'c':300}
# Output : 600

sum=0
for i in Input.values():
    sum=sum+i
print(sum)



# Python program to find the len of a Dictionary


print(len(Input))





# Ways to sort list of dictionaries by values in Python – Using itemgetter



# Ways to sort list of dictionaries by values in Python – Using lambda function

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]


print(sorted(lis, key=lambda i: i['age']))

print(sorted(lis, key=lambda i: i['age'] , reverse=True))

# Python | Merging two Dictionaries

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
# Output: {'a': 10, 'b': 8, 'd': 6, 'c': 4}

dict1.update(dict2)
print(dict1)



# Python – Insertion at the beginning in OrderedDict


original_dict = {'a':1, 'b':2}
item_to_be_inserted = ('c', 3)

#Output:  {'c':3, 'a':1, 'b':2}


dic2 = {'c':3}
dic2.update(original_dict)
print(dic2)





# Python | Find common elements in three sorted arrays by dictionary intersection

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(list(set(ar1).intersection(ar2).intersection(ar3)))
#Output:  [80, 20]


# Python – Key with maximum unique values

# Input :
#test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output : "Gfg"
# Explanation : "Gfg" having max unique elements i.e 5.

dic={}
for key,val in test_dict.items():
    dic[key]=len(list(set(val)))
for k,v in dic.items():
    if v==max(dic.values()):
        print(k)




# Find all duplicate characters in string


ip='geeksforgeeeks'

lis=[]
dupli_lis=[]
for i in ip:
    if i not in lis:
        lis.append(i)
    else:
        dupli_lis.append(i)
print(list(set(dupli_lis)))



# Python – Group Similar items to Dictionary Values List


# Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
# Explanation : Similar items grouped together on occurrences.






# Python – Replace String by Kth Dictionary value


test_list = ['Gfg', 'is', 'Best']
subs_dict = {'Gfg' : [5, 6, 7], 'is' : [7, 4, 2]}
K = 0
# Output : [5, 7, “Best”]

test_dict1=[]
for k,v in subs_dict.items():
    for j in test_list:
        if j==k:
            test_dict1.append(v[0])
            test_list.remove(j)

print(test_dict1+test_list)














#***********************************************Advanced dic programs**********************************************************

#Python – Reverse Dictionary Keys Order

# The original dictionary :
# {‘is’: 2, ‘best’: 5, ‘gfg’: 4}
# The reversed order dictionary :
# OrderedDict([(‘gfg’, 4), (‘best’,5), (‘is’, 2)])

dic={'is': 2,'best': 5, 'gfg': 4}
lis=[]
lis1=[]
for k,v in dic.items():
    lis.append(k)
    lis1.append(v)
list(zip(lis,lis1))




# Python – Extract Key’s Value, if Key Present in List and Dictionary
# Input : \
#     test_list = ["Gfg", "is", "Good", "for", "Geeks"]
#    test_dict = {"Gfg" : 5, "Best" : 6}, K = "Gfg"
# Output : 5
# Explanation : "Gfg" is present in list and has value 5 in dictionary.

for k,v in test_dict.items():
    if k in test_list:
        print(val)

