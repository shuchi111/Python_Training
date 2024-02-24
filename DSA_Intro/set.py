#set concepts
mysets = {
    " Shuchi ", " Shukla"," kumbhaj", " pious"
}
# iteration
for temp_obj in mysets:
    print( temp_obj)
print( " total objects: ", len( mysets))
name = " shuchi"
print( " total characters", len( name))
print( mysets)
mysets.pop() # last item will be deleted
mysets.add( " my new object")
mysets.add( " one more")
for temp_obj in mysets:
    print( temp_obj)
print( " data type of ", type( mysets))
print( " memory location/ address", id( mysets))
# creating objects by using constructor set
mysets1 = set( ( "shuchi", " sweet", " baby "))
print(mysets1)
# python supports functional programming / object oriented programming / reactive programming, 
# procedural based programming, script programming
