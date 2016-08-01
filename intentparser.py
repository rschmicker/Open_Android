import variables

class intentparser:

	intent_list = []

	def __init__(self, apk):
		self.intent_exist = False

		out_apk = apk.strip(".apk")
		out_apk = out_apk.split("/")[-1]
		self.manifest = variables.decoded_apk_dir + out_apk + "/AndroidManifest.xml"
		self.set_intent_list()

	def set_intent_list(self):
		file = open(self.manifest,"r")
		for line in file:
			if line.find("android.intent") != -1:
				self.intent_list.append(line.split("\"")[1])
		if len(self.intent_list) != 0:
			self.intent_exist = True