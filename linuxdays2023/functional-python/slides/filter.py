#
# Použití funkce vyššího řádu filter
#

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = filter(lambda word: len(word) > 4, words)
print(list(filtered))
