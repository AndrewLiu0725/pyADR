from PIL import Image
import numpy as np 
import os
import imagehash
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

DEBUG = 1


# build reference pictures library
reference_folder = "./Figures/ReferencePictures/"

reference_pic_lib = {} # (char: hash value)
for fn in os.listdir(reference_folder):
    reference_pic_lib[fn[-5]] = imagehash.average_hash(Image.open(reference_folder+fn))

# preprocess the image by comparing each char with the reference library
char_count = 0

img = np.asarray((Image.open("TestText.png")).convert("L")).copy()
(max_y, max_x) = img.shape

# covert image to pure black and white (all non-black pixel set to white)
brightness_threshold = 40
for x in range(max_x):
    for y in range(max_y):
        if img[y, x] > brightness_threshold: 
            img[y, x] = 255 # set to white
        else: 
            img[y, x] = 0 # set to black

if DEBUG:
    print("----------------------------------------------------------------")
    print("Before preprocessed:\n")
    print(pytesseract.image_to_string(Image.fromarray(img)))


# L = left, R = right, T = top, B = bottom
Bottom = -1
while True:
    FoundTop = 0
    Top = Bottom + 1

    # find top row for current line
    while (Top < max_y):
        if np.any(img[Top, :]):
            FoundTop = 1
            break
        else:
            Top += 1
    
    # break if there is no line remanined
    if FoundTop:
        Bottom = Top + 1
    else:
        break

    # find bottom row for current line
    while (Bottom < max_y):
        if np.any(img[Bottom, :]):
            Bottom += 1
        else:
            break
    Bottom -= 1 # last row which is not all black

    # parse the current line
    Right = -1
    while True:
        FoundLeft = 0
        Left = Right + 1

        # find left column for current character
        while (Left < max_x):
            if np.any(img[Top:Bottom, Left]):
                FoundLeft = 1
                break
            else:
                Left += 1

        # break if there is no character remained
        if FoundLeft:
            Right = Left + 1
        else:
            break

        # find right column for current character
        while (Right < max_x):
            if np.any(img[Top:Bottom, Right]):
                Right += 1
            else:
                break

        Right -= 1

        # refine the top and bottom row for this char
        Top_refined = Top

        while (Top_refined <= Bottom):
            if np.any(img[Top_refined, Left:Right]):
                break
            else:
                Top_refined += 1

        Bottom_refined = Top_refined + 1

        while (Bottom_refined <= Bottom):
            if np.any(img[Bottom_refined, Left:Right]):
                Bottom_refined += 1
            else:
                break

        Bottom_refined -= 1 # last row which is not all black

        # recongnize the current char
        hash_value = imagehash.average_hash(Image.fromarray(img[Top_refined:Bottom_refined, Left:Right]))

        min_hash_diff = 100
        for char in reference_pic_lib.keys():
            if abs(hash_value - reference_pic_lib[char]) < min_hash_diff:
                min_hash_diff = abs(hash_value - reference_pic_lib[char])
                most_like_char = char

        # preprocessed the image
        if most_like_char == '1':
            img[Top_refined:Bottom_refined, Left:int((Left+Right)/2)] = 0
        
        elif most_like_char == '0' or most_like_char == 'o' or most_like_char == 'O':
            FoundZeroTop = 0

            # find inner top and bottom
            for y in range(Top_refined, Bottom_refined+1):
                if img[y, int((Left+Right)/2)] == 0:
                    if FoundZeroTop:
                        ZeroBottom = y
                    else:
                        ZeroTop = y
                        FoundZeroTop = 1

            # find inner left
            for x in range(Left, Right+1):
                if img[int((Top_refined+Bottom_refined)/2-(Bottom_refined-Top_refined)/5), x] == 0:
                    ZeroLeft = x
                    break

            # find inner right
            for x in reversed(range(Left, Right+1)):
                if img[int((Top_refined+Bottom_refined)/2+(Bottom_refined-Top_refined)/5), x] == 0:
                    ZeroRight = x
                    break

            # fill the center with black pixels
            img[ZeroTop: ZeroBottom+1, ZeroLeft:ZeroRight+1] = 0     

#Image.fromarray(img).show()

# Extract the text from screenshot
if DEBUG:
    print("----------------------------------------------------------------")
    print("After preprocessed:\n")
print(pytesseract.image_to_string(Image.fromarray(img)))