import os
import whisper


def transcribeAudio(audioPath: str, outputPath: str):
    
    os.makedirs(outputPath, exist_ok=True)
    
    model = whisper.load_model("base")
    result = model.transcribe(audioPath)
    
    with open(os.path.join(outputPath, f"{os.path.splitext(os.path.basename(audioPath))[0]}_transcript.txt"), "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcript saved to {os.path.join(outputPath, 'transcript.txt')}")
    
    
if __name__ == "__main__":
    
    audioPath = "./assets/audio/Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp3"
    outputPath = "./assets/transcripts"
    
    transcribeAudio(audioPath, outputPath)