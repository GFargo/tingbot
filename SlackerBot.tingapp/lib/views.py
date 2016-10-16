###
# Core Libs
###
import tingbot
from tingbot import *

######
# Setup Screens
######
def setup_screen( current_screen ):
    
    # Error Handler Screen
    if current_screen == 'error':
        screen.brightness = 100
        screen.fill(color='orange')
        screen.rectangle(align='bottomleft', size=(320,30), color='navy')
    
    # Loading Screen
    if current_screen == 'loading':
        screen.brightness = 85
        screen.fill(color='navy')
        screen.image( 'img/loading.gif', scale='fill' )
        screen.rectangle(align='topleft', size=(320,30), color='navy')
        screen.image( 'img/slack_icon.png', scale=(0.1), xy=(300,16) )
        
    # Waiting on Data from Hook Screen
    if current_screen == 'waiting':
        screen.brightness = 95
        screen.fill(color='navy')
        screen.image( 'img/loading.gif', scale='fill' )
        screen.rectangle(align='bottomleft', size=(320,30), color='navy')
        screen.rectangle(align='topleft', size=(320,30), color='navy')
        
    # Display Chat Transcript
    if current_screen == 'transcript':
        screen.brightness = 100
        screen.fill(color='teal')
        screen.image( 'img/bg.png', scale='fill', align='top' )
        screen.rectangle(align='left', xy=(16,225), size=(240,18), color='navy')
    
    return


######
# Setup Loading / Boot Screen
######
def showLoading():
    setup_screen( 'loading' )
    screen.text(
        'Booting Up...',
        xy=(12, 8),
        align='topleft',
        font_size=12,
        color='white',
    )
    
    return

######
# Setup Waiting for Messages Screen
######
def showWaiting():
    setup_screen( 'waiting' )
    screen.text(
        'SlackerBot',
        xy=(160, 15),
        font_size=12,
        color='white',
    )
    screen.text(
        'waiting for messages...',
        xy=(160, 225),
        font_size=12,
        color='white',
    )
    
    return

######
# Setup Error Screen
######
def showError( message ):
    setup_screen( 'error' )
    screen.text(
        'Error',
        xy=(160, 15),
        font_size=12,
        color='white',
    )
    screen.text(
        message,
        xy=(160, 225),
        font_size=12,
        color='white',
    )
    
    return
