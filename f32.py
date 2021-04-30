class C32:
    status = 'A'

    def __init__(self):
        self.status = 'A'

    def color(self):
        try:
            if self.status == 'A':
                self.status = 'F'
                return 1
            if self.status == 'B':
                self.status = 'C'
                return 2
            if self.status == 'C':
                self.status = 'D'
                return 4
            if self.status == 'D':
                self.status = 'D'
                return 6
            if self.status == 'F':
                self.status = 'D'
                return 8
        except RuntimeError:
            print("RuntimeError")

    def sort(self):
        try:
            if self.status == 'A':
                self.status = 'B'
                return 0
            if self.status == 'B':
                self.status = 'E'
                return 3
            if self.status == 'D':
                self.status = 'E'
                return 5
            if self.status == 'E':
                self.status = 'F'
                return 7
        except RuntimeError:
            print("RuntimeError")

