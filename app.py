from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import streamlit as st

# データベース設定
DATABASE_URL = "sqlite:///users.db"
Base = declarative_base()

# ユーザーモデル
class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password = Column(String)
    login_attempts = Column(Integer, default=0)
    lockout_time = Column(DateTime, default=datetime.fromtimestamp(0))

# データベースエンジンの初期化
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# ユーザー認証関数
def authenticate_user(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False

# ログイン処理関数
def process_login(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        # 新しいユーザーの作成（デフォルトのlockout_timeを設定）
        user = User(username=username, password=password, lockout_time=datetime.fromtimestamp(0))
        session.add(user)
        session.commit()

    # ロックアウトチェック
    if user.lockout_time and user.lockout_time > datetime.now():
        st.error("アカウントは一時的にロックされています。")
        session.close()
        return

    # 認証チェック
    if authenticate_user(username, password):
        st.success("ログイン成功！")
        user.login_attempts = 0
    else:
        user.login_attempts += 1
        st.error("ログイン失敗。")
        # ログイン試行回数に基づいてロックアウト
        if user.login_attempts >= 3:
            user.lockout_time = datetime.now() + timedelta(minutes=1)

    session.commit()
    session.close()

# Streamlit UI
def main():
    st.title("ログインシステム")

    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        process_login(username, password)
        st.write("こんにちは、世界")


if __name__ == "__main__":
    main()
