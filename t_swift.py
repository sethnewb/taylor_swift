import markovify as mrk

chorus = []
bridge = []

with open("all_tswift_lyrics.txt") as f:
    text = f.read()

text_model = mrk.Text(text)

print("")
print("")
print("[VERSE 1]")
for i in range(5):
    print(text_model.make_sentence())

print("")
print("[CHORUS]")
for i in range(3):
    line = text_model.make_short_sentence(280)
    chorus.append(line)
    print(line)

print("")
print("[VERSE 2]")
for i in range(5):
    print(text_model.make_sentence())

print("")
print("[CHORUS]")
for i in chorus:
    print(i)

print("")
print("[BRIDGE]")
for i in range(2):
    line = text_model.make_short_sentence(120)
    bridge.append(line)
    print(line)

for i in bridge:
    print(i)

print("")
print("[CHORUS]")
for i in chorus:
    print(i)