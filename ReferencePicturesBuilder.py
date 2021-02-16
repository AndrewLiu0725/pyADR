from PIL import Image
import numpy as np 
 
img = np.asarray((Image.open("./Figures/CharReference.png")).convert("L")).copy()
(max_y, max_x) = img.shape

# covert the reference image to pure black and white (all non-black pixel set to white)
brightness_threshold = 40
for x in range(max_x):
    for y in range(max_y):
        if img[y, x] > brightness_threshold:
            img[y, x] = 255
        else:
            img[y, x] = 0

#Image.fromarray(img).show()

# L = left, R = right, T = top, B = bottom
count = 0
pic_count = 0
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

        #print(img[Top_refined:Bottom_refined, Left:Right], "\n\n\n")
        im = Image.fromarray(img[Top_refined:Bottom_refined, Left:Right])
        if pic_count > 9:
            if pic_count % 2 == 0:
                filename = "uppercase_"+chr(int(65+(pic_count-10)/2))
            else:
                filename = "lowercase_"+chr(int(97+(pic_count-10)/2))
        else:
            filename = pic_count
        im.save("./Figures/ReferencePictures/{}.png".format(filename))
        pic_count += 1
        