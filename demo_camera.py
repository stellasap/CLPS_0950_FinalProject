import gradio as gr
import numpy as np

def flip(im):
    im[:,:,1] = im[:,:,1]*0
    im[:,:,2] = im[:,:,2]*0
    return im

demo = gr.Interface(
    flip, 
    gr.Image(source="webcam", streaming=True), 
    "image",
    live=True
)
demo.launch()