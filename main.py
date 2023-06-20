#import files
from dotenv import load_dotenv
from langchain.llms import OpenAI



llm = OpenAI(APIKEY)
llm = OpenAI(temperature=0.5) #the temperature effects how random the responses will be between 0 and 1. The closer to 1 the more random the response