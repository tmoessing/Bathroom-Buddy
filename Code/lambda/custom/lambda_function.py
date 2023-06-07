"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""


from __future__ import print_function
import random


# --------------- Helper Functions   ------------------

def getwashhandssongs (session):

    washHandSongsArray = ['wash, wash, wash, your, hands, wash, wash, wash, your, hands, washy, washy, washy, washy, wash, your, hands, wash, under your nails, and wash in between your fingers, wash, wash, wash, your, hands, wash, wash, wash, your, hands',
                          'You got to wash those hands, You got to wash those hands of yours, you got to wash, wash, your hands, wash everywhere, do not miss a spot, wash, wash, your hands, washy, washy, washy, wash, your hands, do not miss a spot, get them with soap and water' ];


    randomwashhandsong = random.choice (washHandSongsArray)

    return randomwashhandsong

def getrandomtip (session):

    tipsArray = ['Remember to wash your hands after going to the bathroom!',
                 'Remember to take daily showers!',
                 'Remember to brush your hair everyday!', 
                 'Remember to flush the toilet!',
                 'Remember to floss your teeth',
                 'Remember to cut your nails regularly!',
                 'Remember to brush your teeth after every meal',
                 'Remember to brush your teeth for 2 minutes!',
                 'Remember to wash your hands for 20 seconds' ];

    randomtip = random.choice (tipsArray)

    return randomtip

def statement(title, body, session):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)


def continue_dialog(session):
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    return build_response(message)

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, content, speech_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + speech_output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_with_image(title, content, speech_output, reprompt_text, should_end_session):

    smallImageUrl = 'https://s3.amazonaws.com/bojo-creatures/' + creature_caught + 'Small.png'
    largeImageUrl = 'https://s3.amazonaws.com/bojo-creatures/' + creature_caught + 'Large.png'
    
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': '<speak>' + speech_output + '</speak>'
        },
        'card': {
            'type': 'Standard',
            'title': title,
            'text': content,
            'image': {
                'smallImageUrl': smallImageUrl,
                'largeImageUrl': largeImageUrl
            }
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def handle_launch_request(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    superlativesCreatureArray = ['aha',
                         'ahoy',
                         'all righty',
                         'bam',
                         'bingo',
                         'boing',
                         'boom',
                         'booya',
                         'cha ching',
                         'cheers',
                         'cowabunga',
                         'dynomite',
                         'eureka',
                         'fancy that',
                         'geronimo',
                         'giddy up',
                         'gotcha',
                         'great scott',
                         'hear hear',
                         'hip hip hooray',
                         'howdy',
                         'hurrah',
                         'huzzah',
                         'jeepers creeers',
                         'jiminy cricket',
                         'kaboom',
                         'kaching',
                         'kapow',
                         'katchow',
                         'kazaam',
                         'kerbam',
                         'kerboom',
                         'kerching',
                         'kerchoo',
                         'kerpow',
                         'mamma mia',
                         'oh my',
                         'oh snap',
                         'ooh la la',
                         'righto',
                         'squee',
                         'wahoo',
                         'whammo',
                         'woo hoo',
                         'wow',
                         'wowza',
                         'wowzer',
                         'yay',
                         'yippee',
                         'yowza',
                         'yowzer',
                         'zoinks'
                        ];

    superlative = random.choice (superlativesCreatureArray)

    session_attributes = {}
    card_title      = "Welcome"
    card_content    = "Welcome to bathroom buddy! What would you like me to do? "                      \
                    + "Say help if you want to know what I can do. "



    speech_output   = "Welcome to bathroom buddy! What would you like me to do? "                      \
                    + "Say help if you want to know what I can do. "

    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_potty_intent(intent, session):
    """ 
    compliments you for going potty
    """

    endCongratulationsArray = [' <say-as interpret-as="interjection">' ' Way to go' '</say-as>,',
                               ' Nice job! ',
                               ' Keep it up! ',
                               ' Congratulations! ',
                               ' Good job! ',
                               ' <say-as interpret-as="interjection">' ' Well done' '</say-as>,',
                               ' Excellent! ',
                               ' Muy bien! ',
                               ' Great job! ']

    randomendword = random.choice (endCongratulationsArray)

    congratulationsArray = ['<say-as interpret-as="interjection">' 'All righty' '</say-as>,' + randomendword , 
                            '<say-as interpret-as="interjection">' 'Bingo'      '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Bravo'      '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Cha ching'  '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Cheers'     '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Cowabunga'  '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Dynomite'   '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Eureka'     '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Hip hip hooray'  '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Hurrah'     '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Hurray'     '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Huzzah'     '</say-as>,' + randomendword , 
                            '<say-as interpret-as="interjection">' 'No way'     '</say-as>,' + randomendword , 
                            '<say-as interpret-as="interjection">' 'Woo hoo'    '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Wow'        '</say-as>,' + randomendword , 
                            '<say-as interpret-as="interjection">' 'Wowza'      '</say-as>,' + randomendword ,  
                            '<say-as interpret-as="interjection">' 'Wowzer'     '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Yay'        '</say-as>,' + randomendword , 
                            '<say-as interpret-as="interjection">' 'Yipee'      '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Yowza'      '</say-as>,' + randomendword ,
                            '<say-as interpret-as="interjection">' 'Yowzer'     '</say-as>,' + randomendword ,
                            '<audio src="https://s3.amazonaws.com/bathroombuddy-audio/Hand+Claps.mp3"/>' + randomendword     ];

    randompottyword = random.choice (congratulationsArray)

    session_attributes = {}
    card_title      = "Congratulations"
    card_content    = "Make sure to wash your hands now"

    speech_output   = randompottyword                                   \
                    + "<break time='500ms'/> Make sure to wash your hands now, "                   \
                    + "say 'Wash my hands' if you would like me to do that for you."


    reprompt_text   = "Go ahead and ask me, if you need help just ask!"

    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_washhands_intent(intent_name, session):
    """ 
   Wash Hands
    """   

    print("session attributess = {}".format(session) )
    try:
        session_attributes = session['attributes']
    except KeyError:
        session_attributes = {}

    beginingwordArray = ['Alright! ',
                         'Ok! ',
                         'Alrighty!',
                         'Got it! ']

    beginingword = random.choice (beginingwordArray)   
    
    card_title      = "Wash Hands"
    card_content    = "20 second timer"

    speech_output   =  beginingword + " three, two, one, Lets go, "  \
                    +  getwashhandssongs (session)    \
                    + "<break time='1s'/> What would you like me to do next? "  
                          
                 
    reprompt_text   = 'What would you like me to do next?'

    should_end_session = False

    session_attributes['last_intent'] = intent_name
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_mirrors_intent(intent_name, session):
    """ 
   Does mirror mirror on the wall and mirror mirror in my hand
    """   


    session_attributes = {}
    card_title      = "Magic mirror"
    card_content    = 'My Queen, you, are the fairest one, of all' 

    speech_output   = 'My Queen, you, are the fairest one, of all. <break time="500ms"/> Would you like me to do anything else? '    \

    reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_learnbrushteeth_intent(intent_name, session):
    """ 
  Tells you how to brush your teeth
    """   
    '''
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog(session)

    elif dialog_state == "COMPLETED":
        learningtopicsslot     = event['request']['intent']['slots']['learningtopicsslot']['value']
        if learningtopicsslot == "flossing":
             speech_output = 'flossing'
        if learningtopicsslot == "brushing teeth":
             speech_output = 'brushing teeth'
        if learningtopicsslot == "washing hands":
             speech_output = 'washing hands'
        else:
             speech_output = 'Sorry what was that?'

    
        return statement("skill_builder_intent", responce)

    else:
        return statement("skill_builder_intent", "No dialog")

    '''
    session_attributes = {}
    card_title      = "Learn how to brush your teeth"
    card_content    = 'First get a brush with soft bristles.'   \
                    + ' Then start brushing at the gumline using short, gentle strokes;'      \
                    + ' going from top to bottom. Then repeat on the inside.'   \
                    + " Brush for at least 2 minutes, and don't forget to brush your tongue!" \

    speech_output   = "First get a brush with soft bristles,"    \
                    + "Then start brushing at the gumline using short, gentle strokes,"      \
                    + "Go from top to bottom. Then repeat on the inside,"   \
                    + "Brush for at least 2 minutes, and don't forget to brush your tongue!" \
                    + " <break time='500ms'/> If you would like to practise say 'I would like to brush my teeth'"

    reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_learnfloss_intent(intent_name, session):

	
    session_attributes = {}
    card_title      = "Learn how to floss your teeth"
    card_content    = "Starting with about 18 inches of floss, wrap most of the floss around each middle finger, leaving an inch or two of floss to work with. "        \
					+ "Holding the floss tightly between your thumbs and index fingers, slide it gently up-and-down between your teeth. "  \
					+ "Gently curve the floss around the base of each tooth, making sure you go beneath the gumline. Never snap or force the floss, as this may cut or bruise delicate gum tissue. "        \
					+ "Use clean sections of floss as you move from tooth to tooth. "                           \
					+ "To remove the floss, use the same back-and-forth motion to bring the floss up and away from the teeth. "         \

    speech_output   = "Starting with about 18 inches of floss, wrap most of the floss around each middle finger, leaving an inch or two of floss to work with. "        \
					+ "Holding the floss tightly between your thumbs and index fingers, slide it gently up-and-down between your teeth. "  \
					+ "Gently curve the floss around the base of each tooth, making sure you go beneath the gumline. Never snap or force the floss, as this may cut or bruise delicate gum tissue. "        \
					+ "Use clean sections of floss as you move from tooth to tooth. "                           \
					+ "To remove the floss, use the same back-and-forth motion to bring the floss up and away from the teeth. "         \
					+ "<break time='500ms'/>Would you like me to do anything else?"


    reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_learnwashhands_intent(intent_name, session):

	
    session_attributes = {}
    card_title      = "Learn how to wash your hands"
    card_content    = "Wet your hands with running water."     \
					+ " Apply soap, and scrub until there are lots of bubbles."       \
					+ " Rub your hands, palm to palm, for at least 20 seconds. Remember to scrub all surfaces, including the backs of your hands, wrists, between your fingers and under your fingernails."          \
					+ " Rinse well. Dry your hands with a clean towel."         \
					+ " Then use the towel to turn off the faucet."

    speech_output   = "Wet your hands with running water."     \
					+ " Apply soap, and scrub until there are lots of bubbles."       \
					+ " Rub your hands, palm to palm, for at least 20 seconds. Remember to scrub all surfaces, including the backs of your hands, wrists, between your fingers and under your fingernails."          \
					+ " Rinse well. Dry your hands with a clean towel."             \
					+ " Then use the towel to turn off the faucet."                          \
                    + "<break time='500ms'/> If you would like to practise say 'I would like to wash my hands'"

    reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

    

def handle_brushteeth_intent(intent_name, session):
    '''
   sets timer to brush teeth
    '''   

    brushingteethtipsArray = [' Make sure you clean your top teeth,',
                 ' Make sure you clean your bottom teeth,',
                 ' Make sure you clean the top of your teeth,',
                 ' Make sure you clean behind your teeth,',
                 ' Make sure you clean the front part of the teeth,',
                 ' Make sure you clean your tongue,',
                 ' Hold the tooth brush at a 45 degree angle,',
                 ' Make sure to clean your gums,',
                 ' Ask how to brush your teeth for a reminder,',
                 ' Remember not to push too hard,',
                 ' Remember too brush at least twice a day,',
                 ' Brush for at least 2 minutes,' ];

    randombrushingtip1 = random.choice (brushingteethtipsArray)
    randombrushingtip2 = random.choice (brushingteethtipsArray)
    randombrushingtip3 = random.choice (brushingteethtipsArray)


    numberArray = ['1','2','3','4','5','6','8']

    randomnumber1 = random.choice (numberArray)
    randomnumber2 = random.choice (numberArray)
    randomnumber3 = random.choice (numberArray)
    randomnumber4 = random.choice (numberArray)

    randombrushingteethsong1 = '"https://s3.amazonaws.com/bathroombuddy-audio/BrushingTeeth' + randomnumber1 + '.mp3"'
    randombrushingteethsong2 = '"https://s3.amazonaws.com/bathroombuddy-audio/BrushingTeeth' + randomnumber2 + '.mp3"'
    randombrushingteethsong3 = '"https://s3.amazonaws.com/bathroombuddy-audio/BrushingTeeth' + randomnumber3 + '.mp3"'
    randombrushingteethsong4 = '"https://s3.amazonaws.com/bathroombuddy-audio/BrushingTeeth' + randomnumber4 + '.mp3"'


    session_attributes = {}
    card_title      = "Brush teeth"
    card_content    = "A two minute timer"    \

    

    speech_output   = 'Get ready! three, two, one, Go! <break time="6s"/>'+randombrushingtip1+'<break time="6s"/><audio src='+ randombrushingteethsong1 + '/><break time="6s"/>' \
                    + randombrushingtip2 +'<break time="6s"/><audio src=' + randombrushingteethsong2 + '/><break time="3s"/> Half way there! <break time="3s"/>'+randombrushingtip3+'<break time="6s"/><audio src=' + randombrushingteethsong3 + '/><break time="6s"/>'       \
                    + 'Almost there!<break time="6s"/> <audio src=' + randombrushingteethsong4 + '/>'    \
                    + '<audio src="https://s3.amazonaws.com/bathroombuddy-audio/Alarm.mp3" /> Thats the end! <break time="1s"/> If you have not already you should floss now. Would you like me to do anything else? '

    reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_NoIntent_intent(intent_name, session):

    """
    print("session attributess = {}".format(session) )
    try:
        session_attributes = session['attributes']
    except KeyError:
        session_attributes = None

    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa in {}'.format(intent_name))

    if session_attributes:
        if session_attributes['last_intent'] == 'WashHandsIntent':
            card_title      = "Wash Hands"
            card_content    = "Tell me when your ready." 

            speech_output   = 'Ok, tell me when your ready'    \

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = False

        if session_attributes['last_intent'] == 'TipIntent':
            card_title      = ""
            card_content    = "Ok, What would you like me to do next?" 
                  
            speech_output   = "Ok, What would you like me to do next?"  \

            reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

            should_end_session = False    

        else:
            card_title      = "Good bye"
            card_content    = 'Ok! See you later Alligator' 

            speech_output   = 'Ok! See you later Alligator'    \

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = True

    else:

        card_title      = "Goodbye"
        card_content    = 'Ok! See you later Alligator' 

        speech_output   = 'Ok! See you later Alligator'    \

        reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

        should_end_session = True


    session_attributes = {}
    session_attributes['last_intent'] = intent_name
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

    """

    session_attributes = {}
    card_title      = "Goodbye"
    card_content    = "Ok! See you later Alligator"

    speech_output   = "Ok! See you later Alligator"

    reprompt_text   = "Go ahead and ask me, if you need help just ask!"

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_YesIntent_intent(intent_name, session):

    """
    print("session attributess = {}".format(session) )
    try:
        session_attributes = session['attributes']
    except KeyError:
        session_attributes = None


    if session_attributes:
        if session_attributes['last_intent'] == 'WashHandsIntent':
            card_title      = "Wash Hands"
            card_content    = "Wash Hands" 

            speech_output   = 'Alright, three, two, one, '  \
                            + getwashhandssongs (session)    \
                            + 'What would you like me to do next?'

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = False

        if  session_attributes['last_intent'] == 'TipIntent':   
            card_title      = 'Tip'
            card_content    =  getrandomtip (session)
                  
            speech_output   = 'Alright! Here is your tip! <break time="500ms"/>' +  getrandomtip (session) +  '<break time="500ms"/>'\
                            + "Would you like another one?"                      \


            reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

            should_end_session = False


        else:
            card_title      = "Good bye"
            card_content    = 'Ok! See you later Alligator' 

            speech_output   = 'Ok! See you later Alligator'    \

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = False

    else:

        card_title      = "Goodbye"
        card_content    = 'Ok! See you later Alligator' 

        speech_output   = 'Ok! See you later Alligator'    \

        reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

        should_end_session = True

    session_attributes = {}
    session_attributes['last_intent'] = intent_name
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

    """

    session_attributes = {}
    card_title      = "Tasks"
    card_content    = "Go ahead and ask me, if you need help just ask!"

    speech_output   = "Go ahead and ask me, if you need help just ask!"

    reprompt_text   = "Go ahead and ask me, if you need help just ask!"

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_Ready_intent(intent_name, session):

    """
    print("session attributess = {}".format(session) )
    try:
        session_attributes = session['attributes']
    except KeyError:
        session_attributes = False


    if session_attributes:
        if session_attributes['last_intent'] == 'WashHandsIntent':
            card_title      = "Wash Hands"
            card_content    = "Wash Hands" 

            speech_output   = 'Alright, three, two, one, '  \
                            + getwashhandssongs (session)   \

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = False

        else:
            card_title      = "Good bye"
            card_content    = 'Ok! See you later Alligator' 

            speech_output   = 'from ready intent else'    \

            reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

            should_end_session = False

    else:

        card_title      = "Goodbye"
        card_content    = 'Ok! See you later Alligator' 

        speech_output   = 'from ready intent'    \

        reprompt_text   = 'Go ahead and ask me, if you need help just ask!'

        should_end_session = True

    session_attributes = {}
    session_attributes['last_intent'] = intent_name
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

    """
    session_attributes = {}
    card_title      = "Tasks"
    card_content    = "Go ahead and ask me, if you need help just ask!"

    speech_output   = "Go ahead and ask me, if you need help just ask!"

    reprompt_text   = "Go ahead and ask me, if you need help just ask!"

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_tip_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    print("session attributess = {}".format(session) )
    try:
        session_attributes = session['attributes']
    except KeyError:
        session_attributes = None

    tipsArray = ['Remember to wash your hands after going to the bathroom!',
                 'Remember to take daily showers!',
                 'Remember to brush your hair everyday!', 
                 'Remember to flush the toilet!',
                 'Remember to floss your teeth',
                 'Remember to cut your nails regularly!',
                 'Remember to brush your teeth after every meal',
                 'Remember to brush your teeth for 2 minutes!',
                 'Remember to wash your hands for 20 seconds' ];

    randomtip = random.choice (tipsArray)    

    session_attributes = {}
    card_title      = 'Tip'
    card_content    = randomtip
                  
    speech_output   = 'Alright! Here is your tip <break time="500ms"/>' + randomtip +  '<break time="500ms"/>'           \
                    + " If you would like another one say 'I would like another tip', Would you like me to do anything else? "                      \


    reprompt_text   = "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = False
    session_attributes['last_intent'] = intent_name
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_help_intent(intent_name, session):

    session_attributes = {}
    card_title      = "Help"
    card_content    = 'Say, "I went potty" to be congratulated, '        \
                    + 'or say "Mirror mirror on the wall, who is the fairest one of them all, " ' \
                    + 'or say "Sing me a song while I wash my hands" for a 20 second timer, '  \
                    + 'or say "Give me a tip" for advice, ' \
                    + 'or say "How do I brush my teeth?" for a description on how to brush teeth, '  \
                    + 'or say "Set a timer for me to brush my teeth" for a 2 minute timer, '       \
                    + 'or say "How do I floss my teeth?" for a description on how to floss teeth, '             \
                    + 'or say "How do I wash my hands?" for a description on how to wash hands.'           

    speech_output   = "Say, 'I went potty' to be congratulated. "          \
                    + "or say 'Mirror mirror on the wall, who is the fairest one of them all,' " \
                    + "or say 'Sing me a song while I wash my hands' for a 20 second timer,"  \
                    + "or say 'Give me a tip' for advice, " \
                    + "or say 'How do I brush my teeth?' for a description on how to brush teeth, "  \
                    + "or say 'Set a timer for me to brush my teeth' for a 2 minute timer, "           \
                    + 'or say "How do I floss my teeth?" for a description on how to floss teeth, '           \
                    + 'or say "How do I wash my hands?" for a description on how to wash hands.'

    reprompt_text   = 'Say, set a timer for me to wash my hands.'

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_end_intent():


    goodbyewordsArray = ["See you later, alligator",
                         "In a while, crocodile",
                         "Gotta go, buffalo",
                         "Bye bye, butterfly",
                         "Bye for now, brown cow",
                         "Gotta bail, big blue whale",
                         "Better shake, rattle snake",
                         "Toodle-Doo, kangaroo",
                         "Take care, big black bear",
                         "Adios, Hippos",
                         "Gotta run, skeleton",
                         "Hit the trail, tiny snake",
                         "Out the door, dinosaur",
                         "Take care, polar bear",
                         "See you soon, raccon",
                         "Hit the road, happy toad",
                         "Time to scoot, little newt",
                         "Till then, penguin",
                         "Hasta mañana, iguana",
                         "On the bus, octopus",
                         "To your house, quiet mouse",
                         "In a hour, sunflower",
                         "Better wish, jelly fish",
                         "Chop chop, lollipop",
                         "Cheers, big ears",
                         "See you soon, big baboon",
                         "Okeedokee, artichokee",
                         "Take care, teddy bear",
                         "Bye bye, french fry",
                         "Time to squirm, wiggle worm",
                         "Lets scat, alley cat",
                         "Sure do, tennis shoe",
                         "Better skadoodle, poodle",
                         "Wave good bye, butterfly"]


    randomgoodbyeword = random.choice (goodbyewordsArray)  

    session_attributes = {}
    card_title      = "Good bye"
    card_content    = randomgoodbyeword

    speech_output   = randomgoodbyeword

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return handle_launch_request(session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    print('{}intent {} was called'.format('*************************************', intent_name))

    # Dispatch to your skill's intent handlers
    if intent_name == "PottyIntent" :
        return handle_potty_intent(intent_name, session)
    elif intent_name == "WashHandsIntent":
        return handle_washhands_intent(intent_name, session)
    elif intent_name == "LearnBrushTeethIntent":
        return handle_learnbrushteeth_intent(intent_name, session)
    elif intent_name == "LearnFlossIntent":
        return handle_learnfloss_intent(intent_name, session)
    elif intent_name == "LearnWashHandsIntent":
        return handle_learnwashhands_intent(intent_name, session)
    elif intent_name == "BrushTeethIntent":
        return handle_brushteeth_intent(intent_name, session)
    elif intent_name == "TipIntent":
        return handle_tip_intent(intent_name, session)
    elif intent_name == "WallMirrorIntent" or intent_name == "HandMirrorIntent" :
        return handle_mirrors_intent(intent_name, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_intent(intent_name, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_NoIntent_intent(intent_name, session)
    elif intent_name == "ReadyIntent":
        return handle_Ready_intent(intent_name, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_YesIntent_intent(intent_name, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_end_intent()
    else:
        print("what the what is " + intent_name)
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
             "amzn1.ask.skill.069a8d53-f6f4-473b-a78a-97f446e7671f"):
         raise ValueError("Invalid Application ID")
    

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
