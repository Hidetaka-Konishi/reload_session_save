import streamlit as st
import streamlit.components.v1 as components

# Streamlitのページ設定
st.set_page_config(page_title="JavaScript Test")

# ユーザーからの入力を取得
text = st.text_input("文字を入力")

# JavaScriptコードを含むHTMLを定義
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Test</title>
</head>
<body>
    <script>
        // ローカルストレージにデータを保存
        localStorage.setItem('キー', '{text}');
        var value = localStorage.getItem('キー');
        console.log(value);
    </script>
</body>
</html>
"""

# StreamlitアプリにHTMLコードを組み込む
components.html(html_code, height=100)
