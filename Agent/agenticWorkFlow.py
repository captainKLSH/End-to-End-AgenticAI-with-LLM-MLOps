from utils.modelLoader import modelLoad
from promptLibrary.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools.waeatherInfo import WeatherInfoTool
from tools.placeSearch import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currencyConversion import CurrencyConverterTool



class graphBuilder():

    def __init__(self,model_provider: str = "groq"):
        self.model_loader = modelLoad(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
        
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()
        
        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_converter_tool_list])
        
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        self.graph = None
        
        self.system_prompt = SYSTEM_PROMPT


    def agentFunction(self):
        """Main agent function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}

    def buildGraph(self):
        graphBuild=StateGraph(MessagesState)
        graphBuild.add_node("agent", self.agent_function)
        graphBuild.add_node("tools", ToolNode(tools=self.tools))
        graphBuild.add_edge(START,"agent")
        graphBuild.add_conditional_edges("agent",tools_condition)
        graphBuild.add_edge("tools","agent")
        graphBuild.add_edge("agent",END)
        self.graph = graphBuild.compile()
        return self.graph
        


    def __call__(self):
        return self.buildGraph()