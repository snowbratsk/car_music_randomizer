import sys
import os
import random
import shutil


def get_params():
    if len(sys.argv) == 4:
        directory = sys.argv[1]
        flash = sys.argv[1]
        limit = int(sys.argv[1])
    else:
        if (
            input(
                "You didn'o't enter required parameters. Want to enter them now? [Y / n]:"
            )
            == "n"
        ):
            sys.exit()
        else:
            while True:
                directory = input(
                    "Please, enter directory with your music, or 'quit' to quit:"
                )
                if os.path.exists(directory):
                    print("Directory {} accepted.".format(directory))
                    break
                elif directory.lower() == "quit":
                    sys.exit()
                else:
                    print("Directory {} does not exist!".format(directory))

            while True:
                flash = (
                    input("Please, enter flash disk letter or 'quit' to quit:") + ":\\"
                )
                if os.path.exists(flash):
                    print("Flash disk on {} accepted.".format(flash))
                    break
                elif flash.lower() == "quit":
                    sys.exit()
                else:
                    print("Flash disk on {} not found!".format(flash))

            while True:
                limit = input("Please, enter amount of files or 'quit' to quit:")
                if limit.isdigit():
                    print("{} file limit accepted.".format(limit))
                    limit = int(limit)
                    break
                elif limit.lower() == "quit":
                    sys.exit()
                else:
                    print("Incorrect number {}!".format(limit))
    return directory, flash, limit


def main(args):
    directory, flash, limit = args
    print("OK, arguments are:{} {} {}".format(directory, flash, str(limit)))
    print("Let's start!")
    all_music = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            all_music.append(file)
    print("{} files found in {}".format(str(len(all_music)), directory))
    random_music = random.sample(all_music, min(len(all_music), limit))
    digit = 0
    for file in random_music:
        digit += 1
        shutil.copyfile(directory + "\\" + file, flash + "\\" + str(digit) + " " + file)


if __name__ == "__main__":
    main(get_params())