import pygame
from gpiozero import Button

pygame.init()

kit = 1

#Kit 1 - DJ
vscratch = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/vinyl_scratch.wav")
zum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/bd_zum.wav")
basswoods = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/bass_woodsy_c.wav")
choir = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/ambi_choir.wav")
basshit = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/bass_hit_c.wav")
boom = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/bd_boom.wav")
beat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat.wav")

#kit 2 - drums
drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
kick = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_heavy_kick.wav")
cymbal2 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_soft.wav")
snare2 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_soft.wav")
beat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat.wav")

#kit 3 - Guitar
fifths = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/guit_e_fifths.wav")
em9 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/guit_em9.wav")
slide = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/guit_e_slide.wav")
harmonics = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/guit_harmonics.wav")
drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
snap = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/perc_snap.wav")
beat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat.wav")

#kit 4 - random noises
crow = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/misc_crow.wav")
burp = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/misc_burp.wav")
rewind = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/vinyl_rewind.wav")
bong = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/elec_bong.wav")
blip2 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/elec_blip2.wav")
pop = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/elec_pop.wav")
beat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat.wav")

#kit 5 - zen
chime = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/elec_chime.wav")
bell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")
choir = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/ambi_choir.wav")
piano = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/ambi_piano.wav")
snap = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/perc_snap.wav")
tablana = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/tabla_na.wav")
beat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat.wav")

#kit 6- Meme
meme1 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/freshavocado.wav")
meme2 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/patrisha.wav")
meme3 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/sisters.wav")
meme4 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/strips.wav")
meme5 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/yea.wav")
meme6 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/yee.wav")
bg6 = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/basicbeat6.wav")
     
beat1 = Button(18)
beat2 = Button(19)
beat3 = Button(17)
beat4 = Button(16)
beat5 = Button(23)
beat6 = Button(5)
beat7 = Button(4)
switch = Button(26)
 
###MAIN####
try:
    while(True):

        if kit == 1:
            
            beat1.when_pressed = vscratch.play

            beat2.when_pressed = zum.play

            beat3.when_pressed = basswoods.play

            beat4.when_pressed = choir.play
            
            beat5.when_pressed = basshit.play
            
            beat6.when_pressed = boom.play
            
            beat7.when_pressed = beat.play

        if kit == 2:

            beat1.when_pressed = drum.play

            beat2.when_pressed = cymbal.play

            beat3.when_pressed = snare.play

            beat4.when_pressed = kick.play

            beat5.when_pressed = cymbal2.play

            beat6.when_pressed = snare2.play

            beat7.when_pressed = beat.play

        if kit == 3:

            beat1.when_pressed = fifths.play

            beat2.when_pressed = em9.play

            beat3.when_pressed = slide.play

            beat4.when_pressed = harmonics.play

            beat5.when_pressed = drum.play

            beat6.when_pressed = snap.play

            beat7.when_pressed = beat.play
            
        if kit == 4:

            beat1.when_pressed = crow.play

            beat2.when_pressed = burp.play

            beat3.when_pressed = rewind.play

            beat4.when_pressed = bong.play

            beat5.when_pressed = blip2.play

            beat6.when_pressed = pop.play

            beat7.when_pressed = beat.play

        if kit == 5:

            beat1.when_pressed = chime.play

            beat2.when_pressed = bell.play

            beat3.when_pressed = choir.play

            beat4.when_pressed = piano.play

            beat5.when_pressed = snap.play

            beat6.when_pressed = tablana.play

            beat7.when_pressed = beat.play
        
        if kit == 6:
            
            beat1.when_pressed = meme1.play

            beat2.when_pressed = meme2.play

            beat3.when_pressed = meme3.play

            beat4.when_pressed = meme4.play
            
            beat5.when_pressed = meme5.play
            
            beat6.when_pressed = meme6.play
            
            beat7.when_pressed = bg6.play
            
        if kit >= 6:
            kit = 1
        switch.wait_for_press()
        kit += 1
    
except:
    print("failed")