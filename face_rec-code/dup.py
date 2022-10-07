import hashlib

#1
output_file_path = "C:/Users/Aswathi/Desktop/att/webatt/face_rec-code/attend.txt"
input_file_path = "C:/Users/Aswathi/Desktop/att/webatt/face_rec-code/attendance.txt"

#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, "w")
#4
for line in open(input_file_path, "r"):
	#5
	hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
	#6
	if hashValue not in completed_lines_hash:
		output_file.write(line)
		completed_lines_hash.add(hashValue)

#7

with open('attendance.txt','a') as f:
           f.truncate(0)



output_file.close()
f=open('attend.txt',"r")
#z=(f.read())

#print(z)
rez = []
rez1 = []
rez.insert(0,f.read())
print(rez)
for x in rez:
    rez1.append(x.replace("\n", ","))

print("New list : " + str(rez1))

data=str(rez1)
print(data)
from url import thin
thin(data)
# with open('display.txt','w') as d:
# 	d.write(data)

