# ----- IMPORTS -----

import os
import sys
import random

from tqdm import tqdm
from PIL import Image, ImageFont

# ----- GLOBALS -----

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ALPHABET = [
    '\u0627', '\u0628', '\u062A', '\u062B', '\u062C', '\u062D', '\u062E', '\u062F', '\u0630', '\u0631', '\u0632',
    '\u0633', '\u0634', '\u0635', '\u0636', '\u0637', '\u0638', '\u0639', '\u063A', '\u0641', '\u0642', '\u0643',
    '\u0644', '\u0645', '\u0646', '\u0647', '\u0648', '\u064A', '\u0621', '\u0623', '\u0624', '\u0625', '\u0626',
    '\u0649'
]
ALPHABET_SIZE = len(ALPHABET)

FONTS_DIR_PATH = "fonts"
DEFAULT_FONT_SIZE = 36
DEFAULT_TEXT_COLOR = BLACK

font_paths = []
words_list = None

# ----- HELPER FUNCTIONS -----

# generates an image out of text
def generate_text_image(
        text,
        img_path,
        font_path,
        color = DEFAULT_TEXT_COLOR,
        font_size = DEFAULT_FONT_SIZE
    ):
    font = ImageFont.truetype(font_path, size=font_size)
    mask_image = font.getmask(text, "L")
    img = Image.new("RGBA", mask_image.size, color = WHITE)
    img.im.paste(color, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
    img.save(img_path)

# generate a random arabic word
def get_random_arabic_word():
    length = random.randint(3, 7);

    word = ""
    for i in range(length):
        word += random.choice(ALPHABET)

    return word

# pick a random arabic word from words list
def get_random_arabic_word_from_list():
    assert(words_list is not None)
    return random.choice(words_list)

# ----- MAIN PROGRAM -----

def main():
    # check for correct number of arguments
    if len(sys.argv) < 3:
        print("ARGUMENTS: <dataset_size> <dataset_dir_path> [<words_list]")
        return

    # get the arguments
    dataset_size = int(sys.argv[1])
    dataset_dir_path = sys.argv[2]
    words_list_file_path = None
    if len(sys.argv) >= 4:
        words_list_file_path = sys.argv[3]

    # get words list if given
    global words_list
    if words_list_file_path is not None:
        words_list = [line.strip() for line in open(words_list_file_path, "r").readlines()]

    # get all font paths
    font_paths = [FONTS_DIR_PATH + "/" + font for font in os.listdir(FONTS_DIR_PATH)]
    font_count = len(font_paths)

    # generate images
    for i in tqdm(range(dataset_size)):
        ### when generating random images
        # word = get_random_arabic_word()
        ### when picking from a words file
        word = get_random_arabic_word_from_list()

        font_path = random.choice(font_paths)
        img_path = dataset_dir_path + "/" + word + ".png"
        generate_text_image(word, img_path, font_path)

if __name__ == "__main__":
    main()
