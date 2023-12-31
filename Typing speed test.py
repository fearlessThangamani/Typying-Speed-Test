import random
import time

# Sample sentences
sentences = [
    "Typing speed test. Press 'Enter' to begin.",
    "Python is an interpreted, high-level, general-purpose programming language.",
    "Speed and accuracy are the most important aspects of typing.",
    "Practice makes perfect!",
]

# Get a random sentence
sentence = random.choice(sentences)

def main():
    # Print the sentence
    print(sentence)
    
    # Start the timer
    start_time = time.time()
    
    # Get the user input
    user_input = input()
    
    # Calculate the time taken
    time_taken = time.time() - start_time
    
    # Calculate the number of characters typed
    characters_typed = len(user_input)
    
    # Calculate the number of words typed
    words_typed = len(user_input.split())
    
    # Calculate the typing speed (in words per minute)
    wpm = words_typed / (time_taken / 60)
    
    # Print the results
    print("\nTime taken:", round(time_taken, 2), "seconds")
    print("Characters typed:", characters_typed)
    print("Words typed:", words_typed)
    print("Typing speed:", round(wpm, 2), "words per minute")

if __name__ == "__main__":
    main()
