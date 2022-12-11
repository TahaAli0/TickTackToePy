import asyncio
import random
import os


class Main:
    def __init__(self):
        self.name = None

        self.points = 0
        self.cpu_points = 0
        self.selection = None

        self.user = "X"
        self.cpu = "O"

        # 0-2-4-10-12-14-20-22-24 = Spots
        # 1-3-11-13-21-23 = Lines
        # 5-6-7-8-9-15-16-17-18-19 = Under-lines

        #  X | X | X
        # -----------
        #  X | X | X
        # -----------
        #  X | X | X

        self.map = [
            " 1 ", "|", " 2 ", "|", " 3 ",
            "\n---", "--", "--", "--", "--\n",
            " 4 ", "|", " 5 ", "|", " 6 ",
            "\n---", "--", "--", "--", "--\n"
            " 7 ", "|", " 8 ", "|", " 9 "
                    ]

    async def refresh_map(self):
        # os.system("cls")
        refreshed = ""

        selected_spot = self.selection
        index = 0

        for i in self.map:
            if self.map[index] == f" {selected_spot} ":
                refreshed += i
                index += 1

            else:
                refreshed += i
                index += 1
                continue

        print(refreshed)

    async def main(self):

        self.selection = input("Select a number from 1 to 9:\n")

        try:
            int(self.selection)
        except:
            print("That's not a number...")
            return

        await self.refresh_map()


game = Main()
asyncio.run(game.main())
