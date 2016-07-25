import subprocess
import re

class intentparser:

	intent_list = []

	def __init__(self, apk):
		self.intent_exist = False
		intent_cmd = "aapt d xmltree " + "'" + apk + "'" + " AndroidManifest.xml | grep android.intent."
		self.set_intent_list(intent_cmd)
		#self.toString()

	def set_intent_list(self, intent_cmd):
		intent_subp = subprocess.Popen(['/bin/sh', '-c', intent_cmd], stdout=subprocess.PIPE)
		out = intent_subp.communicate()[0]
		intent_list = out.splitlines()
		for intent in intent_list:
			quoted = re.compile('"[^"]*"')
			found = quoted.findall(intent)[0]
			found = found.replace("\"","")
			self.intent_list.append(found)
		if len(self.intent_list) != 0:
			self.intent_exist = True
		

	def toString(self):
		for intent in self.intent_list:
			print(intent)