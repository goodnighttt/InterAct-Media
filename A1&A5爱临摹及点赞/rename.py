import os

# 获取文件夹中的所有文件名
folder_path = "./image/images"  # 替换为你的文件夹路径
file_names = os.listdir(folder_path)

# 处理文件名
for file_name in file_names:
    # 去掉前缀"S0_"
    if file_name.startswith("1_"):
        new_file_name = file_name.replace("1_", "", 1)
    else:
        new_file_name = file_name

    # 去掉开头的0
    if new_file_name.startswith("0"):
        new_file_name = new_file_name[1:]

    # 重命名文件
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)
