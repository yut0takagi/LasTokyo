# LAS@tokyo
東京都新宿区🗼におけるLas点群データを用いた解析を行いました。

# ポイント座標化
Las データには、整数値int32しか持っていないため、座標として利用できるようにします。
```Python
GetCoodinate(filepath)
```
