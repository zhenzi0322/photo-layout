import os
from PIL import Image
from .layout import LayoutModel


class LayoutImage(object):
    """
    图像排版
    """

    def __init__(self, layout: LayoutModel):
        self._layout = layout

    @staticmethod
    def set_pasts(image, img, row, column, space) -> Image:
        for i in range(column):
            x = img.width * i + space * i + space
            if image.width - img.width >= x:
                image.paste(img, box=(x, space))
                for j in range(row):
                    y = img.height * j + space * (j + 1)
                    if image.height - img.height >= y:
                        image.paste(img, box=(x, y))
        return image

    def create(self):
        if self._layout.imagePath and not os.path.exists(self._layout.imagePath):
            raise FileNotFoundError(f"imagePath image does not exist")
        row = self._layout.row
        column = self._layout.column
        canvas_color = self._layout.canvas.color
        space = self._layout.space
        img = Image.open(self._layout.imagePath)
        width, height = img.size
        canvas_width = self._layout.canvas.width
        canvas_height = self._layout.canvas.height
        if row and column:
            canvas_width = width * column + space * (column + 1)
            canvas_height = height * row + space * (row + 1)
        else:
            row = round(canvas_height / height)
            column = round(canvas_width / width)
        image = Image.new(mode="RGB", size=(canvas_width, canvas_height), color=canvas_color)
        image = self.set_pasts(image=image, img=img, row=row, column=column, space=space)
        img.close()
        return image
