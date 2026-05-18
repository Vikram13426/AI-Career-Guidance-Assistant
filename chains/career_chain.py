from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

from utils.prompts import CAREER_PROMPT

load_dotenv()


# Gemini Flash Model
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0.7
)


# Prompt Template
prompt = PromptTemplate(
    input_variables=[
        'skills',
        'interests',
        'experience',
        'goals'
    ],
    template=CAREER_PROMPT
)


# Output Parser
parser = StrOutputParser()


# LCEL Chain
chain = prompt | llm | parser


def generate_career_guidance(
    skills,
    interests,
    experience,
    goals
):

    response = chain.invoke({
        'skills': skills,
        'interests': interests,
        'experience': experience,
        'goals': goals
    })

    return response