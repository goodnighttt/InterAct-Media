# 读取数据文件
file_path = '分组整合.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 整合相同编号的内容
result = {}
for line in lines:
    line = line.strip()
    if line:
        parts = line.split(',')
        if len(parts) == 2:
            code, content = parts
            if code in result:
                result[code].append(content)
            else:
                result[code] = [content]
        else:
            print(f"无法解析的数据行: {line}")

# 导出整合结果到新文件
output_file_path = '整合结果.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for code, contents in result.items():
        line = f"{code}: {', '.join(contents)}\n"
        output_file.write(line)

print("整合结果已导出到文件:", output_file_path)
