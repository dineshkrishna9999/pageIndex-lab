"""Local PageIndex client + index helper for the ADK agent."""

from __future__ import annotations

import json
import os

from pageindex import PageIndexClient

from settings import settings

client = PageIndexClient(index=settings.model_name, chat=settings.model_name)


def index_document(pdf_path: str) -> str:
    """Index a local PDF so browse_documents / get_page_content can use it."""
    if not os.path.isfile(pdf_path):
        return json.dumps({"error": f"File not found: {pdf_path}"})
    if not pdf_path.lower().endswith(".pdf"):
        return json.dumps({"error": "Only PDF files are supported"})

    try:
        result = client.submit_document(pdf_path)
    except Exception as exc:  # noqa: BLE001
        return json.dumps({"error": str(exc)})

    return json.dumps(
        {
            "success": True,
            "doc_id": result.get("doc_id"),
            "name": result.get("name"),
        }
    )
