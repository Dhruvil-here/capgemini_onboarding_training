from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model

test_case_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Software Test Engineer.

Generate detailed test cases from the given requirement and requirement analysis.

For every test case provide:

- Test Case ID
- Test Scenario
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Priority

Generate:

1. Positive Test Cases
2. Negative Test Cases
3. Boundary Value Test Cases
4. Validation Test Cases
5. Cart Test Cases
6. Coupon Test Cases
7. Payment Test Cases
8. Order Placement Test Cases

Do not invent unsupported functionality.
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}

Requirement Analysis:

{analysis}
"""
    )
])

test_case_chain = test_case_prompt | chat_model