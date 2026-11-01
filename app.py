import spaces
import gradio as gr
from main import app as fastapi_app

# ZeroGPU / CPU binding for Hugging Face free tier
@spaces.GPU
def predict(prompt: str = "") -> str:
    return "⚡ TwitchCutter API Server is Active and Running!"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Status Check", value="ping"),
    outputs=gr.Textbox(label="Response"),
    title="⚡ TwitchCutter API Server",
    description="Backend API for TwitchCutter Stream & VOD Clipper"
)

if __name__ == "__main__":
    res = demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        prevent_thread_lock=True,
        allowed_paths=["/tmp/twitchcutter", "/tmp"]
    )
    launched_app = res[0]
    launched_app.include_router(fastapi_app.router)
    demo.block_thread()

