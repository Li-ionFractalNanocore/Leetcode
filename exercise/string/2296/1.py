class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        c = 0
        while self.left and c < k:
            self.left.pop()
            c += 1
        return c

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if self.left:
                self.right.append(self.left.pop())
        left = max(0, len(self.left) - 10)
        return "".join(self.left[left:])

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if self.right:
                self.left.append(self.right.pop())
        left = max(0, len(self.left) - 10)
        return "".join(self.left[left:])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)


if __name__ == '__main__':
    # test case
    textEditor = TextEditor()
    textEditor.addText("leetcode")
    textEditor.deleteText(4)
    textEditor.addText("practice")
    textEditor.cursorRight(3)
    textEditor.cursorLeft(8)
    textEditor.deleteText(10)
    textEditor.cursorLeft(2)
    textEditor.cursorRight(6)