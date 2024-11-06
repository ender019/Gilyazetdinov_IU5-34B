import sys

def get_coef(index, prompt):
    coef_str = sys.argv[index]; g=True
    while g:
        try:
            coef = float(coef_str)
            g=False
        except:
            print(prompt)
            coef_str = input()
    print(coef)
    return coef

class BiSqUr:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_disc(self):
        return self.b*self.b - 4*self.a*self.c

    def get_base_solve(self):
        d = self.get_disc()
        # print(d)
        if d<0: return -1,-1
        return (-self.b-d**0.5)/2, (-self.b+d**0.5)/2

    def get_solve(self):
        a, b = self.get_base_solve()
        # print(a,b)
        ans = []
        if a>0: ans += [-a**0.5, a**0.5]
        if b>0: ans += [-b**0.5, b**0.5]
        if len(ans) == 0: return "no solution"
        return ans