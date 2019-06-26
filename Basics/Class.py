class Duck:
    quacking = "Quaaak!!"

    walking = 'walks liks a duck'


    def quack(self):
        print(self.quacking)

    def walk(self):
        print(self.walking)

def main():
    ankit = Duck()
    ankit.quack()
    ankit.walk()


if __name__ == '__main__': main() 