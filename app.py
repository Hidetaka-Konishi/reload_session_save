import streamlit as st
import streamlit.components.v1 as components

# Streamlitのページ設定
st.set_page_config(page_title="JavaScript Test")

# キー名を定義
key_name = 'user_input'

# ローカルストレージから値を読み込む
if 'load_once' not in st.session_state:
    components.html(f"""
        <script>
            window.onload = () => {{
                const savedValue = localStorage.getItem('{key_name}');
                if (savedValue) {{
                    window.parent.postMessage({{
                        type: 'streamlit:set_widget_value',
                        key: '{key_name}',
                        value: savedValue
                    }}, '*');
                }}
            }}
        </script>
    """, height=0)
    st.session_state.load_once = True

# ユーザーからの入力を取得
text = st.text_input("文字を入力", key=key_name)

# 入力された値をローカルストレージに保存
components.html(f"""
    <script>
        localStorage.setItem('{key_name}', '{text}');
    </script>
""", height=0)
