def first_modified():
    # ファイルを読み込む
    with open('./text/talents.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # URLの共通部分を削除
    modified_lines = [line.replace('https://hololive.hololivepro.com/talents/', '').strip() for line in lines]
    # modified_lines2 = [line.replace('/', '').strip() for line in lines]

    # 変更をファイルに保存
    with open('./text/talents.txt', 'w', encoding='utf-8') as file:
        for line in modified_lines:
            file.write(line + '\n')

def second_modified():
    # ファイルを読み込む
    with open('./text/talents.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    modified_lines2 = [line.replace('/', '').strip() for line in lines]

    # 変更をファイルに保存
    with open('./text/talents.txt', 'w', encoding='utf-8') as file:
        for line in modified_lines2:
            file.write(line + '\n')

if __name__ == '__main__':
    first_modified()
    second_modified()