import random
import streamlit as st

st.set_page_config(page_title="TOEFL iBT - Build a Sentence", page_icon="✏️")

st.title("✏️ TOEFL iBT: Build a Sentence Practice")
st.write(
    "Reorder the correct chunks to complete the response, and identify the trap chunk!"
)

# Question Bank (Zero API Cost)
questions = [
    {
        "speaker_a": "Do you know where the campus library is located?",
        "chunks": [
            "He asked me",
            "if I knew",
            "where",
            "the library was",
        ],
        "distractor": "was the library",
        "explanation": "In embedded questions, use normal statement word order (Subject + Verb: 'the library was'), not question order ('was the library').",
    },
    {
        "speaker_a": "Are you going to the biology review session tonight?",
        "chunks": [
            "I would go",
            "if I didn't have",
            "to work late",
            "at the lab",
        ],
        "distractor": "if I wouldn't have",
        "explanation": "In second conditional clauses, use the simple past after 'if' ('if I didn't have'), not 'would'.",
    },
    {
        "speaker_a": "Why was the professor unhappy with the final draft?",
        "chunks": [
            "The paper involved",
            "analyzing data",
            "collecting samples",
            "and writing reports",
        ],
        "distractor": "and to write reports",
        "explanation": "Maintain parallel structure when listing actions (gerunds: analyzing, collecting, and writing).",
    },
]

if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(questions)

q = st.session_state.current_q

st.subheader(f"Speaker A: '{q['speaker_a']}'")

# Shuffle chunks + distractor for display
if "shuffled_chunks" not in st.session_state:
    all_chunks = q["chunks"] + [q["distractor"]]
    random.shuffle(all_chunks)
    st.session_state.shuffled_chunks = all_chunks

st.write("**Available Chunks (including 1 Trap Chunk):**")
st.info(" | ".join([f"`[{c}]`" for c in st.session_state.shuffled_chunks]))

user_order = st.text_input("Type the correct sentence (excluding the trap):")
user_trap = st.text_input("Which chunk is the trap/distractor?")

if st.button("Check Answer"):
    correct_sentence = " ".join(q["chunks"])
    if (
        user_order.strip().lower() == correct_sentence.lower()
        and user_trap.strip().lower() == q["distractor"].lower()
    ):
        st.success("🎉 Excellent! You got both the sentence order and trap right.")
    else:
        st.error(f"**Correct Sentence:** {correct_sentence}")
        st.warning(f"**Trap Chunk:** `{q['distractor']}`")
    st.info(f"💡 **Grammar Rule:** {q['explanation']}")

if st.button("Next Question ➡️"):
    st.session_state.current_q = random.choice(questions)
    all_chunks = st.session_state.current_q["chunks"] + [
        st.session_state.current_q["distractor"]
    ]
    random.shuffle(all_chunks)
    st.session_state.shuffled_chunks = all_chunks
    st.rerun()
