import glob
import os.path
import re

directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + r'\testdata'

# 获取目录下的文件名
def get_file_dir(type):
    file_dir = [file for file in glob.glob(os.path.join(directory, 'preprints?*'+type)) if os.path.isfile(file)]
    return file_dir[0]


def replace_numbers(directory, type, replacement='', pattern=r'\d+'):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        new_path=' '
        new_name=' '
        if os.path.isfile(old_path):
            # 替换数字并保留扩展名
            name, ext = os.path.splitext(filename)
            if ext in type:
                new_name = re.sub(pattern, replacement, name) + ext
                new_path = os.path.join(directory, new_name)

            # 避免重名冲突
                if new_path != old_path:
                    counter = 1
                    while os.path.exists(new_path):
                        new_name = f"{re.sub(pattern, replacement, name)}_{counter}{ext}"
                        new_path = os.path.join(directory, new_name)
                        counter += 1

                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_name}")


if __name__ == "__main__":
    # target_dir = r"C:\target\directory"  # 替换为目标目录
    type =['.zip','.dox','.docx','.pdf']
    replace_numbers(directory,type,replacement="132331")  # 将数字替换为"NUM"
    test=get_file_dir('.docx')
    print(test)
