from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Paper Summarization")
paper_input = st.selectbox(
    "Select a research paper:",
    [
        "Artificial Intelligence in Healthcare",
        "Bert: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ]
)
length_input = st.selectbox("Select the length of summary:", ["Short", "Medium", "Long"])
style_input = st.selectbox("Select the style of summary:", ["Technical", "Layman", "Analytical"])

template = PromptTemplate(
    template="""
Please summarize the following research paper in a {style} style with a {length} length:
{paper}
1. Mathematical Details
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive language where applicable.

2. Analogies
    - Use analogies to explain complex concepts in a more relatable way.
    - Provide examples that relate to everyday experiences or common knowledge.
If certain information is not present in the paper, please mention that it is not available.
""",
    input_variables=["paper", "style", "length"]
)

prompt = template.format(
    paper=paper_input,
    style=style_input,
    length=length_input
)

llm = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=1000)

if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        response = llm.invoke(prompt)
        st.subheader("Summary:")
        st.write(response.content)