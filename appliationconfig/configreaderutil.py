#!/usr/bin/env python3

import configparser

class ReadProfile:

    def readandfindconfig(_self, profile, key):
        config = configparser.ConfigParser()
        config.read("applicationproperties")
        finalurl = config[profile][key]
        return finalurl
