"""#adding contact into phone book"""
def add_contacts(name:str, mobile:int):
    if(name not in contacts):
        contacts[name]=mobile
        return "contact added"
    return "contact already exits"
"""updating cotcts in the phone book"""
def update_contact(name:str, mobile:int):
    if(name in contacts):
        contacts[name]=mobile
        return "contact updated"
"""removing conacts from the phone book"""
def remove_contacts(name:str, mobile:int):
    if(name in contacts):
        contacts.pop(name)
        return "contacts are removed"
"""Entering all the contacts in the phone book"""
def All_contacts(name:str,mobile:int):
    for name, mobile in contacts:
        return name, mobile
"""printing all the data"""
contacts = {"Kaushik":8074944420,"Ram":9849757793,"Vamshi":9542000718,"tanveer":9963241653,"chaitran":8639462003,"Nithin":9502297660,"ashok":7997248743}
print(contacts)
print(update_contact("Ram",8074955420))
print(add_contacts("kaushik",9849757793))
print(remove_contacts("chaitran",8639462003))
print(remove_contacts("tanveer",9963241653))
print(contacts)
