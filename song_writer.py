import markovify as mrk

swift = "all_tswift_lyrics.txt"
tfb = "tfb.txt"


chorus = []
bridge = []

with open(tfb) as f:
    text = f.read()

text_model = mrk.Text(text)

title = text_model.make_short_sentence(35)
print('Title:' + title)

print("")
print("")
print("[VERSE 1]")
for i in range(5):
    print(text_model.make_short_sentence(100))

print("")
print("[CHORUS]")
for i in range(3):
    line = text_model.make_short_sentence(200)
    chorus.append(line)
    print(line)

print("")
print("[VERSE 2]")
for i in range(5):
    print(text_model.make_short_sentence(150))

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

print("")
print("[HOOK]")
for i in range(1):
    line = text_model.make_short_sentence(80)
    bridge.append(line)
    print(line + '[x8]')