from game import Game

def main():
    b = Game()
    b.make_move(1)
    print(str(b))
    print([b])
    
    
if __name__ == "__main__":
    main()