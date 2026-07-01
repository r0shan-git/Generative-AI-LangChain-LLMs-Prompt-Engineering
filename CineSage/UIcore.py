from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import List, Optional

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-small-2506")


# Pydantic Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# Output Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.

{format_instructions}
""",
        ),
        ("human", "{paragraph}"),
    ]
)

# Streamlit UI
st.set_page_config(
    page_title="CineSage",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 CineSage")
st.subheader("AI-Powered Movie Information Extractor")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=200,
    placeholder="Paste a movie description here..."
)

if st.button("Extract Information"):

    if not paragraph.strip():
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Analyzing movie information..."):

            final_prompt = prompt.invoke(
                {
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions(),
                }
            )

            response = model.invoke(final_prompt)

            movie_data = parser.parse(response.content)

            st.success("Extraction Complete!")

            st.subheader("Movie Details")

            st.json(movie_data.model_dump())

            st.subheader("Summary")
            st.write(movie_data.summary)
