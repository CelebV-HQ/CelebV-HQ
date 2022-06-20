# Download tool for CelebV-HQ
## Usage:

prepare the tools: youtube-dl 

RUN: `python download_tools.py` 


## JSON DATA Structure:
JSON: 
```javascript
{"mete_info": {
"appearance_mapping": ["Blurry", "Male", "Young", ...], 
"action_mapping": ["blow", "chew", "close_eyes", ...]}, 

"clips": 
{
    "M2Ohb0FAaJU_1":  // clip 1 
    {
        "ytb_id": "M2Ohb0FAaJU",  
        "duration": {"start_sec": 81.62, "end_sec": 86.17}, 
        "bbox": {"top": 0.0, "bottom": 0.8815, "left": 0.1964, "right": 0.6922}, 
        "attributes": 
        {
            "appearance": [0, 0, 1, ...], 
            "action": [0, 0, 0, ...], 
            "emotion": {"sep_flag": false, "labels": "neutral"} // only one emotion int the clip 
         }, 
         "version": "v0.1"
           
    }
    "_0tf2n3rlJU_0":  // clip 2 
    {
        "ytb_id": "_0tf2n3rlJU", 
        "duration": {"start_sec": 52.72, "end_sec": 56.1}, 
        "bbox": {"top": 0.0, "bottom": 0.8407, "left": 0.5271, "right": 1.0}, 
        "attributes": 
        {
            "appearance": [0, 0, 1, ...], 
            "action": [0, 0, 0, ...], 
            "emotion": 
            {
                "sep_flag": true, "labels": [
                    {"emotion": "neutral", "start_sec": 0, "end_sec": 0.28000000000000114}, 
                    {"emotion": "happy", "start_sec": 1.2800000000000011, "end_sec": 3.280000000000001}]
            }
        }, 
        "version": "v0.1"
    }
    "..."
    "..."

}```
