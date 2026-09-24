"""ADK agent over PageIndex."""

from __future__ import annotations

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from settings import settings

from .tools import client, index_document

root_agent = LlmAgent(
    name="pageindex_agent",
    model=LiteLlm(model=settings.llm.model_name, **settings.llm.provider_args),
    description="Q&A over PDFs with PageIndex.",
    instruction=(
        client.agent_instructions()
        + "\n\nIf the user gives a local PDF path, call index_document first."
    ),
    tools=[index_document, *client.agent_tools()],  # type: ignore[arg-type]
)
