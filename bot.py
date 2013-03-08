#!/usr/bin/python
import sys
import socket
import string
import os
import ssl

HOST = 'irc.faceroar.com'
PORT = 6667
NICK = 'stwt'
IDENT = 'pybot'
REALNAME = 'stewart'
OWNER = 'sgtw'
CHANNELINIT = '#room'
readbufer = ''

def ping():
    ircsock.send('PONG :Pong\n')

def sendmsg(chan, msg):
    ircsock.send('PRIVMSG ' + chan + ' :' + msg + '\n')

def joinchan(chan):
    ircsock.send('JOIN ' + chan + '\n')

def hello(newnick):
    ircsock.send('PRIVMSG ' + channel + ' :Hello!\n')


ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((HOST, PORT))
ircsock.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\n')
ircsock.send('NICK '+NICK+'\n')
joinchan(CHANNELINIT)

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    user = ircmsg[:ircmsg.find('!')]
    msg = ircmsg[ircmsg.find('#room :')+1:]
    print (user + msg)
    if ircmsg.find("PING :") != -1:
        ping()
    if msg.find(NICK) != -1:
        ircsock.send('PRIVMSG ' + CHANNELINIT + ' :the FUCK DO YOU WANT\n')

