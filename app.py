from os import path, listdir
from sys import argv, exit
from shutil import copyfile
from random import sample
from progress.bar import IncrementalBar


def get_params():
    if len(argv) == 4:
        directory = argv[1]
        flash = argv[1]
        limit = int(argv[1])
    else:
        if (
            input(
                "You didn'o't enter required parameters. Want to enter them now? [Y / n]:"
            )
            == "n"
        ):
            exit()
        else:
            while True:
                directory = input(
                    "Please, enter directory with your music, or 'quit' to quit:"
                )
                if path.exists(directory):
                    print("Directory {} accepted.".format(directory))
                    break
                elif directory.lower() == "quit":
                    exit()
                else:
                    print("Directory {} does not exist!".format(directory))

            while True:
                flash = (
                    input("Please, enter flash disk letter or 'quit' to quit:") + ":\\"
                )
                if path.exists(flash):
                    print("Flash disk on {} accepted.".format(flash))
                    break
                elif flash.lower() == "quit":
                    exit()
                else:
                    print("Flash disk on {} not found!".format(flash))

            while True:
                limit = input("Please, enter amount of files or 'quit' to quit:")
                if limit.isdigit():
                    print("{} file limit accepted.".format(limit))
                    limit = int(limit)
                    break
                elif limit.lower() == "quit":
                    exit()
                else:
                    print("Incorrect number {}!".format(limit))
    return directory, flash, limit


def main(args):
    directory, flash, limit = args
    print("OK, arguments are:{} {} {}".format(directory, flash, str(limit)))
    print("Let's start!")
    all_music = []
    for file in listdir(directory):
        if file.endswith(".mp3"):
            all_music.append(file)
    print("{} files found in {}".format(str(len(all_music)), directory))
    random_music = sample(all_music, min(len(all_music), limit))
    digit = 0
    bar = IncrementalBar("Processing...", max=len(random_music))
    for file in random_music:
        digit += 1
        copyfile(directory + "\\" + file, flash + "\\" + str(digit) + " " + file)
        bar.next()

    bar.finish()
    print("Job well done! {} files copied to {}".format(len(random_music), flash))


if __name__ == "__main__":
    main(get_params())