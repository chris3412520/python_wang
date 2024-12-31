import re

def keep_only_letters(input_file, output_file):
    """
    从输入文件中仅保留字母字符，并将结果写入输出文件。

    参数：
    - input_file: str, 输入文件的路径（例如 'a.txt'）
    - output_file: str, 输出文件的路径（例如 'a_letters_only.txt'）
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

    # 定义匹配非字母字符的正则表达式
    # 这里使用 [^A-Za-z] 匹配所有非英文字母字符
    # 如果需要保留其他语言的字母，可以调整正则表达式
    non_letter_pattern = re.compile(r'[^A-Za-z]+')

    # 使用正则表达式替换非字母字符为空字符串
    letters_only_content = non_letter_pattern.sub('', content)

    try:
        # 以写入模式打开输出文件，使用相同的编码
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(letters_only_content)
        print(f"成功：已生成仅保留字母字符的文件 {output_file}")
    except Exception as e:
        print(f"写入文件时发生错误：{e}")

if __name__ == "__main__":
    input_filename = 'a_lowercase.txt'               # 输入文件名
    output_filename = 'a_letters_only.txt' # 输出文件名

    keep_only_letters(input_filename, output_filename)