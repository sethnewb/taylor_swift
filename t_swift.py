import markovify as mrk

chorus = []

with open("all_tswift_lyrics.txt") as f:
    text = f.read()

text_model = mrk.Text(text)


for i in range(5):
    print(text_model.make_sentence())

print("")
print("[CHORUS]")
for i in range(3):
    line = text_model.make_short_sentence(280)
    chorus.append(line)
    print(line)

print("")
print("[VERSE]")
for i in range(5):
    print(text_model.make_sentence())

print("")
print("[CHORUS]")
for i in chorus:
    print(i)