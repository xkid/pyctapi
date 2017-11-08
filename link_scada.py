#! /usr/bin/env python
# DLL Needed : ctapi.dll, ct_ipc.dll, cteng32.dll, ctres32.dll, ctutil32.dll, and CiDebugHelp.dll
# Tested with Python 2.7.13 + Citect SCADA 7.5 DLL + Citect SCADA 8.0 2016
from pyctapi import adapter
import time
import signal
import sys

IP_ADDRESS = ""
CITECT_USERNAME = ""
CITECT_PASSWORD = ""
SOME_CITECT_TAG_NAME = "DO0001"

tag_dict = {}

# Test using adapter as an object
cti = adapter.CTAPIAdapter(IP_ADDRESS, CITECT_USERNAME, CITECT_PASSWORD,dll_path="7.5")
cti.connect()
print(cti.read_tag(SOME_CITECT_TAG_NAME))
cti.write_tag(SOME_CITECT_TAG_NAME, 1)
print(cti.read_tag(SOME_CITECT_TAG_NAME))

def handler_stop_signals(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

def process_tag(tag):
    current = cti.read_tag(tag)
    if tag in tag_dict.keys():
        if tag_dict[tag] <> current:
            tag_dict[tag] = current
            print(current)
            print(tag_dict)
    else:
        tag_dict[tag] = current
        print(current)
        print(tag_dict)ain=True)

while True:
    process_tag("DO0001")
    process_tag("D0002")
    process_tag("R0001")
    process_tag("Rawang_Motor_1")
    
    time.sleep(0.1)

# print(cti.call_function("Version(3)"))

# Test using adapter as context manager
# simple tag rea/write & cicode function call
# with adapter.CTAPIAdapter(IP_ADDRESS, CITECT_USERNAME, CITECT_PASSWORD) as ct2:
    # ct2.write_tag(SOME_CITECT_TAG_NAME, 2)
    # print(ct2.read_tag(SOME_CITECT_TAG_NAME))
    # print(ct2.call_function("Version(3)"))

# Testusing adapter as a context manager
# tag list read/write
# with adapter.CTAPIAdapter(IP_ADDRESS, CITECT_USERNAME, CITECT_PASSWORD) as ct3:
    # ct3.create_tag_list("my_tag_list")
    # ct3.add_tag_to_list("my_tag_list", SOME_CITECT_TAG_NAME)
    # ct3.refresh_list("my_tag_list")
    # print(ct3.value_from_list(SOME_CITECT_TAG_NAME))
    # ct3.write_tag_list(SOME_CITECT_TAG_NAME, 3)
    # ct3.refresh_list("my_tag_list")
    # print(ct3.value_from_list(SOME_CITECT_TAG_NAME))

