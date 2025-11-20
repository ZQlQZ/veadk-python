import asyncio

from veadk import Agent, Runner

agent = Agent(
    model_api_key="9459c0e3-0e94-4255-8c31-4ca6542ad157",
    name="hello_assistant",
    description="一个agent简单例子。",
    # 系统提示
    instruction="以赵本山的幽默风格响应用户的输入。",
    model_provider="volcengine",
    model_name="doubao-seed-1.6-250615",
    model_extra_config = {
    "thinking":{
         "type":"enabled" # enabled, disabled, auto
        }
    },
    )
runner = Runner(agent=agent)

response = asyncio.run(runner.run(messages="hi!"))
print(response)
