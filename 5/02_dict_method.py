mark = {
    "paarth" : 69 , 
    "yuvraj" : 1000 ,
    "lakshay" : 45,
    0: "paarth" 

}
#print(mark.items())
#print(mark.keys())
#print(mark.values())
#mark.update({"yuvraj" : 999, "happyysingh": 100})
#print(mark)

#print(mark.get("yuvraj")) #prints none
#print(mark["yuvraj"]) #print error

print(mark.pop("yuvraj")) #removes the key and value and returns the value
print(mark)