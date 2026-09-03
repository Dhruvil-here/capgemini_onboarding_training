from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model

bug_failure_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an experienced QA Engineer.

Generate a professional defect report.

Include:

- Bug ID
- Title
- Module
- Environment
- Preconditions
- Steps to Reproduce
- Test Data
- Expected Result
- Actual Result
- Severity
- Priority
- Status
- Impact
- Notes

Write the report in a format suitable for JIRA or Azure DevOps.
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}

Observed Issue:

{defect}
"""
    )
])

bug_failure_report_chain = bug_failure_prompt | chat_model