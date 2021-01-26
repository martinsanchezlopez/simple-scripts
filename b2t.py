
while True:
    inputStr = input("\n Binary to convert : ")
    noSpace = inputStr.replace(' ', '')


    addNb = 8 - len(noSpace) % 8
    
    if addNb!= 8:
        for i in range(0, addNb):
            noSpace = "0" + noSpace

    letters = int(len(noSpace))
    text="Conversion : "
    for j in range(0, letters, 8):
        text += (chr(int(noSpace[j:j+8], 2)))
    print(text)
