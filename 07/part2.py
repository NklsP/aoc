# get lines to array
file = open('07/input1.txt', 'r')
Lines = file.read().splitlines()

Rules = []

class Rule():
    def __init__(self, rule=""):
        self.rule = rule
        self.bag = ""
        self.contents = []
        self.quantitys = []

        self.bag = Bag(rule.split(" bags contain ")[0])

        if "no other bags." not in rule:
            for content in rule.split(" bags contain ")[1].split(","):
                self.quantitys.append(int(content.lstrip().split(" ")[0]))
                self.contents.append(content.lstrip().split(content.lstrip().split(" ")[0])[1].strip())
        else:
            self.bag.basgInside = 0
    
    def __str__(self):
        return self.bag.color
    def __len__(self):
        if len(self.quantitys) == 0:
            self.bag.basgInside = 0
            return 0
        return max(self.quantitys)
            

class Bag():
    def __init__(self, color, bagsInside=1):
        self.color = color
        self.basgInside = bagsInside
    def __str__(self):
        return self.color