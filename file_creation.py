#usin context manager 
'''
with open("newfile.txt","r")as f:
    print("current position ",f.tell())
    f.read(6)
    print("after read position: ",f.tell())
    f.seek(4)
    print("after seek position: ",f.tell())
    print(f.read()

with open ("pet.jpg","rb") as data:
    image_read=data.read()
    print(image_read)
#try out pip install pillow and use its functions ,use pillow to import image
tech=open("delete_file.txt","x")
print(tech)
tech.close()

file_path="delete_file.txt"
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"(file_path)deleted succesfully")
else:
    print("file doesnot exist")'''

# python objects is stored into a file-dump and memory locaton-dumps(serialization)
# python objects is stored into a file-load and memory locaton-loads(deserialization)

import pickle
data={
    "students" : ["darsana","aardra","aruna","gouri","adhithya"],
    "marks" : (70,65,59,48,53,80),
    "subject" : {"maths","eng","phy","chem","bio"},
}
#serialization - saving data to file 
with open("user data details.pkl","wb") as f:
    pickle.dump(data,f)
print("data is serialized to user details ",data)

with open("user data details.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print("Data Read From tha pickle :",loaded_data)

#serialization - saving data in memory
dump_data=pickle.dumps(data)
print("data is serialized to bytes: ",dump_data)

loaded_data=pickle.loads(dump_data)
 
# jaison module is used fo sharng data btw diff systems eg: sending data from python backend to react frontend
# pickle module is used for saving python objects eg: saving a trained ml model or py object