import os

from dotenv import load_dotenv

from langchain_core.tools import Tool
from langchain.agents import create_agent

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from tools.document_tool import (
    search_client_documents
)

from tools.meeting_tool import (
    get_meeting_notes
)

from memory_store import (
    retrieve_memory,
    save_memory
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    ),
    temperature=0
)

tools = [

    Tool(
        name="Document_Search",
        func=search_client_documents,
        description="""
        Search company/client documents.
        """
    ),

    Tool(
        name="Meeting_Notes",
        func=get_meeting_notes,
        description="""
        Retrieve previous meeting notes.
        """
    ),

    Tool(
        name="Memory_Retrieval",
        func=retrieve_memory,
        description="""
        Retrieve relevant long-term memories.
        """
    ),

    Tool(
        name="Memory_Save",
        func=save_memory,
        description="""
        Store important information
        into long-term memory.
        """
    )
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are an intelligent enterprise assistant.

Available tools:

1. Document_Search
2. Meeting_Notes
3. Memory_Retrieval
4. Memory_Save

Rules:
- Use Document_Search for company knowledge.
- Use Meeting_Notes for meeting discussions.
- Use Memory_Retrieval when user refers to past information.
- Use Memory_Save when important information should be remembered.
"""
)