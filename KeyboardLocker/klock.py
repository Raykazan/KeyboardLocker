#!/usr/bin/env python3

import dbus
import subprocess

__doc__ = """
    Author: Eviner Santos
    Description: Utility to lock the default laptop keyboard.
    How To: Open the aplication to disable the keyboard, the open again to enable the keyboard.
"""

status_file = open(".keyboard_current_status", 'r')
status = status_file.readline()
status_file.close()
status_writer = open(".keyboard_current_status", "w")

default_keyboard  = "'AT Translated Set 2 keyboard'"
title             = "Keyboard Locker"

if (status == 'disabled'):
    icon              = "input-keyboard-virtual-on"
    text              = "ON - Keyboard connected!"
    subprocess.call("xinput enable " + default_keyboard, shell=True)
    status_writer.write("enabled")
    
else:
    icon              = "input-keyboard-virtual-off"
    text              = "OFF - Keyboard disconnected!"
    subprocess.call("xinput disable " + default_keyboard, shell=True)
    status_writer.write("disabled")
    
status_writer.close()
item              = "org.freedesktop.Notifications"
path              = "/org/freedesktop/Notifications"
interface         = "org.freedesktop.Notifications"
app_name          = "Keyboard Locker"
id_num_to_replace = 0
actions_list      = ["action1", "OK"]
#hint              = {}
time              = 5000   # Use seconds x 1000

bus = dbus.SessionBus()
notif = bus.get_object(item, path)
notify = dbus.Interface(notif, interface)
notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, {}, time)
