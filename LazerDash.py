from microbit import *
import radio
import speech
import microbit
import log
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

    if button_a.is_pressed():
        # display.scroll("button pressed")
        firstLightVal = display.read_light_level()
        # count += 1
        # display.show(str(count))
        if count == 1:
            display.show(firstLightVal)

        default_light_level_sender = display.read_light_level()
        while display.read_light_level() > 0.8 * default_light_level_sender:
            continue
        radio.send("1")
        speech.say("go!")
        display.clear()
    # number shouldn't matter b/c everyone is on a different radio
    # speech.say("ready!")

    val = radio.receive()
    if val == "1":
        display.show("Hi")
        start_time = microbit.running_time()
        default_light_levevl_reciever = display.read_light_level()
        elasped_seconds = 0
        speech.say("go!")
        while display.read_light_level() > default_light_level_reciever:
            continue
        run_count += 1
        end_time = microbit.running_time()
        elasped_seconds = (end_time - start_time) / 1000
        speech.say("done!")
        speech.say(str(elasped_seconds))
        display.show(elasped_seconds)
        log.create_cv(StudentNumber=run_count, Seconds=elasped_seconds)  # records
        val = ""


# input.on_button_pressed_a(Button.A, on_button_pressed_a)
# still need datalogger
# still need calibration w/ laser pointers

# def on_forever():


# basic.forever(on_forever)


def on_received_number(recievedNumber, run_count):
    pass

    #


radio.on_received_number(on_received_number, run_count)
