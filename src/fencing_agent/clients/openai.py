from openai import AsyncOpenAI

from fencing_agent.core.config import settings

client = AsyncOpenAI(api_key=settings.openai_api_key)

async def get_chat_response(messages: list[dict]) -> str:
    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=messages
    )
    return response.choices[0].message.content
