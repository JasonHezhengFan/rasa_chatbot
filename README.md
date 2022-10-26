# rasa_chatbot
To activate chatbot:
1. Make sure you have installed rasa.
2. "rasa shell" to activate bot.
3. Type "/stop" to stop the bot.
4. Use "rasa train" to retrain the bot after modifying yml files.

### Basic Files structure:
Domain.yml: 
1. Intents: What user can say to bot.
2. Response: What bot can reply, the bot won't say anything that's not on the lis.t

config.yml:
1. NLU pipeline(no need to worry about this until we have a lot of data)

nlu.yml:
1. Training data for each intent.

rules.yml:
1. Hard coded