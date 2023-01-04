# CelebV-HQ: A Large-Scale Video Facial Attributes Dataset (ECCV 2022)
<img src="./assets/teaser.png" width="96%" height="96%">
 

**CelebV-HQ: A Large-Scale Video Facial Attributes Dataset**<br>
[Hao Zhu](https://www.zhuhaozh.xyz)\*, 
[Wayne Wu](https://wywu.github.io/)\*, 
[Wentao Zhu](https://wentao.live), 
[Liming Jiang](https://liming-jiang.com/),
[Siwei Tang](mailto:tangsiwei@sensetime.com),
[Li Zhang](mailto:zhangli2@sensetime.com),
[Ziwei Liu](https://liuziwei7.github.io/), 
and [Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/)<br>
In ECCV 2022. <small>(*Equal contribution)</small><br>
**[Demo Video](https://www.youtube.com/watch?v=Y0uxlUW4sW0)** | **[Project Page](https://celebv-hq.github.io/)** | **[Paper](https://arxiv.org/abs/2207.12393)** | **[Annotations](https://github.com/CelebV-HQ/CelebV-HQ/blob/main/celebvhq_info.json)**

> Abstract: Large-scale datasets have played indispensable roles in the recent success of face generation/editing and significantly facilitated the advances of emerging research fields. However, the academic community still lacks a video dataset with diverse facial attribute annotations, which is crucial for the research on face-related videos. 
In this work, we propose a large-scale, high-quality, and diverse video dataset with rich facial attribute annotations, named the High-Quality Celebrity Video Dataset (CelebV-HQ). CelebV-HQ contains 35,666 video clips with the resolution of 512x512 at least, involving 15,653 identities. All clips are labeled manually with 83 facial attributes, covering appearance, action, and emotion.
We conduct a comprehensive analysis in terms of age, ethnicity, brightness stability, motion smoothness, head pose diversity, and data quality to demonstrate the diversity and temporal coherence of CelebV-HQ. Besides, its versatility and potential are validated on two representative tasks, i.e., unconditional video generation and video facial attribute editing.
Furthermore, we envision the future potential of CelebV-HQ, as well as the new opportunities and challenges it would bring to related research directions. 


## Updates
- [08/08/2022] Data annotations are released. Please check it in file 'celebvhq_info.json'.
- [26/07/2022] The paper is released on ArXiv.
- [25/07/2022] The download and processing tools for the dataset is released. Use them to construct your CelebV-HQ! :sparkles:
- [21/6/2022] The codebase and project page are created.

## TODO
- [x] Data download and processing tools.
- [x] Data annotations.
- [ ] Inference code of unconditional video generation
- [ ] Pretrained models of unconditional video generation





## Statistics
https://user-images.githubusercontent.com/10545746/179714392-4289e67c-884f-4a45-aa1d-b01b2ae6ee3f.mp4

The distributions of each attribute. CelebV-HQ has a diverse distribution on each attribute category. Overall, CelebV-HQ contains diverse facial attributes and natural distributions, bringing new opportunities and challenges to the community.

<img src="./assets/statistic.png" width="96%" height="96%">


## Agreement
- The CelebV-HQ dataset is available for non-commercial research purposes only.
- All videos of the CelebV-HQ dataset are obtained from the Internet which are not property of our institutions. Our institutions are not responsible for the content nor the meaning of these videos.
- You agree not to reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purposes, any portion of the videos and any portion of derived data.
- You agree not to further copy, publish or distribute any portion of the CelebV-HQ dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset.

## Download


### TL;DR:

This **[issue](https://github.com/CelebV-HQ/CelebV-HQ/issues/8)** is helpful.


### Usage:


Prepare the environment: 
```bash
pip install youtube_dl
pip install opencv-python
```

Run script: 
```bash
# you can change the download folder in the code 
python download_and_process.py
``` 


### JSON File Structure:
```javascript
{
"meta_info": 
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
        "attributes":                                              // attributes information (TBD)
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

}
```
## Baselines
### Unconditional Video Generation
To train other baselines, we used their original implementations in our paper:
- [VideoGPT](https://github.com/wilson1yan/VideoGPT)
- [MoCoGAN-HD](https://github.com/snap-research/MoCoGAN-HD)
- [DIGAN](https://github.com/sihyun-yu/digan)
- [StyleGAN-V](https://github.com/universome/stylegan-v)

### Facial Attribute Editing
- [StarGAN-v2](https://github.com/clovaai/stargan-v2)
- [MUNIT](https://github.com/NVlabs/MUNIT)


## Related Work
* (Tech. Report 2023) **CelebV-Text: A Large-Scale Facial Text-Video Dataset**, Jianhui Yu et al. [[Paper](https://arxiv.org/pdf/0000.00000.pdf)], [[Project Page](https://celebv-text.github.io/)], [[Dataset](https://github.com/CelebV-Text/CelebV-Text)]
* (ECCV 2022) **StyleGAN-Human: A Data-Centric Odyssey of Human Generation**, Jianglin Fu et al. [[Paper](https://arxiv.org/pdf/2204.11823.pdf)], [[Project Page](https://stylegan-human.github.io/)], [[Dataset](https://github.com/stylegan-human/StyleGAN-Human)]

## Citation
If you find this work useful for your research, please consider citing our paper:

```bibtex
@inproceedings{zhu2022celebvhq,
  title={{CelebV-HQ}: A Large-Scale Video Facial Attributes Dataset},
  author={Zhu, Hao and Wu, Wayne and Zhu, Wentao and Jiang, Liming and Tang, Siwei and Zhang, Li and Liu, Ziwei and Loy, Chen Change},
  booktitle={ECCV},
  year={2022}
}
```

## Acknowledgement
We sincerely thank Zongcai Sun for his help with source data preparation and the download tool development. This work is partly supported by Shanghai AI Laboratory and SenseTime Research. It is also supported by NTU NAP, MOE AcRF Tier 1 (2021-T1-001-088), and under the RIE2020 Industry Alignment Fund – Industry Collaboration Projects (IAF-ICP) Funding Initiative, as well as cash and in-kind contribution from the industry partner(s).


