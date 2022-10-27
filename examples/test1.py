from photo_layout.layout import Canvas, LayoutModel
from photo_layout.image import LayoutImage


def main():
    canvas = Canvas(color="pink")
    layout_model = LayoutModel(canvas=canvas, imagePath="test.jpg", row=3, column=3, space=10)
    layout_image = LayoutImage(layout=layout_model)
    image = layout_image.create()
    image.show()
    image.save("imgs/example1.jpg")


if __name__ == '__main__':
    main()
