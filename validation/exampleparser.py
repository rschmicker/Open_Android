import variables

class exampleparser:

	apk_dir = ""
	decoded_dir = ""
	key = ""
	value = []	

	def __init__(self, APK):
		self.apk_dir = APK
		self.decoded_dir = APK.strip('.apk')
		self.decoded_dir = self.decoded_dir.split('/')[-1]
		self.decoded_dir = variables.decoded_apk_dir + self.decoded_dir
		self.parse_feature()
	
	def parse_feature(self):
		#parse feature here
		self.key = 'Im a key!'
		self.value = ['hello', 'world']

