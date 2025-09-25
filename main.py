import os

from core.downloader import downloadAudio
from core.transcribeAudio import transcribeAudio
from core.transcribeAudio import transcribeAudio
from core.transcriptChunker import chunkTranscript
from core.summarizer import summarizeTrancsript
from core.getTitle import getTitle

if __name__ == "__main__":
    
    os.system("cls")
    
    chunkSize = 2000
    overlap = 100
    
    modelName = "mistral" # If conputer is slow, try "llama3.2"
    prompt = "Summarize the following message in 500 words or less:"
    
    with open("urls.txt", "r") as file:
        urls = file.read().splitlines()
        
    for url in urls:
        
        title = getTitle(url)
        
        print(f"\nProcessing {title}...")
        
        print("\n   Downloading audio...")
        downloadAudio(title, url, "./assets/audios")
        
        print("\n   Transcribing audio...")
        transcribeAudio(f"./assets/audios/{title}.mp3", "./assets/transcripts")
        
        print("\n   Chunking transcript...")
        chunks = chunkTranscript(f"./assets/transcripts/{title}_transcript.txt", chunkSize, overlap)
        
        print("\n   Summarizing transcript...")
        summary = summarizeTrancsript(chunks, prompt, model=modelName)
        
        with open(f'./assets/summaries/{title}.txt', "w", encoding="utf-8") as file:
            file.write(summary)
            
        print(f"\n      Summary saved to {os.path.join('./assets/summaries', f'{title}.txt')}")