import json
import os
import shutil
import os.path as osp
from tqdm import tqdm

# before use the script, you should change the origin_video_dir and dest_video_dir variables
if __name__ == "__main__":
    origin_video_dir = os.getcwd()
    dest_video_dir = os.getcwd()
    emotion_list = ["neutral", "happy", "anger", "sadness", "contempt", "fear", "disgust", "surprise", "uncertain"]
    json_path = "celebvhq_info.json"
    with open(json_path) as f:
        data_dict = json.load(f)
    # create dir
    for emotion in emotion_list:
        emotion_dir = osp.join(dest_video_dir, emotion)
        os.makedirs(emotion_dir, exist_ok=True)

    for key, val in tqdm(data_dict['clips'].items()):
        emotion = val['attributes']['emotion']
        file_name = key + ".mp4"
        source_file = osp.join(origin_video_dir, file_name)
        if emotion['sep_flag'] is True:
            target_dir = osp.join(dest_video_dir, "uncertain", file_name)
        else:
            target_dir = osp.join(dest_video_dir, emotion["labels"], file_name)
        try:
            shutil.move(source_file, target_dir)
        except Exception as e:
            raise e

