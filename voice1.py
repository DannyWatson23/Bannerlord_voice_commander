import speech_recognition as sr
import sys
import time
import logging
logging.basicConfig(filename='out.log', level=logging.DEBUG)
#TODO: Need to be able to disable listen feature after battle

K0 = 0x0B
K1 = 0x02
K2 = 0x03
K3 = 0x04
K4 = 0x05
K5 = 0x06
K6 = 0x07
K7 = 0x08
K8 = 0x09


F1 = 0x3B
F2 = 0x3C
F3 = 0x3D
F4 = 0x3E
F5 = 0x3F
F6 = 0x40
F7 = 0x41
F8 = 0x42
ctrl = 0x1D


import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# while (True):
    # PressKey(0x11)
    # time.sleep(0.5)
    # ReleaseKey(0x11)
    # time.sleep(0.5)



r = sr.Recognizer()

def match(first, second): 
  
    # If we reach at the end of both strings, we are done 
    if len(first) == 0 and len(second) == 0: 
        return True
  
    # Make sure that the characters after '*' are present 
    # in second string. This function assumes that the first 
    # string will not contain two consecutive '*' 
    if len(first) > 1 and first[0] == '*' and  len(second) == 0: 
        return False
  
    # If the first string contains '?', or current characters 
    # of both strings match 
    if (len(first) > 1 and first[0] == '?') or (len(first) != 0
        and len(second) !=0 and first[0] == second[0]): 
        return match(first[1:],second[1:]); 
  
    # If there is *, then there are two possibilities 
    # a) We consider current character of second string 
    # b) We ignore current character of second string. 
    if len(first) !=0 and first[0] == '*': 
        return match(first[1:],second) or match(first,second[1:]) 
  
    return False

def test(first, second): 
    if match(first, second): 
        print("Yes")
    else: 
        print("No")

	
# go there - are there


def follow():
	KeyPress(F1)
	KeyPress(F2)
	print("Following!")
def hold_position():
	KeyPress(F1)
	KeyPress(F1)
	print("Moving to position")
	
def charge():
	KeyPress(F1)
	KeyPress(F3)
	print("Charging to mount and blade the enemy.")

def advance():
	KeyPress(F1)
	KeyPress(F4)
	print("Advancing, you'll probs forget that you made us do this.")
	
def fall_back():
	KeyPress(F1)
	KeyPress(F5)
	print("Falling back, you'll probs forget and wonder where the fuck we are in like 40 seconds...")

def stop():
	KeyPress(F1)
	KeyPress(F6)
	print("Stopping still.")
	
def retreat():
	KeyPress(F1)
	KeyPress(F7)
	print("Fly you fools!")
	
def face_enemy():
	KeyPress(F2)
	KeyPress(F2)
	print("Facing enemy.")

def look_here():
	KeyPress(F2)
	KeyPress(F1)
	print("Looking at direction.")

def form_line():
	KeyPress(F3)
	KeyPress(F1)
	print("Forming a line formation")

def form_shield_wall():
	KeyPress(F3)
	KeyPress(F2)
	print("Forming a shield wall! If I don't have shields, RIP in pip.")

def loose_formation():
	KeyPress(F3)
	KeyPress(F3)
	print("Spreading out.")

def circle_formation():
	KeyPress(F3)
	KeyPress(F4)
	print("Forming circle.")

def square_formation():
	KeyPress(F3)
	KeyPress(F5)
	print("Forming square.")
	
def form_skein():
	KeyPress(F3)
	KeyPress(F6)
	print("Forming skein")

def form_column():
	KeyPress(F3)
	KeyPress(F7)
	print("Forming column.")

def scatter():
	KeyPress(F3)
	KeyPress(F8)
	print("Scatting")
	
def Hold_and_fire_at_will():
	KeyPress(F4)
	print("Firing at will, or not, one of the two.")
	
def dismount_and_mount():
	KeyPress(F5)
	print("Dismounting or mounting")

def delegate_control():
	KeyPress(F6)
	print("Switching command to sergeants")
	
def infantry(text):
	KeyPress(K1)
	if len(text.split()) == 1:
		print("Nothing left to do")
	else:
		print("Infantry!")
		data = text.split()
		decide_task(data, text)
			
def archers(text):
	KeyPress(K2)
	if len(text.split()) == 1:
		print("Nothing left to do")
	else:
		print("Archers!")
		data = text.split()
		decide_task(data, text)
def melee_cavalry(text):
	KeyPress(K3)
	if len(text.split()) == 1:
		print("Nothing left to do")
	else:
		print("Cavalry!")
		data = text.split()
		decide_task(data,text)

def horse_archers(text):
	KeyPress(K4)
	if len(text.split()) == 1:
		print("Nothing left to do")
	else:
		print("Horse archers!")
		data = text.split()
		decide_task(data,text)

def skirmishers(text):
	KeyPress(K5)
	if len(text.split()) == 1:
		print("Nothing else to do")
	else:
		print("Skirmishers!")
		data = text.split()
		decide_task(data,text)

def everyone(text):
	KeyPress(K0)
	if len(text.split()) == 1:
		print("Nothing else to do")
	else:
		print("Everyone!!!!!!")
		data = text.split()
		decide_task(data,text)

def heavy_infantry(text):
	KeyPress(K6)
	if len(text.split()) == 1:
		print("Nothing else to do")
	else:
		print("Heavy Infantry!")
		data = text.split()
		decide_task(data,text)
def light_cavalry(text):
	KeyPress(K7)
	if len(text.split()) == 1:
		print("Nothing else to do")
	else:
		print("Light Cavalry!")
		data = text.split()
		decide_task(data,text)
def heavy_cavalry(text):
	KeyPress(K8)
	if len(text.split()) == 1:
		print("Nothing else to do")
	else:
		print("Heavy Cavalry!")
		data = text.split()
		decide_task(data,text)
def decide_task(data, text):
	if "llow" in data[1]:
			follow()
	elif "osition" in data[1] or "hold" in data[1] or "wait" in data[1]:
		  hold_position()
	elif "rge" in data[1] or "harge" in data[1] or "attack" in data[1]:
			charge()
	elif "vance" in data[1] or "forward" in data[1] or "go" in data[1]:
			advance()
	elif "fall" in data[1] or "back" in data[1] or "return" in data[1]:
			fall_back()
	elif "stop" in data[1] or "halt" in data[1] or "stop" in data[1]:
			stop()
	elif "run" in data[1] or "retreat" in data[1] or "run mother fuckers" in text or "run motherfuckers" in text or "run m**********" in text or "hold please" in text or "Gold please" in text:
			retreat()
	elif "face" in data[1] or "meet" in data[1] or "meat" in data[1]:
			face_enemy()
	elif "look" in data[1] or "luck" in data[1] or "yeah" in data[1]:
			look_here()
	elif "line" in data[1] or "single" in data[1]:
			form_line()
	elif "shield" in data[1] or "wall" in data[1]:
			form_shield_wall()
	elif "loose" in data[1] or "spread" in data[1]:
			loose_formation()
	elif "circle" in data[1]:
			circle_formation()
	elif "quare" in data[1]:
			square_formation()
	elif "skein" in data[1] or "arrow" in data[1] or "screen" in data[1] or "that weird arrow thing" in text:
			form_skein()
	elif "column" in data[1] or "rank" in data[1]:
			form_column()
	elif "ire at" in text:
			Hold_and_fire_at_will()
	elif "mounty" in text or "horses" in text:
			dismount_and_mount()
	elif "simon" in text or "lars" in text or "sally feet pics" in text:
			delegate_control()

def KeyPress(key):
	print(key)
	PressKey(key)
	time.sleep(0.5)
	ReleaseKey(key)
	time.sleep(0.5)
	print("Finished pressing key")

def listen(wsh):
	wsh.AppActivate('Bannerlord.Native.exe')
	print('Before listening')
	with sr.Microphone() as source:
		print("Speak anything")
		audio = r.listen(source, timeout=3, phrase_time_limit=3)
		try:
			text = r.recognize_google(audio)
			print("You said {}".format(text))
		except:
			print("Sorry could not recognize voice, I'm retarded I know...")
		with open('text_output', 'a') as file:
			file.write(str(text) + '\n')
	if "exit" in text:
		print("exiting")
		return False
	if "one" in text or "won" in text or "1" in text:
		infantry(text)
	elif "two" in text or "to" in text or "2" in text or "do" in text:
		archers(text)
	elif "three" in text or "tree" in text or "3" in text:
		melee_cavalry(text)
	elif "four" in text or "for" in text or "4" in text:
		horse_archers(text)
	elif "5" in text or "five" in text or "hive" in text or "I've" in text:
	    skirmishers(text)
	elif "six" in text or "sex" in text or "6" in text:
		heavy_infantry(text)
	elif "seven" in text or "sev" in text or "7" in text:
		light_cavalry(text)
	elif "eight" in text or "ight" in text or "8" in text:
		heavy_cavalry(text)
	elif "everybody" in text or "guys" in text or "soldiers" in text:
		everyone(text)
	return True	
def main():
	try:
		wsh = client.Dispatch('WScript.Shell')
	except Exception as e:
	    print(e)
	br_cond = True
	while br_cond == True:
		try:
			br_cond = listen(wsh)
		except Exception as e:
			print(e)
			pass

if __name__ == "__main__":
 main()