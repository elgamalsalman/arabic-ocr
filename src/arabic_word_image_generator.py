# ----- IMPORTS -----

from PIL import Image, ImageFont

# ----- GLOBALS -----

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DEFAULT_FONT_PATH = "/usr/share/fonts/opentype/freefont/FreeSerif.otf"
DEFAULT_FONT_SIZE = 36
DEFAULT_TEXT_COLOR = BLACK

# ----- HELPER FUNCTIONS -----

# generates an image out of text
def generate_text_image(
        text,
        img_path,
        color = DEFAULT_TEXT_COLOR,
        font_path = DEFAULT_FONT_PATH,
        font_size = DEFAULT_FONT_SIZE
    ):
    font = ImageFont.truetype(font_path, size=font_size)
    mask_image = font.getmask(text, "L")
    img = Image.new("RGBA", mask_image.size, color = WHITE)
    img.im.paste(color, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
    img.save(img_path)

# ----- MAIN PROGRAM -----

def main():
    generate_text_image("اهلا بِكُم معًا", "img.png");

if __name__ == "__main__":
    main()
