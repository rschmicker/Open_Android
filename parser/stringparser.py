import subprocess
import re
import sys
import variables
# To run RAPID in command line:
# /Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home/bin/java 
#-Dfile.encoding=UTF-8 
#-classpath /Users/rschmicker/Documents/RAPID/Code/Parser/bin:/Users/rschmicker/Documents/RAPID/Rapid0.2.jar StringParser
# Must be in RAPID dir

class stringparser:

	__jdk = variables.jdk
	__encoding = variables.encoding
	__classpath = variables.classpath
	__name_of_java_file = variables.string_java_file
	has_IP_list = []
	has_Phone_list = []
	has_URL_list = []
	has_Sys_Cmd_list = []
	all_strings = []

	def __init__(self, APK):
		self.strings_exist = False
		string_cmd = self.__jdk+" "+self.__encoding+" "+self.__classpath+" "+self.__name_of_java_file+" "+APK
		string_cmd = string_cmd + " | awk '{if(NR>6)print}'"
		self.all_strings = self.get_all_strings(string_cmd)
		#self.has_IP_list = self.to_byte(self.has_IP_list)
		#self.has_Phone_list = self.to_byte(self.has_Phone_list)
		#self.has_URL_list = self.to_byte(self.has_URL_list)
		#self.has_Sys_Cmd_list = self.to_byte(self.has_Sys_Cmd_list)
		#self.toString()

	def get_all_strings(self, string_cmd):
		string_subp = subprocess.Popen(['/bin/sh', '-c', string_cmd], stdout=subprocess.PIPE)
		out = string_subp.communicate()[0]
		string_list = out.splitlines()
		#for string in string_list:
			#searchIP = re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", string)
			#searchPhone = re.search("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", string)
			#searchURL = re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?", string)
			#if searchIP:
			#	self.has_IP_list.append('1')
			#else:
			#	self.has_IP_list.append('0')
			#if searchPhone:
			#	self.has_Phone_list.append('1')
			#else:
			#	self.has_Phone_list.append('0')
			#if searchURL:
			#	self.has_URL_list.append('1')
			#else:
			#	self.has_URL_list.append('0')
			#for cmd in self.__system_cmd_list:
			#	if string.find(" " + cmd + " ") != -1 or string.startswith(cmd) == True:
			#		self.has_Sys_Cmd_list.append('1')
			#		break
			#	elif self.__system_cmd_list[len(self.__system_cmd_list)-1] == cmd:
			#		self.has_Sys_Cmd_list.append('0')
		if len(string_list) != 0:
			self.strings_exist = True
		return string_list

	def to_byte(self, list):
		temp_list = []
		temp_string = ""
		for bit in list:
			if len(temp_string) == 8:
				byte = int(temp_string, 2)
				temp_list.append(byte)
				temp_string = ""
			temp_string = temp_string + bit
		return temp_list

	def toString(self):
		for i in range(len(self.all_strings)):
			print(self.all_strings[i])
			print("IP: " + self.has_IP_list[i] + "\t\tPhone: " + self.has_Phone_list[i])
			print("URL: " + self.has_URL_list[i] + "\t\tSys: " + self.has_Sys_Cmd_list[i])