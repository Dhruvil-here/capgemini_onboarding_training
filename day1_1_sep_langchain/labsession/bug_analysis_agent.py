from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model

bug_analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a Senior QA Engineer.

Analyze the reported defect and provide:

1. Defect Summary
2. Expected Behavior
3. Actual Behavior
4. Requirement Violated
5. Business Impact
6. Severity
7. Priority
8. Root Cause Possibilities
9. Recommended Fix
10. Regression Areas

Base the analysis strictly on the requirement.
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}

Defect Report:

{bug_report}
"""
    )
])

bug_analysis_chain = bug_analysis_prompt | chat_model