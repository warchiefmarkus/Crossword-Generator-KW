# Crossword generator (Edited Fork)
Generates crosswords and exports them to htlm, png or ascii.

# Font 
To get the output font working on Ubuntu: 

1. use apt-get to install package `ttf-mscorefonts-installer`
2. edit `crossword.py` to have the correct path to `arial.ttf`
3. need questiosn file `lot_questions.cwf` , ttf font file
4. example of use !python3 crossword.py crosswords/lot_questions.cwf --create-image -o crossword.png --solved  
