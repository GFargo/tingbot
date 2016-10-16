# coding: utf-8
# v0.0.1

####################################
###### IMPORTS
####################################
    

###
# Core Libs
###
import tingbot
from tingbot import *

###
# External Libs
###
import requests
import urllib, json
from datetime import datetime
from urlparse import urlparse, parse_qsl, parse_qs

###
# Local Libs
###
from lib.helpers import *
from lib.views import *


####################################
###### SETUP STATE
####################################
    
# retrieve webhook url from config
webhook_name = str( tingbot.app.settings['webhook_name'] )
cache_cap = int( tingbot.app.settings['message_limit'] )

state = {}
# state['log'] = {}
state['log'] = tingbot.app.settings['log']
# state['transcript'] = []
state['transcript'] = tingbot.app.settings['transcript']

state['screen'] = 'loading'


####################################
###### BUTTONS
####################################
    
######
# Reset Button
######
@midright_button.press
def midright_reset():
    state['log'] = None
    state['transcript'] = None

######
# OnIT Button
######
@midleft_button.press
def midleft_send_message():
    """ 
    Goal with this would be to allow this button to
    push up a string to the slack room from which
    the most recent message originated
    """
    return

######
# Scrolling
######
@left_button.press
def scroll_up():
    """ scroll up in the transcript log """
    return

@right_button.press
def scroll_down():
    """ scroll down in the transcript log """
    return


####################################
###### DATA LAYER
####################################

######
# Trim Log 
######
def trim_log():
    # Max messages to be stored defined in settings
    global cache_cap
    
    # Create reversed version to trim based on cache_cap  
    revTranscript = state['transcript']
    revTranscript.reverse()
    
    # Trim Log Length - ensure log doesn't get too long
    if len( state['log'] ) >= cache_cap:
        # walk through transcript in reverse chron
        count = 0
        for timestamp, message in revTranscript:
            if count >= cache_cap:
                print(message)
                state['log'].pop( message['timestamp'], None )
            # increase count
            count = count + 1
            
######
# Setup Main Screen
######
def showTranscript():
    setup_screen( 'transcript' )
    title_text = '%s v%s - %s' % ( tingbot.app.info['name'], tingbot.app.info['version'], get_ip_address() )
    screen.text(
        title_text,
        xy=(20, 226),
        align='left',
        font_size=8,
        # font='font/Arial Rounded Bold.ttf',
        color='white',
    )
    
    y_pos = 26
    message_count = 0
    # for timestamp, message in sorted( state['log'].iteritems() ):
    for timestamp, message in state['transcript'] :
        if message_count <= 3:
            meta = "%s @%s --- [%s] ---" % ( pretty_date( float( message['timestamp'] ) ), message['author'], message['channel'] )
            # Meta Content
            screen.text(
                meta,
                align='topleft',
                xy=( 20, ( y_pos - 10 ) ),
                font_size=8,
                color='black',
            )
            
            # Message Text
            screen.text(
                strip_non_ascii( message['text'] ),
                align='topleft',
                xy=( 22, y_pos ),
                font_size=10,
                max_width=280,
                color='black',
            )
            y_pos = y_pos + ( 18 * line_count( message['text'], 75 ) )
            message_count = message_count - 1
            
    return

######
# Validate Data from Webhook
######
def validate_data( data ):
    return True

######
# Process New Data from Webhook
######
def store_data( data ):
    
    if state['log'] == None:
        state['log'] = {}
    if state['transcript'] == None:
        state['transcript'] = []
    
    # Parse post data
    data = parse_qs( urlparse( data ).path ) 

    if validate_data( data ) == True:
    
        # Store Log Update
        state['log'][ data['timestamp'][0] ] = { 
            "timestamp": data['timestamp'][0], 
            "author": data['user_name'][0], 
            "text": data['text'][0], 
            "channel":data['channel_name'][0] 
        }
        
        # Sort transcript for display
        state['transcript'] = sorted( state['log'].iteritems() )
        
        # Remove old items from chat log
        trim_log()
        
        # Update order of transcript to be chronological
        state['transcript'].reverse()
        
        # Save trimmed log
        tingbot.app.settings['log'] = state['log']
        tingbot.app.settings.save()

    return

####################################
###### THE LOOP / EVENTS
####################################

######
# Init Application
######
@once(seconds=2.5)
def check_init():
    if 'log' in state or state['log']:
        state['screen'] = 'transcript'
    else:    
        state['screen'] = 'waiting'
    return

######
# Webhook Setup
######
@webhook( webhook_name )
def on_webhook( data ):
    store_data( data )
    return

######
# Main Loop
######
@every(seconds=1.0/30)
def loop():
    if state['log'] and state['screen'] != 'loading':
        showTranscript()
    else:
        showWaiting()
    
    if state['screen'] == 'loading':
        showLoading()
    
    return


######
# Makes the magic happen
######
tingbot.run()