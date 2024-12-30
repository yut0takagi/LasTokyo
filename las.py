#lasデータを編集、解析するためのファイルです
import laspy
import matplotlib.pyplot as plt
import pyarrow as pa
import pyarrow.parquet as pq

class LasTokyo:
    def __init__(self,filepath):
        self.filepath = filepath
        self.las = laspy.read(self.filepath)
        self.header = self.las.header
        self.version_major = self.las.header.version.major
        self.version_minor = self.las.header.version.minor
    def getVersion(self):
        version = f"{self.version_major}.{self.version_minor}"
        return version
    def las_array(self):
        X = self.las.X
        Y = self.las.Y
        Z = self.las.Z
        return [X,Y,Z]
    def GetCoordinates():
        X_coordinate = (self.las.X * self.header.x_offset)+self.header.x_offset
        Y_coordinate = (self.las.Y * self.header.y_offset)+self.header.y_offset
        Z_coordinate = (self.las.Z * self.header.z_offset)+self.header.z_offset
        return [X_coordinate,Y_coordinate,Z_coordinate]
    def getPlot(self):
        A = self.getCoordinates()
        fig = plt.figure(figsize = (10, 10))
        ax= fig.add_subplot(111, projection='3d')
        ax.scatter(A["x"],A["y"],A["z"], s = 1, c = "blue")
        plt.show()