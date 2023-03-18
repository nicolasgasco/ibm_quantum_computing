from count import text_analyzer

print("\033[93m" + "Test 1: No argument" + "\033[0m")
text_analyzer()

print("\033[93m" + "Test 2: None" + "\033[0m")
text_analyzer(None)

print("\033[93m" + "Test 3: Not a string" + "\033[0m")
text_analyzer(42)

print("\033[93m" + "Test 4: Empty string" "\033[0m")
text_analyzer("")

print("\033[93m" + "Test 5: Hello World!" + "\033[0m")
text_analyzer("Hello World!")

print("\033[93m" + "Test 6: Hello World! 42" + "\033[0m")
text_analyzer("Hello World! 42")

print("\033[93m" + "Test 7: Only lowercase" + "\033[0m")
text_analyzer("hello world")

print("\033[93m" + "Test 8: Only uppercase" + "\033[0m")
text_analyzer("HELLO WORLD")

print("\033[93m" + "Test 9: Only punctuation" + "\033[0m")
text_analyzer(".,!?;:")

print("\033[93m" + "Test 10: Only spaces" + "\033[0m")
text_analyzer("   ")

print("\033[93m" + "Test 11: Only numbers" + "\033[0m")
text_analyzer("42")

print("\033[93m" + "Test 12: Only numbers and spaces" + "\033[0m")
text_analyzer("42 42 42")

print("\033[93m" + "Test 13: Only numbers and punctuation" + "\033[0m")
text_analyzer("42,42,42")

print("\033[93m" + "Test 14: example 1 from subject" + "\033[0m")
text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")

print("\033[93m" + "Test 15: example 2 from subject" + "\033[0m")
text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")

print("\033[93m" + "Test 16: example 3 from subject" + "\033[0m")
text_analyzer("Hello World!")
