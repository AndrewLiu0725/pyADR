from PIL import Image
import numpy as np 
import imagehash
import pickle
 
img = np.asarray((Image.open("./Figures/CharReference_stronger.png")).convert("L")).copy()
(max_y, max_x) = img.shape

# covert the reference image to pure black and white (all non-black pixel set to white)
brightness_threshold = 40
for x in range(max_x):
    for y in range(max_y):
        if img[y, x] > brightness_threshold:
            img[y, x] = 255
        else:
            img[y, x] = 0

Image.fromarray(img).show()

# L = left, R = right, T = top, B = bottom
row_count = 0
reference_pic_hash_lib = {}
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
    char_count_this_line = 0
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

        # build reference
        hash0 = imagehash.average_hash(Image.fromarray(img[Top_refined:Bottom_refined, Left:Right]))

        if row_count >= 0 and row_count < 10: # digit
            this_char = str(char_count_this_line)

        elif row_count >= 10 and row_count < 20: # english alphabet
            if char_count_this_line % 2 == 0:
                this_char = chr(int(65 + char_count_this_line/2))
            else:
                this_char = chr(int(97 + char_count_this_line/2))
        
        else: # dot
            this_char = '.'

        if this_char in reference_pic_hash_lib.keys():
                if not (hash0 in reference_pic_hash_lib[this_char]):
                    reference_pic_hash_lib[this_char].append(hash0)
        else:
            reference_pic_hash_lib[this_char] = [hash0]

        char_count_this_line += 1
    row_count += 1


# store the reference dict
with open("reference_dict.pickle", 'wb') as handle:
    pickle.dump(reference_pic_hash_lib, handle, protocol=pickle.HIGHEST_PROTOCOL)
