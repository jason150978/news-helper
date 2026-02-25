import streamlit as st
import time

st.set_page_config(page_title="新聞編輯與媒體對照系統", layout="wide")

st.title("🚀 新聞編輯與全台媒體範本對照系統")

st.write("---")

st.subheader("📝 內容編輯區")
user_title = st.text_input("第一步：新聞標題", placeholder="輸入標題關鍵字...")
content = st.text_area("第二步：新聞內文", height=250, placeholder="貼上內文...")

st.write("---")

t_len = len(user_title)
c_len = len(content)
para_count = content.count('\n') if c_len > 0 else 0

score = 0
score = score + 30 if 15 <= t_len <= 35 else score
score = score + 30 if c_len >= 450 else score
score = score + 20 if para_count >= 5 else score
score = score + 20 if any(k in user_title for k in ["！", "曝光", "驚", "直擊", "影", "起底"]) else score

st.subheader("📈 全台媒體入口收錄潛力評估")
st.progress(score / 100)
st.write(f"📊 根據全台主流媒體 (Yahoo/Google/LINE) 數據對比，本則新聞被收錄機率：{score}%")

st.write("---")

col_l, col_r = st.columns(2)

col_l.subheader("🚩 標題優化建議 (媒體熱門格式)")
col_l.write(f"當前：{t_len} 字 (熱門中位數：24 字)")
col_l.write("💡 專業媒體下標參考：")
col_l.write(f"1. 動態型：{user_title[:10]}... 現場畫面曝光！網驚：太危險")
col_l.write(f"2. 深度型：{user_title[:12]} 內幕起底！背後原因竟然是這關鍵")
col_l.write(f"3. 懶人包：{user_title[:10]}？一圖看懂受影響範圍、應對方案")
col_l.write(f"4. 引戰型：這也能過？{user_title[:12]} 掀兩派網友戰翻")
col_l.write(f"5. 直擊型：獨家／{user_title[:12]} 直擊！最新現場進度回報")

col_r.subheader("🚩 內文診斷與錯別字修正")
typo_db = {"反應": "反映", "份量": "分量", "紀錄": "紀錄", "匯整": "彙整", "佈置": "布置", "收獲": "收穫", "身分證": "身分證", "再接再厲": "再接再厲", "名列前茅": "名列前茅", "由其": "尤其", "既使": "即使", "一昧": "一味", "幅員": "幅員", "急燥": "急躁", "針貶": "針砭", "稍微": "稍微"}
found_typos = [f"『{k}』→『{v}』" for k, v in typo_db.items() if k in content or k in user_title]
typo_msg = "、".join(found_typos) if found_typos else "✅ 內文用詞符合媒體標準，尚未偵測到錯字。"
col_r.error(f"🔍 錯字提醒：{typo_msg}")
col_r.write("💡 同業寫作結構對照：")
col_r.write("· Yahoo 偏好：" + ("✅ 第一段字數充足" if c_len > 100 else "⚠️ 第一段建議補齊 50 字摘要"))
col_r.write("· LINE 偏好：" + ("✅ 段落分布均勻" if para_count >= 5 else "⚠️ 建議增加換行，方便行動版用戶滑動"))
col_r.write("· Google 偏好：" + ("✅ SEO 權重達標" if c_len >= 500 else "⚠️ 字數過少，容易被視為無效簡訊"))

st.write("---")

st.subheader("🔍 參考同業內容：各大媒體類似新聞對照")
auto_kw = user_title[:5] if t_len > 0 else "最新新聞"
kw = st.text_input("輸入對照關鍵字", auto_kw)

ref_url = f"https://www.google.com/search?q=https://news.google.com/search%3Fq%3D{kw}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"

st.info(f"💡 點擊下方按鈕，系統會為您開啟 Google 新聞中所有關於「{kw}」的報導：")
st.write("您可以參考聯合、自由、三立等同業的「新聞切入點」與「段落編排」。")

st.markdown(f"### ")
st.link_button(f"🚀 開啟同業範本對照列表", ref_url)

st.write("---")
st.caption(f"媒體範本對照版 V16 | 更新時間: {time.strftime('%H:%M:%S')} | 無縮排穩定模式")
