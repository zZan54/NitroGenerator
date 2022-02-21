import numpy
import string
import time

class DiscordNitroGenerator:
    def main(gen):
        discordnitrogen = """  _  _ _ _            ___                       _           
 | \| (_) |_ _ _ ___ / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 | .` | |  _| '_/ _ \ (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_|\_|_|\__|_| \___/\___\___|_||_\___|_| \__,_|\__\___/_|  """
        print(discordnitrogen)
        print(" by github.com/zZan54")
        print(" ")
        gen.slowType("How many codes to generate: ", 0.05, newLine = False)
        try:
            num = int(input(" "))
        except ValueError:
            input("That isn't a number.\nPress enter to exit")
            exit()
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

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