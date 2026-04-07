#Dictonarys is ordered collection
details = {'name':'tanveer','batch':49,'course': 'python'}
print(details)



#Dictonarys keys are unique
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik'}
print(details)




#Dictonarys doesn't supports indexes and slicing
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
print(details[0])1



#update value in the dictionary
#dictionary can also add the iteam if there is no key
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
details['course'] = 'c++'
details['age'] = 28
print(details)




# dictionary methods
# get(key, default_value): It returns the values if the key  is present in the dictionary otherwise it returns default
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
print(details.get('location','india'))
print(details.get('batch',48))
print(details.get('marks')) #if it not there in the dictinoary it returns the none value




#upadte(items):Dictionary updates with new items
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
new_dic = {'course': 'java','batch':50, ' location': 'india'}
details.update(new_dic)
print(details)




details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
print(details.keys()) #it returns the list of dictionary keys
print(details.values()) #it returns list of dictionary
print(details.items()) #it returns list of tuple of key-value pairs
print(type(list(details.items())))




#pop(key): It returns the values and removes the items from dictionary if key is present, otherwise keyError 
#popitem(): It return and removes the lastname
details = {'name':'tanveer','batch':49,'course': 'python','name':'shaik' ,0:1}
print(details.pop('name'))
print(details.popitem())
print(details)
print(len(details))
