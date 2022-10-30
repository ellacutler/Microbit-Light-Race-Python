from microbit import *
import radio
import speech
import microbit
import log
import music

run_count = 1
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
    print(str(val))
    if val=="2" or val == "":
        # display.scroll("button pressed")
        firstLightVal = display.read_light_level()
        # count += 1
        # display.show(str(count))
        if count == 1:
            display.scroll(firstLightVal)

        default_light_level_sender = display.read_light_level()
        music.pitch(600)
        sleep(200)
        music.stop()
        
        while display.read_light_level() > 0.7 * default_light_level_sender:
            continue
        radio.send("1")
        #val = ""
        music.pitch(900)
        sleep(225)
        music.stop() 
        #speech.say("go", throat=125,speed=140,mouth=0,pitch=30)
        #speech.say("stop", throat=120,speed=160,mouth=0,pitch=30)
        display.clear()
    # number shouldn't matter b/c everyone is on a different radio
    # speech.say("ready!")

    val = radio.receive()
    print(str(radio.receive()))
    print(str(val))
    if val == "1":
        display.scroll("Hi") # only activating after second light is hit?
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
        elasped_seconds = (end_time - start_time) / 100
        music.pitch(900)
        sleep(225)
        music.stop() 
        #speech.say("done!", throat=125,speed=140,mouth=0,pitch=30)
        speech.say(str(elasped_seconds)+"Seconds")
        
        log.add({"StudentNumber":run_count, "Seconds":elasped_seconds})  # records
        radio.send("2")
        display.scroll(elasped_seconds)

