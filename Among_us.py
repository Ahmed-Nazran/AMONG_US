import random
import time
class color:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YEL = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
def play():
    player = input("\nHello player please enter your name: \n")
    dumme = ["java","neko","python","pikaboy","html"]
    impo = random.choice(dumme)
    chat = ["HI!\n", f"What is {player} doing\n", "What is he doing\n", "VOTE Someone!!!\n","I am safe\n", "don't vote me please\n","where is he?\n"]
    print("SHhhhhh!\n")
    time.sleep(2)
    print("There is 1 imposters among us\n")
    print("You are white\n\n")
    time.sleep(1)
    while True:
        print(color.RED+"  ඞ       "+color.BLUE+"ඞ      "+color.GREEN+"    ඞ      "+color.YEL+"   ඞ      "+color.CYAN+" ඞ       "+color.ENDC+"  ඞ")
        print(color.RED+" Java   "+color.BLUE+" Neko     "+color.GREEN+" Python  "+color.YEL+" Pikaboy   "+color.CYAN+" HTML "+color.ENDC+f"   {player}\n\n")
        time.sleep(1)
        #blue
        print(color.BLUE+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #red
        print(color.RED+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #green
        print(color.GREEN+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #yellow
        print(color.YEL+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #cyan
        print(color.CYAN+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #blue
        print(color.BLUE+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #red
        print(color.RED+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #green
        print(color.GREEN+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #yellow
        print(color.YEL+random.choice(chat)+color.ENDC+"\n")
        time.sleep(1)
        #cyan
        print(color.CYAN+random.choice(chat)+color.ENDC+"\n")
        for i in range(4):
            vote = input("Enter player name\nVOTE: ").lower()
            if vote == impo:
                print(f"\n{impo} was the imposter")
                print(color.CYAN+"\n\n              VICTORY")
                exit()
            else:
                print(f"\n{vote} was not the imposter")
                
        print(color.RED+"\n\n               DEFEAT")
        print(color.RED+f"{impo} was the imposter"+color.ENDC)
while True:
    print("            Among Us\n")

    game = input(""" 
    <1> PLAY <1>
    <2> HOW TO PLAY <2>
    <3> EXIT <3>
    """)
    time.sleep(1)
    if game == "1":
        play()
    elif game == "2":
        print("""           AMONG US
        A game where you have to find the imposter and vote them out!
        \n
        """)
    elif game == "3":
        exit()
    else:
        print("Check your internet connection.")
