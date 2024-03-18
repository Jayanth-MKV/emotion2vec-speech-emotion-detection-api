from fastapi import FastAPI, File, UploadFile
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import numpy as np

app = FastAPI()

mapper = ["angry", "disgust", "fear", "happy",
          "neutral", "other", "sad", "surprised", "unknown"]

inference_pipeline = pipeline(
    task=Tasks.emotion_recognition,
    model="iic/emotion2vec_base_finetuned", model_revision="v2.0.4")


@app.post("/emotion_recognition")
async def emotion_recognition(audio_file: UploadFile = File(...)):
    audio_bytes = await audio_file.read()
    rec_result = inference_pipeline(
        audio_bytes, output_dir="./outputs", granularity="utterance", extract_embedding=False)
    max_emotion_score = np.argmax(rec_result[0]["scores"])
    return {
        "emotion": mapper[max_emotion_score],
        "confidence":rec_result[0]["scores"][max_emotion_score]
    }
