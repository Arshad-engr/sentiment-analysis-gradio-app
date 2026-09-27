from transformers import pipeline
import gradio as gr

classifier = pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = classifier(text)

    label = result[0]["label"]
    score = result[0]["score"]

    return f"{label} ({score:.2%})"

demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Textbox(label="Prediction"),
    title="Sentiment Analysis"
)

demo.launch()
