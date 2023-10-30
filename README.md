Preparation:

Install the openai library if you haven't.
Set up the environment variable containing the OpenAI API key:
On Linux/macOS:

bash
Copy code
export OPENAI_API_KEY='YOUR_API_KEY_HERE'
On Windows (Command Prompt):

cmd
Copy code
set OPENAI_API_KEY=YOUR_API_KEY_HERE
On Windows (PowerShell):

powershell
Copy code
$env:OPENAI_API_KEY = 'YOUR_API_KEY_HERE'
Execute your Python script.
Console Interface Interaction:

bash
Copy code
ChatGPT interface v0.1
Please select one of the following options:

1. FreeChat: Chat with ChatGPT over the console.
2. Image Generator: Create new photos in seconds!
3. Random Fact: Try it and you'll see

If you would like to know more please refer to the documentation.

System message: Welcome!

> 1

I
USER : Hello GPT-3!
GPT: Hello! How can I assist you today?

USER : exit

System message: Exit successful.
...

> 2

Image Generator Friend is here!
Please enter a description. Ex: Statue of Liberty in a rock band

> A cat wearing a hat

http://dall-e-image-url.com/cat_wearing_hat

...

> 3

System message: Did you know? Honey never spoils. Archeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat.
Again, this scenario assumes:

You have set up the OpenAI API key as an environment variable.
You have the necessary permissions and credits to interact with both GPT-3 and DALL-E.
The chatPrompt.txt file is correctly formatted and located in the script's directory.
This scenario demonstrates a more secure interaction with OpenAI services using an environment variable instead of a plaintext file to store the API key. Using environment variables in this way ensures that secrets like API keys are not hard-coded in the code or stored in an easily accessible format, providing a layer of protection against inadvertent exposure or leaks.

Angel Millan Pirela 2023