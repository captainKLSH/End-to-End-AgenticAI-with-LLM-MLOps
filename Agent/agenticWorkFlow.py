from utils.modelLoader import modelLoad
from promptLibrary.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools.waeatherInfo import WeatherInfoTool
from tools.placeSearch import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currencyConversion import CurrencyConverterTool



class graphBuilder():

    def __init__(self):
        pass


    def agentFunction(self):
        pass

    def buildGraph(self):
        pass


    def __call__(self, *args, **kwds):
        pass