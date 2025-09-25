# aiVideoSummarizer

`aiVideoSummarizer` is a local-first tool that takes a video link, extracts the transcript, and generates concise summaries using a local LLM. The pipeline is designed for privacy, reproducibility, and flexibility, making it useful for research, note-taking, or quickly understanding long-form content.

---

## Features

* **Transcript Extraction**: Fetches transcripts from supported video sources (YouTube, Vimeo).
* **Chunking**: Splits transcripts into manageable segments for processing without context loss.
* **Local LLM Integration**: Summarizes text using a local model via [Ollama](https://ollama.com/).
* **Customizable Output**: Summaries can be short abstracts, detailed notes, or structured outlines.
* **Privacy First**: No data is sent to external APIs unless configured by the user.

---

## Installation

### 1. Install Ollama

Download and install Ollama from [https://ollama.com/download](https://ollama.com/download).

### 2. Set Up Virtual Environment

```bash

python -m venv aiVideoSummarizerEnv
```

Windows:
```bash
source aiVideoSummarizerEnv/Scripts/activate  # Windows
```

macOS/Linux:
```bash
source aiVideoSummarizerEnv/bin/activate      # macOS/Linux
```

### 3. Clone Repository

```bash
git clone https://github.com/yourusername/aiVideoSummarizer.git
cd aiVideoSummarizer
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

* Add video URLs (YouTube or Vimeo) to `urls.txt`, one per line.
* By default, the script uses the `mistral` model. If your computer is slow, switch to `llama3.2` in `main.py`.
* Edit main.py to change the prompt, and configure the output of the LLM.
* Summaries, transcripts, and audio files are saved in the following folders:

  * `./assets/audios`
  * `./assets/transcripts`
  * `./assets/summaries`

---

## Example Output

**Input**: 45-minute technical lecture
**Output (short summary)**:

```
Prompt: 
Give me the main focus, what was covered, and all key takeaways from the lecture.

Output:
- Main focus: Basics of signal processing
- Covered: Fourier transforms, FIR vs IIR filters, noise reduction
- Key takeaway: Real-world filtering involves balancing precision vs efficiency
```

## License

Creative Commons Zero v1.0 Universal – free for personal use.
