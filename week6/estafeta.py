"1"


"2"



"3"

# class MyString(str):
#     def __init__(self, string):
#         self.string = string

#     def append(self, other):
#         self.string = self.string + other
#         return self.string

#     def pop(self):
#         poped = self.string[-1]
#         self.string = self.string[:-1]
#         return poped

# string1 = MyString('Hello')
# print(string1.append('World'))
# print(string1.pop())



"4"
# class MyDict(dict):
#     def __init__(self, dict_):
#         self.dict_ = dict_

#     def get(self, key, default = 'Are you kidding?'):
#         return self.dict_.get(key, default)

# object = MyDict({'a':1,'b':2})
# print(object.get('k'))

"5"

# class ContactList(list):
#     def __init__(self,list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         names = [i for i in self.list_ if name in i]
#         print(names)

# all_contacts = ContactList(['Jane', "Jane Foster",'Kil'])
# all_contacts.search_by_name('Jane')




"6"


"7"

# class RadioMixin:
#     def play_music(title):
#         print(f'Песня называется {title}')
    
# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass
# class Amphibian(Auto,Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('Happy')
# boat.play_music('Believe')
# obj.play_music('opa')

"8"
class MyList(list):
    def __init__(self, list_):
        self.list_ = list_
    def __getitem__(self,index):
        return self.list_[index -1]

list1 = MyList([1,2,3,4])
print(list1[1])