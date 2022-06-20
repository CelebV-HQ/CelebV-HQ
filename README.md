# Download tool for CelebV-HQ
## Usage:

prepare the tools: youtube-dl 

RUN: `python download_tools.py` 


## JSON DATA Structure:
JSON: 
```javascript
{"mete_info": {
"appearance_mapping": ["Blurry", "Male", "Young", ...],  // appearance attributes
"action_mapping": ["blow", "chew", "close_eyes", ...]},  // action attributes

"clips": 
{
    "M2Ohb0FAaJU_1":  // clip 1 
    {
        "ytb_id": "M2Ohb0FAaJU",                                   // youtube id
        "duration": {"start_sec": 81.62, "end_sec": 86.17},        // start and end times in the original video
        "bbox": {"top": 0.0, "bottom": 0.8815, "left": 0.1964, "right": 0.6922},  // bounding box
        "attributes":                                              // attributes information
        {
            "appearance": [0, 0, 1, ...],                          // same order as the "appearance_mapping"
            "action": [0, 0, 0, ...],                              // same order as the "action_mapping"
            "emotion": {"sep_flag": false, "labels": "neutral"}    // only one emotion in the clip 
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
                "sep_flag": true, "labels": [                      // multi-emotion in the clip
                    {"emotion": "neutral", "start_sec": 0, "end_sec": 0.28}, 
                    {"emotion": "happy", "start_sec": 1.28, "end_sec": 3.28}]
            }
        }, 
        "version": "v0.1" 
    }
    "..."
    "..."

}```
