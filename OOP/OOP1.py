class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created")

or1 = Orange(10, 'Dark Orange')
or1.color = 'light orange'
or1.weight = 100

print(or1.color)
print(or1.weight)


or2 = Orange(1, 'dark orange')
or3 = Orange(20, 'yellow')
