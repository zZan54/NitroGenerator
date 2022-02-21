import numpy
import string
import time

class DiscordNitroGenerator:
    def main(gen):
        discordnitrogen = """  _  _ _ _            ___                       _           
 | \| (_) |_ _ _ ___ / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 | .` | |  _| '_/ _ \ (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_|\_|_|\__|_| \___/\___\___|_||_\___|_| \__,_|\__\___/_|  """
        time.sleep(1)
        print(discordnitrogen)
        print(" by github.com/zZan54")
        print(" ")
        time.sleep(1.5)
        gen.slowType(" How many codes to generate: ", 0.05, newLine = False)
        try:
            num = int(input(" "))
        except ValueError:
            input(" That isn't a number.\n Press enter to exit")
            exit()
        print(" ")
        print(" 1 - With https://")
        print(" 2 - Without https://")
        print(" 3 - Only the code")
        print(" ")
        gen.slowType(" Type of code generation: ", 0.05, newLine = False)
        try:
            type = int(input(" "))
        except ValueError:
            input(" That isn't a number.\n Press enter to exit")
            exit()
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                
                url1 = f" https://discord.gift/{code}"
                url2 = f" discord.gift/{code}"
                url3 = f" {code}"
                if type == 1:
                    url = url1
                elif type == 2:
                    url = url2
                elif type == 3:
                    url = url3
                print(url)
            except KeyboardInterrupt:
               break
    def slowType(gen, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

Gen = DiscordNitroGenerator()
Gen.main()
