import streamlit as st
import streamlit.components.v1 as components

# Streamlitのページ設定
st.set_page_config(page_title="JavaScript Test")

# JavaScriptコードを含むHTMLを定義
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Test</title>
</head>
<body>
    <script>
        // ローカルストレージにデータを保存
        localStorage.setItem('キー', '保存する値');
        var value = localStorage.getItem('キー');
        console.log(value);
    </script>
</body>
</html>
"""

# StreamlitアプリにHTMLコードを組み込む
components.html(html_code, height=100)
