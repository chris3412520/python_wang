def convert_upper_to_lower(input_file, output_file):
    """
    将输入文件中的所有大写字母转换为小写，并将结果写入输出文件。

    参数：
    - input_file: str, 输入文件的路径（例如 'a.txt'）
    - output_file: str, 输出文件的路径（例如 'a_lowercase.txt'）
    """
    try:
        # 以读取模式打开输入文件，确保使用正确的编码（通常为utf-8）
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到。请确保文件路径正确。")
        return
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return

    # 将所有大写字母转换为小写
    lowercase_content = content.lower()

    try:
        # 以写入模式打开输出文件，使用相同的编码
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(lowercase_content)
        print(f"成功：已生成将大写字母转换为小写的文件 {output_file}")
    except Exception as e:
        print(f"写入文件时发生错误：{e}")

if __name__ == "__main__":
    input_filename = 'a_no_chinese.txt'             # 输入文件名
    output_filename = 'a_lowercase.txt'  # 输出文件名

    convert_upper_to_lower(input_filename, output_filename)