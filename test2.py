# -*- coding: utf-8 -*-

import random
def generate_verfication_code_v2():
    
    code_list = []
    
    # 循环两次,每次生成3个字符
    for i in range(2):
        
        # 随机生成0-9的数字
        random_num = random.randint(0,9)
        
        # 随机生成65-90的数字，65-90是ASCII码对应的控制字符"A-Z"
        a = random.randint(65, 90)
        
        # 随机生成97-122的数字，91-122是ASCII码对应的控制字符"a-z"
        b = random.randint(97, 122)
        
        # 将a变量随机生成的的ASCII码转换为对应的控制字符
        random_uppercase_letter = chr(a)
        
        # 将b变量随机生成的的ASCII码转换为对应的控制字符
        random_lowercase_letter = chr(b)
        
        # 将整型转换成字符串并添加到列表中
        code_list.append(str(random_num))
        
        # 添加到列表中
        code_list.append(random_uppercase_letter)
        
        # 添加到列表中
        code_list.append(random_lowercase_letter)
        
    # 将列表连接起来成为字符串
    verification_code = ''.join(code_list)
    
    return verification_code    

code = generate_verfication_code_v2()

print code