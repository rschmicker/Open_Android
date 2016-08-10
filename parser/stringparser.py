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
	__classpath =  "-cp " + variables.code_location + ":" + variables.classpath
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

	def get_all_strings(self, string_cmd):
		string_subp = subprocess.Popen(['/bin/sh', '-c', string_cmd], stdout=subprocess.PIPE)
		out = string_subp.communicate()[0]
		string_list = out.splitlines()
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