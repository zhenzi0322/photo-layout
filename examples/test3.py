from photo_layout.layout import Canvas, LayoutModel
from photo_layout.image import LayoutImage


def main():
    canvas = Canvas(width=2000, height=800, color="pink", is_del_extra=True)
    layout_model = LayoutModel(canvas=canvas, imagePath="test.jpg", space=10)
    layout_image = LayoutImage(layout=layout_model)
    image = layout_image.create()
    # image.show()
    image.save("imgs/example3.jpg")


if __name__ == '__main__':
    main()
