import h5py
import numpy as np

file_path = 'part_00000_of_04320.hdf5'  # 替换为你的文件路径

# 打开 HDF5 文件
with h5py.File(file_path, 'r') as hdf:
    # 定义一个函数来获取文件结构
    def get_structure(name, obj):
        obj_type = 'group' if isinstance(obj, h5py.Group) else 'dataset'
        obj_shape = obj.shape if isinstance(obj, h5py.Dataset) else None
        obj_dtype = obj.dtype if isinstance(obj, h5py.Dataset) else None
        print(f"Name: {name}, Type: {obj_type}, Shape: {obj_shape}, Dtype: {obj_dtype}")

    # 遍历文件结构
    hdf.visititems(get_structure)

    # 读取名为 'data' 的数据集
    dataset_name = 'next_sentence_labels'  # 替换为实际的数据集名称
    data = hdf[dataset_name]
    
    # 打印数据集的形状和数据类型
    print(f"Dataset '{dataset_name}': Shape = {data.shape}, Dtype = {data.dtype}")
    
    # 查看前10条数据
    sample_data = data[:10]  # 可以调整切片查看不同范围的数据
    print("Sample Data:\n", sample_data)
