import openai
import os
# Simple function to open path
def openFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = os.environ.get('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# ChatGPT Connection 
def gpt3Completion(prompt, engine='text-davinci-002', temp=0.8, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['USER:']):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop
    )
    text = response['choices'][0]['text'].strip()
    return text

# Console interface
def gpt3Interface(text):
    os.system('cls')
    option = None
    try:
        option = int(input("ChatGPT interface v0.1\nPlease select one of the following options:\n\n1. FreeChat: Chat with ChatGPT over the console.\n2. Image Generator: Create new photos in seconds !\n3. Random Fact: Try it and you'll see\n\nIf you would like to know more please refer to the documentation.\n\nSystem message: " + text + '\n\n' ))
    except ValueError:
        pass

    match option:
        case 0:
            gpt3Interface('Refresh')
        case 1:
            freeChat()
        case 2:
            imgGenerator()
        case 3:
            randomFact()
        case _:
            gpt3Interface('Invalid key. Try again')

# Console command to return or exit
def exitFunc(Input):
    if 'exit' == Input:
        gpt3Interface('Exit successful.')

# Simple call to openai for a random fact
def randomFact():
    random = gpt3Completion('Random fact. EXCLUDE(  :)')
    gpt3Interface(random)

# Console based chatbot
def freeChat():
    os.system('cls')
    conversation = list()
    print('I')
    while True:
        userInput = input('USER : ')
        exitFunc(userInput)
        conversation.append('USER : %s' % userInput)
        text_block = '\n'.join(conversation)
        prompt = openFile('chatPrompt.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nGPT'
        response = gpt3Completion(prompt)
        print('GPT' +response)
        conversation.append('ChatGPT%s' % response)
        
# Image generation from Dall-E
def imgGenerator():
    os.system('cls')
    print("Image Generator Friend is here !\nPlease enter a description. Ex: Statue of Liberty in a rock band")
    while True:
        default = 'Statue of Liberty in a rock band'
        userInput = input()
        if not userInput:
            userInput = default
        exitFunc(userInput)
        response = openai.Image.create(
            prompt=userInput,
            n=1,
            size="1024x1024"
        )
        imageUrl = response['data'][0]['url']
        print(imageUrl)

if __name__ == '__main__':
    gpt3Interface('Welcome !')