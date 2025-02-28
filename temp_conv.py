# to get temp in F
# Convert to K and C 
f = float(input("Enter temp in F"))
f_to_c= (f-32) * (5/9)
print("Temp is conveted from F to C"+ str(f_to_c)+"\n")
f_to_k = f_to_c+273.15
print("temp is converted from F to K")
