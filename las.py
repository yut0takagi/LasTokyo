#lasデータを編集、解析するためのファイルです
import laspy
import pyarrow


def GetCoodinate(filepath):
    x_first = las.X[0]
    x_scale = header.x_scale
    x_offset = header.x_offset
    x_coordinate = (x_first * x_scale) + x_offset

    print(f"{x_first=}")
    print(f"{x_scale=}")
    print(f"{x_offset=}")
    print(f"{x_coordinate=}")
