#A python program using lambda to find whether all the elements in list areeither int or string 
#iitialize the list 
Data = ["get",12.0,3.76,9,"list"]
for i in Data:
    result = lambda a:a.isdigit()

    if (result==True):
        print("Integer")
    else:
        print("String")