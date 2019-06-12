#!/usr/bin/env python3

import keyboard

def wait_for_key_combination(key="`"):
	#Wait for the user to press a key combination
	print("They are not in cooltext")
	keyboard.wait("alt", suppress=False)
	keyboard.wait(key, suppress=False)
	#once these keys have been pressed, the program can continue
	print("They want to start cooltext")

def make_cooltext(is_uppercase_turn=False):
	#wait for them to press a key and then record that event
	key  = keyboard.read_event(suppress=True)
	name = key.name

	#If they are not pressing down a key, then we should just ignore the event
	if key.event_type != "down": 
		return make_cooltext(is_uppercase_turn=is_uppercase_turn)
		
	if name == "esc":
		#If they press the escape key, then they want to stop doing the 
		#Cooltext. Once they press the escape buttton, it will recurse 
		#the main funciton, and will again wait for the key combination
		return main( )

	if len(name) != 1: 
		#any time that the length is longer than one it is a special key
		#We should stil send special keys as well, because they cannot have
		#an uppercase version. 
		keyboard.send(name)
		return make_cooltext(is_uppercase_turn=is_uppercase_turn)

	#write the uppercase version of the letter if it is an alternate keypress
	keyboard.write(name.upper() if is_uppercase_turn else name)

	#toggle the boolean value
	return make_cooltext(is_uppercase_turn=not is_uppercase_turn)

def main( ):
	wait_for_key_combination( )
	make_cooltext( )
	
if __name__=="__main__":
	main( )

