# LLM Models Setup and Interaction

This repository provides detailed instructions for setting up and interacting with two different large language models (LLMs): Llama3 and Gemma:2B. 
The setup process includes downloading, installing, and running the models locally on your machine. Additionally, it demonstrates how to interact with these models using the `curl` command.

## Models Covered
1. Llama3
2. Gemma:2B

## Getting Started

### Requirements
- Windows or macOS
- curl (installed by default on macOS, can be installed on Windows)

### Setting Up Llama3

1. **Download Llama3**: Follow the download link for your system from the [Ollama Llama3 GitHub repository](https://github.com/Ollama/llama3) (https://ollama.com/download/OllamaSetup.exe).
2. **Install**: Follow the installation instructions specific to your operating system.
3. **Start the Model**:
   - On Windows:
     ```sh
     ollama run llama3
     ```
   - On macOS:
     ```sh
     /Applications/Ollama.app/Contents/MacOS/Ollama run llama3
     ```

4. **Verify the Setup**: Use the following `curl` command in Command Prompt to verify that the model is running correctly:
   ```sh
   curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"messages\": [{\"role\": \"user\", \"content\": \"Why is the sky blue?\"}], \"stream\": false}"


### Setting Up Gemma:2b

1. **Assuming you have already downlaoded and installed OllamaSetup.exe file**, run the gemma:2b model
3. **Start the Model**:
   - On Windows:
     ```sh
     ollama run gemma:2b
     ```
   - On macOS:
     ```sh
     /Applications/Ollama.app/Contents/MacOS/Ollama run gemma:2b
     ```

4. **Verify the Setup**: Use the following `curl` command in Command Prompt to verify that the model is running correctly:
   ```sh
   curl -X POST http://localhost:11435/api/chat -H "Content-Type: application/json" -d "{\"model\": \"gemma:2b\", \"messages\": [{\"role\": \"user\", \"content\": \"What is the capital of France?\"}],\"stream\":false}"


### Interacting with Local LLM via Chatbot using StreamLit
- Download the llm_chatbot.py file in a folder

#### Set Up a Virtual Environment
- Windows
```sh
python -m venv venv
venv\Scripts\activate
```

- macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

#### Install Requirements
```sh
pip install -r requirements.txt
```

### Start the LLM Model
Llama3 Model
Open Command Prompt or Terminal.
Start the Llama3 model server:
```sh
ollama serve --port 11434
```

#### Run the Chatbot Application
Open a new Command Prompt or Terminal and run:
```sh
streamlit run llm_chatbot.py
```

#### Interact with the Chatbot
Open your web browser and go to http://localhost:8501. You can now interact with the chatbot.


### License
This project is licensed under the MIT License.

## Author
Dristi Dani
