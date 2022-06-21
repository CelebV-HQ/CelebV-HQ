# CelebV-HQ: A Large-Scale Video Facial Attributes Dataset
> Abstract: Large-scale datasets have played indispensable roles in the recent success of face generation/editing and significantly facilitated the advances of emerging research fields. However, the academic community still lacks a video dataset with diverse facial attribute annotations, which is crucial for the research on face-related videos. 
In this work, we propose a large-scale, high-quality, and diverse video dataset with rich facial attribute annotations, named the High-Quality Celebrity Video Dataset (CelebV-HQ). CelebV-HQ contains 35,666 video clips with the resolution of 512x512 at least, involving 15,653 identities. All clips are labeled manually with 83 facial attributes, covering appearance, action, and emotion.
We conduct a comprehensive analysis in terms of age, ethnicity, brightness stability, motion smoothness, head pose diversity, and data quality to demonstrate the diversity and temporal coherence of CelebV-HQ. Besides, its versatility and potential are validated on two representative tasks, i.e., unconditional video generation and video facial attribute editing.
Furthermore, we envision the future potential of CelebV-HQ, as well as the new opportunities and challenges it would bring to related research directions. 

Hao Zhu*, Wayne Wu*, Wentao Zhu, Liming Jiang, Siwei Tang, Li Zhang, Ziwei Liu, and Chen Change Loy (*Equal contribution)

## Download
### Usage:

Prepare the environment: 
```bash
pip install youtube_dl
pip install opencv-python
```

Run script: 
```bash
# you can change the download folder in the code 
python download_tools.py
``` 


### JSON File Structure:
JSON: 
```javascript
{
"mete_info": 
    {
        "appearance_mapping": ["Blurry", "Male", "Young", ...],  // appearance attributes
        "action_mapping": ["blow", "chew", "close_eyes", ...]    // action attributes
    },  

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
           
    },
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
