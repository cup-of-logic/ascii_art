from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
import pickle
from tqdm import tqdm


class Generate:
    def __init__(self, file_name: str):
        self.char_dict = {}
        self.file_name = file_name
        self.image_arr = None
        self.ascii_text = ''

        self.load_char_dict()
        self.load_image()
        self.create_ascii()
        self.save_as_image()

    def load_char_dict(self):
        with open("char_dict.pkl", mode='rb') as file:
            self.char_dict = pickle.load(file)

    def load_image(self):
        self.image_arr = np.array(Image.open(f"{self.file_name}.png").convert('L'))

    def create_ascii(self):
        progress_bar = tqdm(total=self.image_arr.shape[0] * self.image_arr.shape[1], desc="Creating ASCII Art")
        for row in range(self.image_arr.shape[0]):
            for col in range(self.image_arr.shape[1]):
                self.ascii_text += self.char_dict[self.image_arr[row][col]] + " "
                progress_bar.update(1)
            self.ascii_text += '\n'

    def save_as_image(self):
        font_size = 10
        font_width = 0.6
        font_height = 1.2
        width, height = int(self.image_arr.shape[1] * font_size * font_width * 2), int(self.image_arr.shape[0] * font_size * font_height)

        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font=r"C:\Windows\Fonts\consola.ttf", size=font_size)
        draw.text((0, 0), self.ascii_text, fill='black', font=font)

        img.save(f'{self.file_name}_ascii.png')


if __name__ == '__main__':
    Generate(file_name=r'images\3')
