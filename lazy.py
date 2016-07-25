f = open("sys_cmd_list.txt", "r")
temp = []
for line in f:
	line = line.replace(" ","\n")
	temp.append(line)
f.close()

f2 = open("sys_cmd_list.txt", "w")
for line in temp:
	f2.write(line)
f2.close()