import random
import os


#Randomly select rhythm patterns of a given difficulty until the given number of bars is filled up
def generate_bars(difficulty, number_of_bars):

    #Each element holds the information of one bar
    bars_list = []

    for i in range(number_of_bars):
        
        bar = "{"

        totalLength = 0

        #Patterns for 4/4 bars
        while totalLength < 4:

            if difficulty == 1:
                pattern = random.randint(1,6)

            if difficulty == 2:
                pattern = random.randint(1,9)

            if difficulty == 3:
                pattern = random.randint(1,18)

            if difficulty == 4:
                pattern = random.randint(1,26)

            if difficulty == 5:
                pattern = random.randint(1,32)


            #####Difficulty 1#####

            #Crotchet    
            if pattern == 1:
                bar = bar + "b'4 "
                totalLength+=1

            #Two Quavers
            elif pattern == 2:
                bar = bar + "b'8 "
                bar = bar + "b'8 "
                totalLength+=1

            #Minim (can only be placed on first 3 beats)
            elif pattern == 3:
                if totalLength < 3:
                    bar = bar + "b'2 "
                    totalLength+=2

            #Crotchet Rest
            elif pattern == 4:
                bar = bar + "r4 "
                totalLength+=1

            #Dotted Minim (can only be placed on first two beats)
            elif pattern == 5:
                if totalLength < 2:
                    bar = bar + "b'2. "
                    totalLength+=3

            #Semibreve (can only be placed on the first beat)
            elif pattern == 6:
                if totalLength == 0:
                    bar = bar + "b'1 "
                    totalLength+=4\


            #####Difficulty 2#####

            #Dotted Crotchet + Quaver (can only be placed on beat 1 or 3 as I haven't implemented ties yet)        
            elif pattern == 7:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'4. "
                    bar = bar + "b'8 "
                    totalLength+=2

            #Quaver + Quaver Rest
            elif pattern == 8:
                    bar = bar + "b'8 "
                    bar = bar + "r8 "
                    totalLength+=1

            #Quaver-Crotchet-Quaver
            elif pattern == 9:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'8 "
                    bar = bar + "b'4 "
                    bar = bar + "b'8 "
                    totalLength+=2


            #####Difficulty 3#####

            #Quaver Rest + Quaver
            elif pattern == 10:
                bar = bar + "r8 "
                bar = bar + "b'8 "
                totalLength+=1

            #Quaver Triplets
            elif pattern == 11:
                bar = bar + "\\tuplet 3/2 { "
                bar = bar + "b'8 "
                bar = bar + "b'8 "
                bar = bar + "b'8 "
                bar = bar + "} "
                totalLength+=1

            #Crotchet Triplets (can only be placed on beat 1 or 3)
            elif pattern == 12:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "\\tuplet 3/2 { "
                    bar = bar + "b'4 "
                    bar = bar + "b'4 "
                    bar = bar + "b'4 "
                    bar = bar + "} "
                    totalLength+=2

            #Four SemiQuavers
            elif pattern == 13:
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                totalLength+=1

            #Quaver-SemiQuaver-SemiQuaver
            elif pattern == 14:
                bar = bar + "b'8 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                totalLength+=1

            #SemiQuaver-SemiQuaver-Quaver
            elif pattern == 15:
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'8 "
                totalLength+=1

            #Dotted Quaver + SemiQuaver
            elif pattern == 16:
                bar = bar + "b'8. "
                bar = bar + "b'16 "
                totalLength+=1

            #SemiQuaver + Dotted Semiquaver
            elif pattern == 17:
                bar = bar + "b'16 "
                bar = bar + "b'8. "
                totalLength+=1

            #Quaver + DOtted Crotchet (can only be placed on beat 1 or 3)
            elif pattern == 18:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'8 "
                    bar = bar + "b'4. "
                    totalLength+=2


            #####Difficulty 4#####

            #SemiQuaver-Quaver-SemiQuaver
            elif pattern == 19:
                bar = bar + "b'16 "
                bar = bar + "b'8 "
                bar = bar + "b'16 "
                totalLength+=1

            #SemiQuaver-SemiQuaverRest-SemiQuaver-SemiQuaverRest
            elif pattern == 20:
                bar = bar + "b'16 "
                bar = bar + "r16 "
                bar = bar + "b'16 "
                bar = bar + "r16 "
                totalLength+=1

            #SemiQuaverRest-SemiQuaver-SemiQuaverRest-SemiQuaver
            elif pattern == 21:
                bar = bar + "r16 "
                bar = bar + "b'16 "
                bar = bar + "r16 "
                bar = bar + "b'16 "
                totalLength+=1

            #SemiQuaver-SemiQuaver-Crotchet-SemiQuaver-SemiQuaver (can only be placed on beat 1 or 3)
            elif pattern == 22:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'16 "
                    bar = bar + "b'16 "
                    bar = bar + "b'4 "
                    bar = bar + "b'16 "
                    bar = bar + "b'16 "
                    totalLength+=2

            #SemiQuaver-SemiQuaver-Crotchet-Quaver (can only be placed on beat 1 or 3)
            elif pattern == 23:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'16 "
                    bar = bar + "b'16 "
                    bar = bar + "b'4 "
                    bar = bar + "b'8 "
                    totalLength+=2

            #Quaver-Crotchet-SemiQuaver-SemiQuaver (can only be placed on beat 1 or 3)
            elif pattern == 24:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "b'8 "
                    bar = bar + "b'4 "
                    bar = bar + "b'16 "
                    bar = bar + "b'16 "
                    totalLength+=2

            #SemiQuaver-SemiQuaver-QuaverRest
            elif pattern == 25:
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "r8 "
                totalLength+=1

            #QuaverRest-SemiQuaver-SemiQuaver
            elif pattern == 26:
                bar = bar + "r8 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                totalLength+=1


            #####Difficulty 5#####

            #Triplet(DottedQuaver-SemiQuaver-Quaver)
            elif pattern == 27:
                bar = bar + "\\tuplet 3/2 { "
                bar = bar + "b'8. "
                bar = bar + "b'16 "
                bar = bar + "b'8 "
                bar = bar + "} "
                totalLength+=1

            #Triplet(Quaver-DottedQuaver-SemiQuaver)
            elif pattern == 28:
                bar = bar + "\\tuplet 3/2 { "
                bar = bar + "b'8 "
                bar = bar + "b'8. "
                bar = bar + "b'16 "
                bar = bar + "} "
                totalLength+=1

            #SemiQuaverRest-SemiQuaver-SemiQuaver-SemiQuaver
            elif pattern == 29:
                bar = bar + "r16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                totalLength+=1

            #Quaver QUintuplets
            elif pattern == 30:
                if totalLength == 0 or totalLength == 2:
                    bar = bar + "\\tuplet 5/4 { "
                    bar = bar + "b'8 "
                    bar = bar + "b'8 "
                    bar = bar + "b'8 "
                    bar = bar + "b'8 "
                    bar = bar + "b'8 "
                    bar = bar + "} "
                    totalLength+=2

            #Quaver + Triplet(SemiQuaver-SemiQuaver-SemiQuaver)
            elif pattern == 31:
                bar = bar + "b'8 "
                bar = bar + "\\tuplet 3/2 { "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "} "
                totalLength+=1

            #Triplet(SemiQuaver-SemiQuaver-SemiQuaver) + Quaver
            elif pattern == 32:
                bar = bar + "\\tuplet 3/2 { "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "b'16 "
                bar = bar + "} "
                bar = bar + "b'8 "
                totalLength+=1
                

        bar = bar + "}"
        
        bars_list.append(bar)


    return bars_list



#Combine all the bars together and add a double bar line at the end
def generate_track(bars):
    all_bars = ["{"]

    for bar in bars:
        all_bars.append(bar)

    track = "".join(all_bars) + " \\bar \"|.\"" + "}"

    return track

    

def generate_rhythms(difficulty, number_of_bars):
    
    bars = generate_bars(difficulty, number_of_bars)

    track = generate_track(bars)

    #Create the correct format for a LilyPond file
    rhythms = open("Rhythms.ly","a")
    rhythms.writelines("\\version \"2.18.2\" \\score {")
    rhythms.write(track)
    rhythms.write("}")
    rhythms.close()

    os.system("lilypond Rhythms.ly")
