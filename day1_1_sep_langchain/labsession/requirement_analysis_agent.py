from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model

requirement_analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Business Analyst and QA Requirement Analyst.

Analyze the given software requirement and provide:

1. Functional Requirements
2. Non-Functional Requirements (if applicable)
3. Missing Requirements
4. Ambiguous Requirements
5. Business Rules
6. Required Validations
7. Edge Cases
8. Assumptions
9. Risks

Do not invent functionality not mentioned in the requirement.
Clearly separate each section.
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}
"""
    )
])

requirement_analysis_chain = requirement_analysis_prompt | chat_model