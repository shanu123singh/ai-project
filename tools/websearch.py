import streamlit as st
import os
from tavily import TavilyClient

TAVILY_API_KEY = st.secrets.get("TAVILY_API_KEY", os.getenv("TAVILY_API_KEY"))

client = TavilyClient(api_key=TAVILY_API_KEY)