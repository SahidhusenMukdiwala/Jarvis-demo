import random

Hello = ('hello', 'hii', 'hey')

reply_Hello = ('Hello sir,Nice to meet you agin ')

bye = ('bye', 'exit', 'sleep', 'go')

reply_bye = ('bye sir')

how_are_you = ('how are you', 'Are you fine?')

reply_how = ('I am fine sir', 'How are you sir')

function = ['functions,abilities,feature']

reply_function = ('I can perform various task,How can i help you,let me ask you first how can i help you?')


def chatbox(Text):
    Text = str(Text)
    for word in Text.split():
        if word in Hello:
            reply = random.choice(reply_Hello)
            return reply
        elif word in bye:
            reply = random.choice(reply_bye)
            return reply
        elif word in how_are_you:
            reply = random.choice(reply_how)
            return reply


value = chatbox("hii")
print(value)
