from microbit import *
import radio
import speech
import microbit
import log
import music

run_count = 0
count = 1
SecondsTimer = 0
default_light_level_sender = 0
default_light_level_reciever = 0
val = ""
radio.on()
radio.config(channel=count)
while True:
    if button_a.get_presses ==0:
        log.set_labels("StudentNumber", "Seconds")
    if button_a.was_pressed():
        # button a - first light sensor
        while True:
            firstLightVal = display.read_light_level()
            if count == 1:
                display.scroll(firstLightVal)
            default_light_level_sender = display.read_light_level()
            music.pitch(600)
            sleep(200)
            music.stop()
            while display.read_light_level() > 0.7 * default_light_level_sender:
                continue
            radio.send("1")
            print("here")
            music.pitch(900)
            sleep(225)
            music.stop() 
            display.clear()
    if button_b.was_pressed():
        
        print("button B")
        # button b - second light sensor
        while(True):
            val = radio.receive()
            print(val)
            if (val == "1" ):
                start_time = microbit.running_time()
                print("Start Time" + str(start_time))
                default_light_level_reciever = display.read_light_level()
                elasped_seconds = 0
                #speech.say("go!", throat=255,speed=100,mouth=200,pitch=125)
                
                while display.read_light_level() > 0.7 *default_light_level_reciever:
                    continue
                run_count += 1
                end_time = microbit.running_time()
                print("End Time" + str(end_time))
                elasped_seconds = (end_time - start_time) / 1000
                music.pitch(900)
                sleep(225)
                music.stop() 
                speech.say(str(elasped_seconds)+"Seconds")
                val = " " 
                log.add({"StudentNumber":run_count, "Seconds":elasped_seconds})  # records
                radio.send("2")
                display.scroll(elasped_seconds)
