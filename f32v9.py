class C32:
    status = 'A'

    def __init__(self):
        self.status = 'A'

    def order(self):
        try:
            if self.status == 'B':
                self.status = 'C'
                return 1
            if self.status == 'C':
                self.status = 'D'
                return 3
            if self.status == 'D':
                self.status = 'E'
                return 5
            if self.status == 'F':
                self.status = 'A'
                return 8
        except RuntimeError:
            print("RuntimeError")

    def reset(self):
        try:
            if self.status == 'A':
                self.status = 'B'
                return 0
            if self.status == 'B':
                self.status = 'D'
                return 2
            if self.status == 'D':
                self.status = 'D'
                return 6
            if self.status == 'C':
                self.status = 'E'
                return 4
            if self.status == 'E':
                self.status = 'F'
                return 7
        except RuntimeError:
            print("RuntimeError")

