import subprocess
import variables

class apiparser:

	__jdk = variables.jdk
	__encoding = variables.encoding
	__classpath = variables.classpath
	__name_of_java_file = variables.api_java_file
	address_list = []
	api_list = []
	has_dynamic_list = []
	has_encryption_list = []
	has_network_list = []

	def __init__(self, APK):
		self.api_exist = False
		api_cmd = self.__jdk+" "+self.__encoding+" "+self.__classpath+" "+self.__name_of_java_file+" "+APK
		api_cmd = api_cmd + " | awk '{if(NR>6)print}'"
		self.set_address_and_api(api_cmd)
		self.set_api_vectors()
		self.has_dynamic_list = self.to_byte(self.has_dynamic_list)
		self.has_network_list = self.to_byte(self.has_network_list)
		self.has_encryption_list = self.to_byte(self.has_encryption_list)
		#self.toString()

	def set_address_and_api(self, api_cmd):
		api_subp = subprocess.Popen(['/bin/sh', '-c', api_cmd], stdout=subprocess.PIPE)
		out = api_subp.communicate()[0]
		apiaddr_list = out.splitlines()
		for line in apiaddr_list:
			line = line.strip("\t")
			apiaddr = line.split("\t", 1)
			if apiaddr[0] == '':
				continue
			else:
				address = apiaddr[0]
				api = apiaddr[1]
				self.address_list.append(address)
				self.api_list.append(api)
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

	def toString(self):
		for i in range(len(self.api_list)):
			print("Address: " + self.address_list[i] + "\tAPI:\t" + self.api_list[i])
			print("DYN: "+self.has_dynamic_list[i]+"\t\tENC: "+self.has_encryption_list[i]+"\t\tNET: "+self.has_network_list[i])