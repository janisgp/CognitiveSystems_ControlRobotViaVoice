import speech_recognition as sr
import timeit

def record_voice():

	r = sr.Recognizer() 

	mic = sr.Microphone()

	try:
		with mic as source:
			r.adjust_for_ambient_noise(source) # helps us to deal with the background noise
			print('Speak please...')
			audio = r.listen(source, timeout=5) # records the voice from the microphone
	except:
		print('Exception during recording!', flush=True)

	try:
		text = r.recognize_google(audio, language='en-GB') # uses Google Speech API to convert voice into text (str)
	except:
		text = 'none'

	current_command = text.lower()

	with open("command_file.txt", "w") as command_file:
		if current_command == 'stop':
			command_file.write('none')
		else:
			command_file.write(current_command)
