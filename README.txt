==============================================================
                        BASIC CHATBOT
==============================================================

A simple command-line chatbot written in Python. It responds to
a small set of predefined phrases and exits when you say goodbye.


--------------------------------------------------------------
1. FEATURES
--------------------------------------------------------------
- Runs in the terminal / command prompt
- Case-insensitive input (hello, Hello and HELLO all work)
- Responds to greetings, a "how are you" question, and a farewell
- Gives a fallback reply for anything it doesn't understand
- Keeps running until you type "bye"


--------------------------------------------------------------
2. REQUIREMENTS
--------------------------------------------------------------
- Python 3.x
- No external libraries needed


--------------------------------------------------------------
3. HOW TO RUN
--------------------------------------------------------------
1. Save the file as Basic_chatbot.py
2. Open a terminal or command prompt in the file's folder
3. Run:

       python Basic_chatbot.py

   (On some systems you may need to use "python3" instead.)

4. Type a message and press Enter.


--------------------------------------------------------------
4. SUPPORTED COMMANDS
--------------------------------------------------------------
  You type         Chatbot replies
  --------------   -------------------------------------
  hello            hi!
  how are you      I'm fine, thanks!
  bye              Goodbye!  (and the program exits)
  anything else    sorry, i'm  unable to understand


--------------------------------------------------------------
5. EXAMPLE SESSION
--------------------------------------------------------------
  hello
  hi!
  how are you
  I'm fine, thanks!
  what is your name
  sorry, i'm  unable to understand
  bye
  Goodbye!


--------------------------------------------------------------
6. HOW IT WORKS
--------------------------------------------------------------
- Wish(data): Takes the user's input and compares it with the
  known phrases. It prints the matching reply. If the input is
  "BYE", it also returns the string "bye" to signal the program
  to stop.

- Main loop: Repeatedly reads input, converts it to uppercase
  with .upper() so matching is case-insensitive, and passes it
  to Wish(). When Wish() returns "bye", the loop breaks and the
  program ends.


--------------------------------------------------------------
7. HOW TO ADD NEW RESPONSES
--------------------------------------------------------------
Add another elif branch inside the Wish() function. Remember
to write the trigger phrase in UPPERCASE. For example:

    elif data=='WHAT IS YOUR NAME':
        print("I'm a basic chatbot!")


--------------------------------------------------------------
8. LIMITATIONS
--------------------------------------------------------------
- Only exact phrase matches work (e.g. "hello there" will not
  be recognised).
- Extra punctuation (e.g. "hello!") will not match.
- Replies are hard-coded; the bot does not learn or remember.


--------------------------------------------------------------
9. POSSIBLE IMPROVEMENTS
--------------------------------------------------------------
- Strip whitespace and punctuation from the input
- Use keyword matching instead of exact matching
- Store responses in a dictionary for easier maintenance
- Add more topics (time, date, jokes, etc.)


--------------------------------------------------------------
FILES
--------------------------------------------------------------
  Basic_chatbot.py   - the chatbot program
  README.txt         - this file

==============================================================
