import streamlit as st

# Page setup with festive emoji icon
st.set_page_config(
    page_title="🎄 Riddlement Gridlock's Christmas Cipher Game 🎁",
    page_icon="🎅",
    layout="centered"
)

# Page header
st.title("🎄 Christmas Cipher Game 🎄")
st.write(
    "Ho ho ho! I am **Riddlement Gridlock**, your merry elf guide! 🧝‍♂️\n\n"
    "Solve my Christmas cipher riddles to earn a festive surprise! 🎁✨"
)

# Define rounds with festive flavor
rounds = [
    {"description": "Round 1 (Easy – Caesar shift +1) ❄️",
     "example": "If GIVV is TREE, then what is HMDL?",
     "answer": "SNOW"},
    {"description": "Round 2 (Easy-Medium – Caesar shift +3) 🎁",
     "example": "If JLIW is GIFT, then what is VWDU?",
     "answer": "STAR"},
    {"description": "Round 3 (Medium – Letter scramble / anagram) ⛄",
     "example": "If FMG is ELF, then what is KPX?",
     "answer": "JOY"},
    {"description": "Round 4 (Medium-Hard – Substitution cipher) 🔔",
     "example": "If HZMGZ is SANTA, then what is YFHHT?",
     "answer": "BELLS"},
    {"description": "Round 5 (Hard – Mixed: scramble + Caesar + substitution) 🎄",
     "example": "If OSFM is NOEL, then what is UDLXHWBYMX?",
     "answer": "MISTLETOE"}
]

# Initialize session state
if "current_round" not in st.session_state:
    st.session_state.current_round = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Function to check answer
def check_answer():
    current = st.session_state.current_round
    answer = rounds[current]["answer"]
    user_input = st.session_state.user_input.upper().strip()
    
    if user_input == answer:
        st.session_state.feedback = "🎉 Ho ho ho! Correct! Let's move to the next round... 🎅"
        st.session_state.current_round += 1
        st.session_state.user_input = ""
        if st.session_state.current_round >= len(rounds):
            st.session_state.game_over = True
            st.session_state.feedback = ""
    else:
        st.session_state.feedback = "❌ Oops! That's not right. Try again! 🎄"

# Game logic
if not st.session_state.game_over:
    current = st.session_state.current_round
    st.subheader(rounds[current]["description"])
    st.write(f"🎁 **Cipher:** {rounds[current]['example']}")
    
    # User input
    st.text_input("Your Festive Answer:", key="user_input", on_change=check_answer)
    
    # Feedback message
    if st.session_state.feedback:
        if "Correct" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
else:
    st.balloons()
    st.markdown(
        "## 🎅 Congratulations! You've solved all the Christmas riddles! 🎄\n"
        "✨ May your holidays be filled with joy, snow, and candy canes! 🍭"
    )
