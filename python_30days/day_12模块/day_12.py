import random
import string
# def random_user_id (id_len) :
#     posible = string.digits + string.ascii_letters
#     use_id =''
#     for i in range(0,id_len) :
#         use_id += posible[randint(0,len(posible)-1)]
#     return use_id
# print(random_user_id(6))
def list_of_hexa_colors (n : int =1)->list:
    colours =[]
    hex_chars = '0123456789abcdef'
    for _ in range(n) :
        color = '#'+''.join(random.choice(hex_chars) for _ in range(6))
    colours.append(color)
    return colours
def list_of_rgb_colors(n :int =1)->list:
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append((r, g, b))
    return colors

def generate_colors(n: int, color_type: str) -> list:
    """
    根据 color_type 生成 n 个十六进制或 RGB 颜色。
    - color_type: 'hex' 或 'rgb'
    """
    if color_type.lower() == "hex":
        return list_of_hexa_colors(n)
    elif color_type.lower() == "rgb":
        return list_of_rgb_colors(n)
    else:
        raise ValueError("color_type 必须为 'hex' 或 'rgb'")
def shuffle_list (list :list)->list :
    return random.shuffle(list)
def  random_num ():
    return random.sample(range(0,10),k=7)
print(random_num())