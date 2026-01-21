import instaloader

# 1. Use a stable, standard User-Agent
CHROME_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

M = instaloader.Instaloader(user_agent=CHROME_UA)

# 2. Re-copy the sessionid ONLY after refreshing your browser one last time
SESSION_ID = "77373578060%3AM2L2tGN3ALdAcu%3A19%3AAYi0h2h8UTxKW9wyU0vIy8CbsBMcVoRWG8X1kWIG3g"

M.context._session.cookies.set("sessionid", SESSION_ID, domain=".instagram.com")

try:
    # We use a lower-level check to avoid triggering the 'Login required' loop
    if M.test_login() == "sophoz07":
        print("Success! Handshake confirmed.")
        # This saves the session so you don't need the ID anymore
        M.save_session_to_file(filename="Sophoz07") 
        print("Session file 'Sophoz07' is now locked and loaded.")
    else:
        print("The server rejected the ID. Refresh Chrome and try one more time.")
except Exception as e:
    print(f"Connection error: {e}")