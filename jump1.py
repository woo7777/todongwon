word = str(input('단어를 입력하세요'))
if word[0] == word[-1]:
    print("뒤집힌 단어는:", word[-1])
    print("입력된 단어는 회문입니다:", word[::-1])
else :
    print("입력된 단어는 회문이 아닙니다.")