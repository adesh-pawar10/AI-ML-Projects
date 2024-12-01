import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('model.pkl', 'rb'))
