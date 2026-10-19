arr=[1,2,3,4]
sum=0
for i in range(len(arr)):
    if not i%2==0:
      sum+=arr[i]
print(sum)

word = input("Enter a word: ")

reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("Reversed word:", reversed_word)


def count_word():
    sentence=input("enter text :")
    result=len(sentence)
    return result
print(count_word())

myDict = {"name":"gisubizo","class":"DSI","course":"python"}

print(myDict)