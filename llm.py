from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.gpt4all import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

local_path = (
    "../../../../Musa Computer/AppData/Local/nomic.ai/GPT4All/ggml-model-gpt4all-falcon-q4_0.bin"  # replace with your desired local file path
)

callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)


llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

data = llm_chain.run(question)

