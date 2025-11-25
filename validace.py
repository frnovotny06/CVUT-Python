class Tag:

    def __init__(self, name: str, kind: str):
        self.name = name
        self.kind = kind


class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        if not self.data:
            return None
        return self.data.pop()

    def top(self):
        if not self.data:
            return None
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


class controlor:


    def __init__(self):
        self.stack = Stack()
        self.tags_parove = []
        self.tags_unikatni = set()

    def tagnamer(self, text: str):


        text = text.strip()
        if not text:
            return None


        if text.endswith('/'):
            name = text[:-1].strip()
            if name.isalpha():
                return Tag(name, "single")
            return None



        if text.startswith('/'):
            name = text[1:].strip()
            if name.isalpha():


                return Tag(name, "close")
            return None


        if text.isalpha():
            return Tag(text, "open")

        return None

    def recognise(self, s: str):


        if not s or not s.startswith('<'):
            return (False, None, [])

        i = 0
        n = len(s)

        while i < n:
            if s[i] != '<':
                i += 1
                continue

            j = s.find('>', i+1)
            if j == -1:
                return (False, None, [])

            l = s[i+1:j]

            tag = self.tagnamer(l)
            if tag is None:
                return (False, None, [])


            self.tags_parove.append(tag.name)
            self.tags_unikatni.add(tag.name)


            if tag.kind == "open":
                self.stack.push(tag.name)

            elif tag.kind == "close":
                top = self.stack.pop()
                if top != tag.name:
                    return (False, None, [])



            i = j + 1


        if not self.stack.empty():
            return (False, None, [])

        return (True, len(self.tags_parove), list(self.tags_unikatni))


def xml(s: str):
    validator = controlor()
    reult = validator.recognise(s)
    print(reult)
    return reult


xml('<a><b></a></b>')




