from PIL import Image
import numpy as np 
import imagehash
import pickle


def TextExtractor(filename):
    # load the reference pictures library
    with open("reference_dict.pickle", 'rb') as handle:
        reference_pic_lib = pickle.load(handle)

    # load the screenshot
    img = np.asarray((Image.open(filename)).convert("L")).copy()
    (max_y, max_x) = img.shape

    # covert image to pure black and white (all non-black pixel set to white)
    brightness_threshold = 40
    for x in range(max_x):
        for y in range(max_y):
            if img[y, x] > brightness_threshold: 
                img[y, x] = 255 # set to white
            else: 
                img[y, x] = 0 # set to black


    # extract the text from the screenshot
    text = ""
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
                for i in range(len(reference_pic_lib[char])):
                    if abs(hash_value - reference_pic_lib[char][i]) < min_hash_diff:
                        min_hash_diff = abs(hash_value - reference_pic_lib[char][i])
                        most_like_char = char
            text += most_like_char
        text += "\n"
    
    return text


if __name__ == "__main__":
    print(TextExtractor("TestText.png"))
