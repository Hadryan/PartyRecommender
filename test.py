import os
import tekore as tk
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    user_token = tk.prompt_for_user_token(
        os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('REDIRECT_URI'),
        scope=tk.scope.every
    )
    spotify = tk.Spotify(user_token)
    print(spotify.current_user().id)