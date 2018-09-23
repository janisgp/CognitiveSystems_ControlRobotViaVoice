# some imports 
import speech_recognition as sr

def record_voice():
	"""
	does a voice recording and converts it to speech via google api
	if current_command obtained from audio signal is not equal to 
	none we update the current command in command_file.txt
	"""
	
	r = sr.Recognizer() 

	mic = sr.Microphone()
	
	# get audio from mic
	with mic as source:
		r.adjust_for_ambient_noise(source) # helps us to deal with the background noise
		print('Speak please...')
		audio = r.listen(source, timeout=10) # records the voice from the microphone
		print('Stop please...')
	
	# converte to text via google api
	try:
		text = r.recognize_google(audio, language='en-GB') # uses Google Speech API to convert voice into text (str)
	except:
		text = 'none'
	
	current_command = text.lower()
	
	if current_command != 'none':
	
		########## TO-DO ###############
		# map to given commands
		# Damians code/function call
		################################

		# update command file
		with open("command_file.txt", "w") as command_file:
			if current_command == 'stop':
				command_file.write('none')
			else:
				command_file.write(current_command)		