import itertools
import argparse
import time
import sys

print("""
            Welcome with Dr. Scout ! Give me keywords and a burger and I will give you a custom wordlist !
            You can use wordlists, custom keywords, prefixes, suffixes.
            This is my first script in Python.

                            ⢀⣴⣶⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢸⣿⣿⣿⣿⠇⠈⠉⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠸⣿⡃⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣀⣀⠀⠀
                            ⠀⣯⣧⠀⠀⠀⠀⠀⠀⠤⠔⠒⠛⠉⠉⠛⠛⠒⠶⢤⣠⠴⠒⠋⠉⠉⠀⠀⠀⠈⢿⣿⣿⡿⠀⠀
                            ⠀⠸⣿⣧⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⠀⠀⠀⠀⠀⠀⠀⠈⣩⣿⠁⠀⠀
                            ⠀⠀⠹⣟⠧⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⢠⣾⣱⠇⠀⠀⠀
                            ⠀⠀⠀⠙⢦⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⢀⡴⠋⣰⠋⠀⠀⠀⠀
                            ⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠖⠋⣠⡞⠁⠀⠀⠀⠀⠀
                            ⠀⠀⠀⣸⢣⣾⣿⣧⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⢀⣤⣤⡄⠸⣦⠶⠋⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢿⣤⠿⠛⠛⠒⠉⠉⠁⣿⠟⠒⠚⣷⠈⠉⠒⠤⢸⣿⣿⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠈⠙⠲⢤⣀⣀⠀⠀⠹⣄⣀⣠⠎⠀⠀⠀⠀⠀⣀⣠⡴⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⠁⠉⣹⣤⡆⠀⠀⣤⣀⣖⠒⠒⠈⢻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⡏⠰⢺⣿⣿⣿⠀⠀⣿⣿⡿⠋⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠁⠉⡟⠀⠀⢻⡛⠁⠀⠀⠀⠀⢳⣠⠶⠾⠧⠤⣄⣀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⣴⡃⠀⠀⣀⣧⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠈⠁⠻⠓⢄⡇⠀⠳⡄⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⢘⣆⠀⠀⠀
                            ⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⣤⣄⡀⠀⢰⣿⢿⡄⠀⠀
                            ⠀⠀⠀⠀⠐⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡇⠉⠉⠉⠙⠿⣅⡀⢧⡀⠀
                            ⠀⠀⠀⠀⠀⠙⠒⠦⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠴⠶⠖⠒⠛⠉⠀⠀⠀⠀⠀⠀  ⠾⠷⠀⠀⠀⠀⠀⠀⠀⠀

                            I hope you'll enjoy this little script !⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        Twitter: @_f4ku
                                        Github: f4kuw
"""

      )

# Create ArgumentParser object to assume arguments in cli
parser = argparse.ArgumentParser(
    description=" Welcome to Dr. Scout help ! This little script generate wordlists with custom keywords. You can use wordlists files, or add custom keywords, suffixes, prefixes with the followings arguments ! Enjoy - f4Ku")

default_wordlist = ["123","1","2","3","1111","4444","root","root_","admin","admin_","user","user_","@","!","?","$","*",":","^"] #Default wordlist used if

# Add prefix argument with:
parser.add_argument('-p', '--prefix', nargs='+', type=str, default=default_wordlist,
                    help='add prefixes to your keyword, separate by spaces')
parser.add_argument('-s', '--suffix', nargs='+', type=str, default=default_wordlist,
                    help='add suffixes to your keyword, separate by spaces')
parser.add_argument('-k', '--keyword', nargs='+', type=str, default=[],
                    help='enter keywords such as name, year of birth, be creative idk')
parser.add_argument('-oP', '--output', type=str, default='wordlist.txt',
                    help='enter the name of the output file, default will be wordlist.txt')
parser.add_argument('-fP', '--prefile', type=str, help='Use a previous generated wordlist for prefix')
parser.add_argument('-fS', '--sufile', type=str, help='Use a previous generated wordlist for suffix')

args = parser.parse_args()
prefix = args.prefix + ["admin", "user", "test", "guest", "root", "root_", "admin_", "user_", "1111", "1", "12", "1!",
                        ".1", "123", "1234", "!", "@", "#", "$", "%", "^", "&", "*", "9876"]
suffix = args.suffix + ["admin", "user", "test", "guest", "root", "root_", "admin_", "user_", "1111", "1", "12", "1!",
                        ".1", "123", "1234", "!", "@", "#", "$", "%", "^", "&", "*", "9876"]
keyword = args.keyword
output_file = args.output
pre_file = args.prefile
suf_file = args.sufile



if not keyword:
    print("Error: You need to submit at least one keyword.")
    print('use a keyword with -k')
    sys.exit()
if not prefix:
    if pre_file:  # If user specified a wordlist to use for prefixes
        print("You entered no prefix, but a wordfile")
        with open(pre_file, "r") as f:
            for line in f:
                prefix.append(line.strip())  # words are added to the prefix variable.
    else:
        print('You entered no prefix, and no wordlist, default will be use, type --help for help.')
else:
    if pre_file:
        print('You entered a wordlist and prefixes, both will be added in the wordlist.')
        with open(pre_file, "r") as f:
            for line in f:
                prefix.append(line.strip())
            
if not suffix:
    if suf_file:
        print("You entered no suffix, but a wordfile")
        with open(suf_file, "r") as f:
            for line in f:
                suffix.append(line.strip())
    else:
        print('You entered no sufix, and no wordlist, default will be use. Type --help for help.')
else:
    if suf_file:
        print("You entered both suffixes, and wordlist. Both will be add in the wordlist.")
        with open(pre_file, "r") as f:
            for line in f:
                suffix.append(line.strip())

print("\n\nGenerating wordlist. Please wait ! \ ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! ―― ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! / ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! | ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! \ ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! ―― ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! / ")
time.sleep(0.3)
print("\n\nGenerating wordlist. Please wait ! | ")
time.sleep(0.3)

combinations = itertools.product(prefix, [*keyword],
                                 suffix)  # Generate all combinations. (* is used to unpack the keyword list.)

wordlist = ["".join(comb) for comb in combinations]  # Create a wordlist variable.

with open(output_file, "w") as f:
    f.write("\n".join(wordlist))
    print("Wordlist ", output_file, "generated ! \nThank you for using f4ku Services & Cie !")
