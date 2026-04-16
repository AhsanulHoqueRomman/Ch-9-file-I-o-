'''
rom= a very long string.

emails=[]
34 seconds

'''

'''
In open function for opening files,it takes 2 parameters.
1.Filename 
2.Mode(Read(r),write(w),append(a),update(+),read in binary mode(rb),read in text mode(rt))
But By default the second mode is read.If we don't write anything between read and write it will read the file.
But If we want to write anything in that file we must declare the mode.
'''

#Read from a File:

f= open("file.txt")   #f=open("file.txt", "r")  [Both are right]
data=f.read()
print(data)
f.close()

#With Statement:

#The same above code can be written using with statment.

with open("file.txt") as f:
    print(f.read())

#We don't have to close the file wxplicitly!
