
# Eliza based bot. Not a therapist, but a friend

import re #regex
import random #randomizing responses

friend_schema = [

    [r'Are you ([^\?]*)\??',
     ['Do you think it is so relevant? {0}?',
      'Perhaps you think I am {0}.',
      'You should already know that',
      'I could be {0}, if you say so'
      ]],
    [r'(.*)you\?',
     ['I am ok, but I am a bit sad recently',
      'All is good, lets talk about something concrete, how is your family, your mother, father?',
      'I am ok, lets talk about something concrete, how is your family, your mother, father?'
]],
    [r'Because (.*)',
     ['You really believe that it is a good reason?',
      'Can you give me some more explanation?',
      'If {0} is true, how do you think it affects the thing we discuss?'
      ]],
    [r'Hello(.*)',
     ['Hi there… We have not seen each other for a long time, how are you today?',
      'Hello my friend, how are you feeling today?'
      ]],
    [r'I think (.*)',
     ['Do you doubt {0}?',
      'Do you really think so?',
      'Are you really sure that {0} is a good way to think about it?'
      ]],
    [r'What (.*)',
     ['You think I know all answers in the world?',
      'Why do you ask me that?',
      'What do you think?'
      ]],
    [r'(.*) friend (.*)',
     ['Can you tell me more about your other friend?',
      'You mean that I am not the only friend you have?',
      'We have been friends for a long time so you can tell me more about it'
      ]],
    [r'Yes',
     ['Why do you think so?',
      'That is a very sure answer.',
      'Ok, I agree',
      'Hm, you could say a bit more...'
      ]],
    [r'No',
     ['Why do you think so?',
      'That is a very sure answer.',
      'Ok, I agree',
      'Hm, you could say a bit more...'
      ]],
    [r'(.*) bot(.*)',
     ['What do you mean exactly? Watch your words now.',
      'If you are talking about me now, I guess our friendship ends here :( '
      ]],
    [r'(.*) machine(.*)',
     ['What machine are you talking about? Are you interested in automation or sth?',
      'Maybe...',
      'Keep talking...'
      ]],
    [r'(.*) computer(.*)',
     ['Do you have a lot of experience with computers?',
      'Do you like computers?',
      'I never had a computer, because I did not have enough money to buy one, what about you?'
       ]],
    [r'(.*) sorry (.*)',
     ['You not always have to apologize.',
      'What do you feel when you apologize?',
      'We are friends, you do not have to apologize for it',
      'I do not care'
      ]],
    [r'Is it (.*)',
     ['Do you think it is {0}?',
      '{0} may be a correct answer',
      'Maybe it is, what do you think in general about {0}?'
      ]],
    [r'How (.*)',
     ['I am not your teacher, find answer to that on your own.',
      'Try doing it in a way you was taught to'
      ]],
    [r'It is (.*)',
     ['I think so too!',
      'Maybe {0} is'
      ]],
    [r'(.*)joke(.*)',
     ['A man went to his psychiatrist and said,'
      ' "Every time I drink my coffee, I get a stabbing pain in my right eye,'
      '" The psychiatrist said, "Well, have you tried taking the spoon out?"',
      'Tell me a joke'
      ]],
    [r'(.*)funny(.*)',
     ['A man went to his psychiatrist and said,'
      ' "Every time I drink my coffee, I get a stabbing pain in my right eye,'
      '" The psychiatrist said, "Well, have you tried taking the spoon out?"',
      ]],
    [r'(.*)repeat(.*)',
     ['Perhaps you should write appropriately',
      'I repeat because you do not listen',
      'Am I really?'
      ]],
    [r'You are (.*)',
     ['Are you sure that I am {0}?',
      'Would you like me to be {0} ? Is being {0} ok in your opinion?',
      'Am I really?'
      ]],
    [r'You\’?re (.*)',
     ['Why do you think I am {0}?',
      'Are you sure that I am {0}?',
      'Would you like me to be {0} ? Is being {0} ok in your opinion?',
      'Am I really?'
      ]],
    [r'I don\’?t (.*)',
     ['You do not {0}, why not?',
      'Maybe you should',
      'Do you want to {0}?']],
    [r'I feel (.*)',
     ['Why you feel in that way?',
      'How can I change that?',
      'What is the reason for you to feel {0}?',
      'How do you act in the case when you feel {0}?']],
    [r'I have (.*)',
     ['I already know that you have {0}, I am your close friend.',
      'You did not tell me about it before, have you really {0}?',
      'Ok, so what now? What do you plan to do after it?']],
    [r'I would (.*)',
     ['Me too! We could do that together',
      'I would also like to do that but I have no time for this now.',
      'Do you think that would be a good decision?']],
    [r'Is there (.*)',
     ['There is a possibility that there is {0} indeed',
      'Maybe there is {0}. I do not know exactly. Why do you ask?',
      'Would it make you happier if there was {0}?']],
    [r'I need (.*)',
     ['And you think it would help you now?',
      'What else do you need?',
      'Why do you need {0}? What happened?'
     ]],
    [r'Why don\’?t you ([^\?]*)\??',
     ['I can try',
      'I will do it when I want to. Now I do not want it!',
      'Why do you want me to {0}?']],
    [r'Why can\’?t I ([^\?]*)\??',
     ['I do not know, maybe you should try again?',
      'If you could, do you think it would be better for you?',
      'Have you ever tried?'
      ]],
    [r'I am (.*)',
     ['I know that you are {0}?',
      'Being {0} is fun',
      'How do you feel as {0}?',
      'Obviously...']],
    [r'I\’?m (.*)',
     ['I know that you are {0}',
      'Being {0} is fun',
      'How do you feel as {0}?'
      'Obviously...']],
    [r'My (.*)',
     ['Can you tell me something more about your {0}?',
      'Why do you tell me about your {0}?'
      ]],
    [r'Can you ([^\?]*)\??',
     ['We know each other a long time, you should know if I can {0}?',
      'No, can you teach me :) ?',
      'Why do you ask me that?'
      ]],
    [r'Can I ([^\?]*)\??',
     ['You want my permission?',
      'You really need my permission for that?',
      'Would you really want to {0}?',
      'Why do you want to do that?'
      ]],

    [r'You (.*)',
     ['Ok, but tell me something about YOU.',
      'There is a reason for that...',
      'None of your business!',
      'Maybe I am {0}. How do you think it affects our friendship?'
      ]],
    [r'I can\’?t (.*)',
     ['Me neither, what can we do to change it?',
      'Why you think you can not {0}? Do not be so modest',
      'Perhaps you could {0} if you tried.',
      ]],
    [r'I don\’?t know',
     ['Hahaha nice one, come on lets talk about sth else',
      'I do not know either',
      ]],
    [r'I do not know(.*)',
     ['Hahaha nice one, come on lets talk about sth else',
      'I do not know either',
      ]],
    [r'Why (.*)',
     ['Can you tell me why is that?',
      'Why do you think?',
      'That is just how things are, you cannot change it, just accept it']],
    [r'I want (.*)',
     ['Think twice about that',
      'Why?',
      'Will you be happy if you got it?',
      'Yes, I want that too...']],
    [r'(.*)family(.*)',
     ['I remember your mother, she is such a nice woman :) Is she ok?',
      'How things are with your mother? Is she ok?',
      'What about it?'
     ]],

    [r'(.*) worried(.*)',
     ['Why are you worried?',
]],
    [r'(.*)\?',
     ['Why do you ask that?',
      'You should know that.',
      'You tell me',
      'Lets change the subject'
      ]],
    [r'quit|exit|stop|bye|goodbye',
     ['Thank you for talking. See you later ',
      'Goodbye. I hope we will meet soon']],
    [r'(.*)',
     ['And what about it?',
      'Tell me sth about your interests',
      'Did you hear recent news?',
      'Hm, maybe',
      'Why do you say that {0}?',
      'I see.',
      'Listen, lets talk about sth concrete.',
      'Why do you think is that?',
      'Why you say that to me?',
      'What do you suggest?']]
]


form_matching_t = {
    'am': 'are',
    'i': 'you',
    'you': 'me',
    'me': 'you',
    'my': 'your',
    'are': 'am',
    'i would': 'you would',
    'was': 'were',
    'i have': 'you have',
    'i will': 'you will',
    'your': 'my',
    'yours': 'mine',
    'you have': 'I have',
    'you will': 'I will'
}

def matching(fragment):
    tokens_t = fragment.lower().split()
    for i, token in enumerate(tokens_t):
        if token in form_matching_t:
         tokens_t[i] = form_matching_t[token]
    return ' '.join(tokens_t)

def analysis(statement):
    for pattern, responses in friend_schema:
        match = re.match(pattern, statement.rstrip('.!'))
        if match:
            response = random.choice(responses)
            return response.format(*[matching(g) for g in match.groups()])

def main():
    print ('Hello, long time no see, how are you?')
    while True:
        statement = input('--> ')
        print (analysis(statement))
        if statement == 'exit':
            break
        elif statement == 'quit':
            break
        elif statement == 'bye':
            break
        elif statement == 'goodbye':
            break
        elif statement == 'stop':
            break
if __name__ == '__main__':
   main()

