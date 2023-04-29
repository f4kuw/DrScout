Welcome on Dr Scout's github page ! 



Dr Scout is a very simple wordlist generator.
I'm not python developper just trying to learn some stuff.











Usage:
  example: You want to generate a custom wordlist because you lost your password and 
  remember it has something to do with your dog Jane and your birthday year which is 1967:
  
  python3 DrScout.py -k Jane 1967 -fP /some/wordlist/you/want/to/use/as/prefix -s potatoe 1968 Birkin dogs dog -oP passwordJane.txt
  
  This command-line will generate a wordlist passwordJane.txt that use as keyword Jane or 1967, concatened with all words in the wordlist specified
  and your suffixes (potatoe, 1968, Birkin, dogs and dog) as suffixes (ex : randomJanepotatoe)
  
  There's a default wordlist if you don't want to specify an external wordlist or words through arguments that contains few words/number/special characters.
  
  f4ku
