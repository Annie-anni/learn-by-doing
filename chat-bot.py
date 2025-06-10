import random
import time

def chat_bot():
    grettings = ["Hello there!","Hi friend!","Hey nice to meet you!","Hey how do you do?"]

    farewells = ["Goodbye","See you later","Until next time"]

    puns = ["Taking off your pants to fart -- Doing something totally unnecessary.",
                                "Throwing a meat bun at a dog -- Something you acn't get back.",
                                "A toad squatting on your foot -- It doesn't bite,but it annoys you.",
                                "Playing the lute to a cow -- Explaining something to someone who doesn't understand.",
                                "Drawing a snake and adding feet -- Doing something unnecessary that ruins the original."]

    jokes = ["Why don't scientists trust atoms? Because they make up everthing!"
             ,"What do you call a fake noodle? An impasta!",
             "I told my doctor 'I broke my arm in two places' He said 'Stop going to those places!'"]

    facts = ["Honey never spoils. Archaeologists found 3000-year-old honey that's still good",
             "Octopuses have three hearts and hearts","Turtles can breathe through their butts",
             "The spicier the chili,the more pain recepors it activates-not taste buds",
             "Chickens are the closest living relatives of the Tyrannosaurus rex"]

    bot_name = "ChatBot"
    print(f"{bot_name} is starting up...")
    time.sleep(1)

    print(f"""Welcome to {bot_name}!
          I can chat about:
          'puns' - Learn some funny puns
          'joke' - Hear a funny joke
          'fact' - Learn something new
          'color' My favorite color
          'bye - End our chat""")

    chatting = True
    user_name = input("What's your name: ").lower().strip()
    print(f"{bot_name}: Nice to meet you {user_name}! How can I help you today?")

    while chatting:
        user_input = input("You: ").strip()

        if user_input in ["hi","hello","hey","how"]:
            print(f"{bot_name}: {random.choice(grettings)}")
        elif "puns" in user_input:
            print(f"{bot_name}: {random.choice(puns)}")
        elif "joke" in user_input:
            print(f"{bot_name}: {random.choice(jokes)}")
        elif "fact" in user_input:
            print(f"{bot_name}: {random.choice(facts)}")
        elif "color" in user_input:
            print("My favorite color is black.What's yours?")
            color = input("You: ").strip()
            print(f"{bot_name}: {color} is a great color!")
        elif user_input in ["bye","goodbye","exit","quit"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"It was fun chatting with you {user_name}!")
            chatting = False
        else:
            response = ["That's interesting! Tell me more.",
                        "I'm not sure I understand. Can you try again?",
                        "Hmm, let's talk something else. Try asking me about a joke or fact."]
            print(f"{bot_name}: {random.choice(response)}")
    print("Thanks for chatting! Run the program again to talk to me later.")

chat_bot()
                    
        