import os
import subprocess


def summarizeChunk(chunk, model="mistral"):
    
    try:
        
        results = subprocess.run(
            ['ollama', 'run', model],
            input=chunk.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return results.stdout.decode('utf-8').strip()
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return ""
    

def summarizeTrancsript(chunks, prompt, model="mistral"):
    
    partialSummaries = []
    
    for i, chunk in enumerate(chunks):
        
        print(f"      Processing chunk {i+1} of {len(chunks)}...")
        summary = summarizeChunk(chunk, model)
        partialSummaries.append(summary)
        
    combinedText = "\n".join(partialSummaries)
    
    finalPrompt = f'{prompt}\nUse these summarized chunks to generate a cohesive summary:\n\n{combinedText}'
    
    print("      Generating final summary...")
    return summarizeChunk(finalPrompt, model)


if __name__ == "__main__":
    
    from transcriptChunker import chunkTranscript
    
    transcriptPath = "./assets/transcripts/Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)_transcript.txt"
    chunkSize = 1000
    overlap = 200
    
    chunks = chunkTranscript(transcriptPath, chunkSize, overlap)

    model = "mistral"
    prompt = "Summarize the following message in 500 words or less:"
    
    summary = summarizeTrancsript(chunks, model)
    print(summary)