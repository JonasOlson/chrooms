#!/usr/bin/env python3
# coding=utf-8

import Ice
Ice.loadSlice('', ['-I' + Ice.getSliceDir(), 'murmur.ice'])
import Murmur
import sys
import configparser
import re

# Read configuration.
config = configparser.ConfigParser()
config.read('chrooms.cfg')
mumble_config = config['Mumble']
mumble_host = mumble_config['host']
mumble_port = mumble_config['port']
mumble_secret = mumble_config['secret']
rooms = {'Red': mumble_config['RED_room'],
         'Blue': mumble_config['BLU_room']}

# Set up a connection to the Mumble server.
props = Ice.createProperties()
props.setProperty('Ice.ImplicitContext', 'Shared')
idata = Ice.InitializationData()
idata.properties = props
comm = Ice.initialize(idata)
comm.getImplicitContext().put('secret', mumble_secret)
proxy = comm.stringToProxy('Meta:tcp -h {0} -p {1}'.format(mumble_host, mumble_port))
server = Murmur.MetaPrx.checkedCast(proxy).getServer(1)

users = server.getUsers()
channels = server.getChannels()
username = sys.argv[1]
channel_name = rooms[sys.argv[2]]

def normalise(name):
    return name.strip().lower()

def is_similar_username(mumble_name, tf2_name):
    def substitute(original_str):
        if original_str.isspace():
            return '[-_' + re.escape(original_str) + ']?'
        else:
            return re.escape(original_str)

    mumble_name = normalise(mumble_name)
    tf2_name = normalise(tf2_name)

    tf2_name_tokens = re.split('(\s)', tf2_name)
    pattern = ''.join(map(substitute, tf2_name_tokens))
    if re.compile(pattern).fullmatch(mumble_name):
        return True
    else:
        return False

def is_similar_room_name(mumble_name, tf2_name):
    return normalise(mumble_name) == normalise(tf2_name)

# Move user.
for c in channels.values():
    if is_similar_room_name(c.name, channel_name):
        for u in users.values():
            if is_similar_username(u.name, username):
                u.channel = c.id
                server.setState(u)
        break
