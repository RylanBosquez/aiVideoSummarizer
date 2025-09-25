import os

def chunkTranscript(transcripPath: str, chunkSize: int, overlap: int):
    
    if overlap >= chunkSize:
        raise ValueError("Overlap must be less than chunk size.")
    
    with open(transcripPath, "r", encoding="utf-8") as file:
        transcript = file.read()
        
    chunks = []
    start = 0
    textLength = len(transcript)
    
    while start < textLength:
        
        end = start + chunkSize
        chunk = transcript[start:end]
        chunks.append(chunk)
        
        start = end - overlap
        
    return chunks

    
if __name__ == "__main__":
    
    transcriptPath = "./assets/transcripts/Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)_transcript.txt"
    chunkSize = 1000
    overlap = 200
    
    chunks = chunkTranscript(transcriptPath, chunkSize, overlap)
    for chunk in chunks:
        print('\n' + chunk)
        
        