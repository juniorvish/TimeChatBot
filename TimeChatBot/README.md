# TimeChatBot

A Discord bot that allows users to chat in a specific channel only between the allowed time period (8PM IST to 10PM IST). Messages sent outside of this time period will be deleted.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/TimeChatBot.git
```

2. Change to the project directory:

```
cd TimeChatBot
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `config.py` file in the project directory and add your Discord bot token:

```python
TOKEN = "your_discord_bot_token_here"
```

## Usage

1. Run the bot:

```
python main.py
```

2. Invite the bot to your Discord server and grant it the necessary permissions.

3. Set up a channel where the time restriction will be applied.

4. Enjoy chatting in the time-restricted channel between 8PM IST and 10PM IST!