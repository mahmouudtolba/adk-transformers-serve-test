## Models
you need to have a folder named "model/safetensors"
eg. 
https://huggingface.co/Qwen/Qwen3-0.6B/tree/main




## start the server
```bash
transformers serve
```
it will run on port 8080 


## talk the model through out the server
```bash
python main.py
```
## run the agent
```bash
cd 1-basic_agent
adk web
```