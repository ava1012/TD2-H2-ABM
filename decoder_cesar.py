import sys
from cesar import cesar

texte = input()
decalage = int(sys.argv[1]) if len(sys.argv) > 1 else 3

print(cesar(texte, -decalage))