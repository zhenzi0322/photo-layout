
# photo-layout
根据图像进行排版。比如排成二行三列的布局。


## 示例一
```python
from photo_layout.layout import Canvas, LayoutModel
from photo_layout.image import LayoutImage

def main():
    canvas = Canvas(color="pink")
    layout_model = LayoutModel(canvas=canvas, imagePath="test.jpg", row=3, column=3, space=10)
    layout_image = LayoutImage(layout=layout_model)
    image = layout_image.create()
    image.show()

if __name__ == '__main__':
    main()
```
效果图如下：

<img src="examples/imgs/example1.jpg" title="示例一" width="50%">

当然你也可以调用`image.save("imgs/example1.jpg")`来保存到本地。

## 示例二
```python
from photo_layout.layout import Canvas, LayoutModel
from photo_layout.image import LayoutImage

def main():
    canvas = Canvas(width=2000, height=800, color="pink")
    layout_model = LayoutModel(canvas=canvas, imagePath="test.jpg", space=10)
    layout_image = LayoutImage(layout=layout_model)
    image = layout_image.create()
    image.show()

if __name__ == '__main__':
    main()
```
效果图如下：

<img src="examples/imgs/example2.jpg" title="示例二" width="50%">