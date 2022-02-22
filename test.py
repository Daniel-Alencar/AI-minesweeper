from minesweeper import Minesweeper, Sentence

mine = Minesweeper(height=8, width=8, mines=8)
sentence = Sentence(count=2, cells=[(1,1), (2,3), (5,2)])
print(sentence)

sentence.mark_safe((2,3))
print(sentence)

A = {1,2,3,4,5}
B = {1,2,3}

print(A - B)