#!/usr/bin/env python3
# coding=utf-8

import Ice
Ice.loadSlice('', ['-I' + Ice.getSliceDir(), 'murmur.ice'])
import Murmur
import sys
import configparser

# Read configuration.
config = configparser.ConfigParser()
config.read('chrooms.cfg')
mumble_config = config['Mumble']
mumble_host = mumble_config['host']
mumble_port = mumble_config['port']
mumble_secret = mumble_config['secret']
rooms = {'RED': mumble_config['RED_room'],
         'BLU': mumble_config['BLU_room']}

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

def is_similar(name0, name1):
    return name0.strip().lower() == name1.strip().lower()

# Move user.
for c in channels.values():
    if is_similar(c.name, channel_name):
        for u in users.values():
            if is_similar(u.name, username):
                u.channel = c.id
                server.setState(u)
        break
