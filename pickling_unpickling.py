# pickling and unpickling -
# basically used for serializing(store) and de-serializing(read) python object structure

# pickling
import pickle
name= ["Harry","Sen","Joy"]
skill= ["Python","SQL","Java"]
pickle_file=open("emp1.txt",'wb ')
pickle.dump(name,pickle_file)
pickle.dump(skill, pickle_file)
pickle_file.close()

# unpickling
import pickle
pickle_file=open("emp1.txt","rb")
name_list=pickle.load(pickle_file)
skill_list=pickle.load(pickle_file)
print(name_list)
print(skill_list)
