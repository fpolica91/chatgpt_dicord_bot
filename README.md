# ChatGPT Discord Bot Template

This template was adapted from [here](https://github.com/Zero6992/chatGPT-discord-bot)

Reverse Engineered ChatGPT by OpenAI [here](https://github.com/acheong08/ChatGPT). 

# Setup

This assumes you have a Discord account, server and a role in that server with priviliges to set up a bot.

## Create a Discord bot

1. Go to https://discord.com/developers/applications create an application.
2. And build a bot under the application.
3. Get the token from Bot setting.
   ![1670143818339](image/README/1670143818339.png)
4. Store the token in Secrets as an environment variable with the name `DISCORD_BOT_TOKEN`
   ![1670176461891](image/README/1670176461891.png)
5. Turn MESSAGE CONTENT INTENT `ON`
   ![1670176647431](image/README/1670176647431.png)
6. Invite your bot through OAuth2 URL Generator
   ![1670176722801](image/README/1670176722801.png)

## Get your session token
Go to https://chat.openai.com/chat from the Chrome browser and log in
1. Open Chrome DevTools 
2. Open `Application` tab > Cookies
   ![image](https://user-images.githubusercontent.com/36258159/205494773-32ef651a-994d-435a-9f76-a26699935dac.png)
3. Copy the value for `__Secure-next-auth.session-token` and add it to Secrets as an environment variable with the name `CHAT_GPT_SESSION_TOKEN`
   ![1670176444011](image/README/1670176444011.png)

## DM your ChatGPT bot in Discord

   ![1670177247310](image/README/1670177247310.png)