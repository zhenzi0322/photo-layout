from typing import Optional
from pydantic import BaseModel


class Canvas(BaseModel):
    width: Optional[int]
    height: Optional[int]
    color: Optional[str] = "white"
    is_del_extra: Optional[bool] = False


class LayoutModel(BaseModel):
    canvas: Optional[Canvas]  # 画布大小
    imagePath: Optional[str]  # 图片路径
    space: Optional[int] = 10  # 间距
    row: Optional[int]  # 行
    column: Optional[int]  # 列
