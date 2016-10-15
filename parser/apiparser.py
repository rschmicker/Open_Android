import subprocess
import variables

class apiparser:

	__jdk = variables.jdk
	__encoding = variables.encoding
	__classpath =  "-cp " + variables.code_location + ":" + variables.classpath
	__name_of_java_file = variables.api_java_file
	api_list = []
	has_dynamic_list = []
	has_encryption_list = []
	has_network_list = []

	def __init__(self, APK):
		self.api_exist = False
		api_cmd = self.__jdk+" "+self.__encoding+" "+self.__classpath+" "+self.__name_of_java_file+" "+APK
		api_cmd = api_cmd + " | awk '{if(NR>6)print}'"
		self.set_api(api_cmd)

	def set_api(self, api_cmd):
		api_subp = subprocess.Popen(['/bin/sh', '-c', api_cmd], stdout=subprocess.PIPE)
		out = api_subp.communicate()[0]
		self.api_list = out.splitlines()
		if len(self.api_list) != 0:
			self.api_exist = True

	def set_api_vectors(self):
		for api in self.api_list:
			if api.find("reflect") != -1:
				self.has_dynamic_list.append('1')
			else:
				self.has_dynamic_list.append('0')
			if api.find("android.net") != -1 or api.find("java.net") != -1:
				self.has_network_list.append('1')
			else:
				self.has_network_list.append('0')
			if api.find("javax.crypto") != -1:
				self.has_encryption_list.append('1')
			else:
				self.has_encryption_list.append('0')

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
