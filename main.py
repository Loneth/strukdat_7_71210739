class Browser:
    def __init__(self):
        self.data: list = []
        self.list_url: list = []
        self.index = 0

    def __len__(self):
        return len(self.data)

    def go(self, url: str):
        self.list_url.append(url)
        self.data.append(url)
        self.index += 1

    def back(self):
        self.data.pop()
        self.index -= 1
        print(self.data[self.index - 1])

    def forward(self):
        self.data.append(self.list_url[self.index])
        print(self.data[self.index])

    def printAll(self):
        for x in self.data:
            print(x, end=' ')


browser = Browser()
browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")
browser.back()  # output: https://ukdw.ac.id
browser.back()  # output: https://google.com
browser.forward()  # output: https://ukdw.ac.id
browser.go("https://twitter.com")
browser.printAll()  # output: https://google.com https://ukdw.ac.id https://twitter.com
