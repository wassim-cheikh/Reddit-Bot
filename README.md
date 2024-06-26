# Reddit-Bot

Reddit-Bot is a Python bot designed to automate various actions on Reddit, including voting on posts and comments, commenting, and joining subreddits. It is built using Python 3.11.4 and leverages SeleniumBase 4.20.3 for web automation.

## Features

- **Automated Voting**: Upvote or downvote posts and comments.
- **Automated Commenting**: Post comments on specified posts.
- **Automated Subreddit Joining**: Join subreddits as specified.
- **Customizable Actions**: Configure multiple accounts and detailed actions.

## Prerequisites

- Python 
- SeleniumBase 

## Installation

1. Clone the repository:
   git clone [https://github.com/yourusername/Reddit-Bot.git](https://github.com/wassim-cheikh/Reddit-Bot)
   cd Reddit-Bot
2. Install the required dependencies:
    pip install -r requirements.txt

## Configuration

Before running the bot, you need to configure the constants.py file with your desired settings:

**ACCOUNTS** : A list that can contain one or many account objects referencing Reddit accounts to be used:
ACCOUNTS = [
    account('username1', 'password1'),
    account('username2', 'password2')
]

**UPVOTE_POST, DOWNVOTE_POST, UPVOTE_COMMENT, DOWNVOTE_COMMENT** : Lists containing the voting actions desired. Each list can contain one or many vote objects:
UPVOTE_POST = [
    vote('post_link1', 'subreddit_link1', 1),
    vote('post_link2', 'subreddit_link2', 2)
]

**COMMENT_ON_POST**: A list that can contain one or more comment objects:
COMMENT_ON_POST = [
    comment('post_link1', 'subreddit_link1', 'Great post!', 1)
]

**JOIN_SUBREDDIT**: A list that can contain one or more join objects:
JOIN_SUBREDDIT = [
    join('subreddit_link1', 1),
    join('subreddit_link2', 2)
]

**AUTO_JOIN**: Automatically join the subreddit when executing vote/comment actions. Default is True.

**SLEEP_TIME**: Pause time in seconds after completing all actions of a certain list. Default is 30 seconds.

**UPVOTE_POST_SLEEP**: Pause time in seconds after upvoting one post. Default is 20 seconds.

**DOWNVOTE_POST_SLEEP**: Pause time in seconds after downvoting one post. Default is 20 seconds.

**UPVOTE_COMMENT_SLEEP**: Pause time in seconds after upvoting one comment. Default is 20 seconds.

**DOWNVOTE_COMMENT_SLEEP**: Pause time in seconds after downvoting one comment. Default is 20 seconds.

**COMMENT_ON_POST_SLEEP**: Pause time in seconds after each comment. Default is 30 seconds.

**JOIN_SUBREDDIT_SLEEP**: Pause time in seconds after joining one subreddit. Default is 30 seconds.

**PROXY**: Proxy address to be used, for example, 'username:password@ip:port'.

## Usage

After setting up the constants.py file, run the bot using the following command:
python main.py
