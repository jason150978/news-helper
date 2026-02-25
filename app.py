import streamlit as st

st.set_page_config(page_title="News SEO Professional", layout="wide")

st.title("🚀 全平台新聞優化與 AI 編輯助手")

st.write("---")

user_title = st.text_input("第一步：編輯新聞標題")
content = st.text_area("第二步：編輯新聞內文", height=250)

st.write("---")

has_title = len(user_title) > 0
has_content = len(content) > 0

hot_words = ["獨家", "快訊", "直擊", "曝光", "內幕", "真相", "懶人包", "攻略", "原因", "震撼", "影／", "圖／", "驚人", "必看", "首度", "證實", "首發", "最新"]
found_hot_words = [word for word in hot_words if word in user_title]

typo_db = {"反應": "反映", "份量": "分量", "紀錄": "紀錄", "匯整": "彙整", "佈置": "布置", "收獲": "收穫", "洗練": "洗鍊", "藉由": "藉由", "遊戰": "遊戲", "到底": "到底", "再見": "再見", "名片": "名片", "當紅": "當紅", "報到": "報到", "身分": "身分", "部分": "部分", "計畫": "計畫", "身分證": "身分證", "一窩風": "一窩蜂", "名列前矛": "名列前茅", "再接再厲": "再接再厲", "破天荒": "破天荒", "不徑而走": "不脛而走", "震撼彈": "震撼彈", "寒喧": "寒暄", "湊合": "湊合"}
detected_typos = [f"『{k}』→『{v}』" for k, v in typo_db.items() if k in content or k in user_title]

score = 0
score += (2 if has_title else 0)
score += (2 if has_content else 0)
score += (4 if len(found_hot_words) > 0 else 0)
score += (2 if "！" in user_title or "？" in user_title or "：" in user_title else 0)

st.subheader("📊 全平台抓取潛力評分")
st.progress(score / 10)
st.header(f"{score} / 10 分")

st.write("---")

st.subheader("✍️ 內容細節修正 (新聞媒體常見錯字檢查)")
st.write(f"🚩 偵測到疑似錯別字： {', '.join(detected_typos)}" if detected_typos else "✅ 尚未偵測到常見錯別字。")

st.write("---")

st.subheader("🎯 針對各大平台的實質建議")

st.info("🌐 Google News (SEO 權重)\n1. 首段黃金律：5W1H 必須在 100 字內交代，Google 才能產生精選摘要。\n2. 標題去空話：移除『不可思議』、『真的太強』，改放『具體人名/事由』。")

st.success("🟢 LINE TODAY (點擊權重)\n1. 符號運用：『！』放在標題最後能提升 15% 點擊，使用『／』能增加視覺節奏感。\n2. 圖說優化：LINE 的讀者喜歡看圖，建議每 200 字插入一張配圖提示。")

st.warning("🟣 Yahoo 新聞 / 聚合平台\n1. 數字化下法：『這 3 招』、『1 分鐘讀懂』能增加轉載率。\n2. 事實查核標籤：標題若含『證實』、『真相』能增加平台信賴度。")

st.write("---")

st.subheader("🔥 流量標題公式建議")
st.code(f"最新／{user_title}！原因內幕曝光網全看傻")
st.code(f"【{user_title}】懶人包：3大重點、影響分析一次看")
st.code(f"獨家直擊／{user_title}？現場最新狀況曝光")
