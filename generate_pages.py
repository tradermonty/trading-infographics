import os
import re

def read_template():
    with open('infographics/template.html', 'r', encoding='utf-8') as f:
        return f.read()

def read_content(content_file):
    with open(content_file, 'r', encoding='utf-8') as f:
        return f.read()

def extract_title(content):
    # 最初のh1タグからタイトルを抽出
    match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    if match:
        return match.group(1).strip()
    return "インフォグラフィック"

def generate_page(content_file):
    template = read_template()
    content = read_content(content_file)
    title = extract_title(content)
    
    # テンプレートのプレースホルダーを置換
    page = template.replace('{%TITLE%}', title)
    page = page.replace('{%CONTENT%}', content)
    
    # 出力ファイル名を生成
    output_file = os.path.basename(content_file)
    
    # ページを保存
    with open(f'infographics/{output_file}', 'w', encoding='utf-8') as f:
        f.write(page)
    
    print(f'Generated: {output_file}')

def main():
    # contentsディレクトリ内のすべてのHTMLファイルを処理
    contents_dir = 'infographics/contents'
    for file in os.listdir(contents_dir):
        if file.endswith('.html'):
            content_file = os.path.join(contents_dir, file)
            generate_page(content_file)

if __name__ == '__main__':
    main() 