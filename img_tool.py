import os
from PIL import Image

def load_img(img_path):
    # Doc anh tu duong dan cho truoc va tra ve doi tuong anh
    try:
        img = Image.open(img_path)
        return img
    except Exception as e:
        print("Error Img from path")
        return None
    
def is_img_file(file_path):
    extentions = ('.jpg', '.png', '.jpeg', '.gif', '.bmp')
    return file_path.lower().endswith(extentions)

def get_img_list(folder_path):
    img_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and is_img_file(file_path):
            img = load_img(file_path)
            img_list.append(img)
    return img_list