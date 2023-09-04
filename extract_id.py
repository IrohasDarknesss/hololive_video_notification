import re

# 正規表現パターンを定義
pattern = r'https://www\.youtube\.com/channel/([a-zA-Z0-9_-]+)'

# ファイルを読み込む
with open('./text/talent_id.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# チャンネルIDを抽出
channel_ids = re.findall(pattern, content)

# チャンネルIDを新しいテキストファイルに保存
with open('./text/channel_ids.txt', 'w', encoding='utf-8') as f:
    for channel_id in channel_ids:
        f.write(channel_id + '\n')