import cv2
import os
import numpy as np
import json

def download(video_id, video_folder, proxy=None):
    if proxy is not None:
        proxy_cmd = "--proxy {}".format(proxy)
    else:
        proxy_cmd = ""
    video_path = os.path.join(video_folder, video_id + ".mp4")
    if not os.path.exists(video_path):
        down_video = " ".join([
            "youtube-dl", 
             proxy_cmd,
            '-f', "'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'", 
            '--skip-unavailable-fragments',
            '--merge-output-format', 'mp4',
            "https://www.youtube.com/watch?v=" + video_id, "--output",
            video_path, "--external-downloader", "aria2c",
            "--external-downloader-args", '"-x 16 -k 1M"'
        ])
        print(down_video)
        os.system(down_video)

    return video_path


def process_ffmpeg(path, save_path, out_vid_name, box, time):
    """
    box: top, bottom, left, right, normalized to 0~1
    time: begin_sec, end_sec
    """

    def secs_to_timestr(secs):
        hrs = secs // (60 * 60)
        min = secs // 60
        sec = secs % 60
        end = (secs - int(secs)) * 100
        return "{:02d}:{:02d}:{:02d}.{:02d}".format(int(hrs), int(min),
                                                    int(sec), int(end))

    def expand(box, ratio):
        top, bottom = max(box[0] - ratio, 0), min(box[1] + ratio, 1)
        left, right = max(box[2] - ratio, 0), min(box[3] + ratio, 1)

        return top, bottom, left, right

    def to_square(box):
        top, bottom, leftx, right = box
        h = bottom - top
        w = right - leftx
        c = min(h, w) // 2
        c_h = (top + bottom) / 2
        c_w = (leftx + right) / 2

        top, bottom = c_h - c, c_h + c
        leftx, right = c_w - c, c_w + c
        return top, bottom, leftx, right

    def denorm(box, height, width):
        top, bottom, left, right = \
                round(box[0] * height), \
                round(box[1] * height), \
                round(box[2] * width), \
                round(box[3] * width)

        return top, bottom, left, right

    out_name = os.path.join(save_path, out_vid_name)

    cap = cv2.VideoCapture(path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    top, bottom, left, right = to_square(
        denorm(expand(box, 0.02), height, width))
    start_sec, end_sec = time

    cmd = f"ffmpeg -i {path} -vf crop=w={right-left}:h={bottom-top}:x={left}:y={top} -ss {secs_to_timestr(start_sec)} -to {secs_to_timestr(end_sec)} -loglevel error {out_name}"
    os.system(cmd)
    return out_name

def load_data(file_path):
    with open(file_path) as f:
        data_dict = json.load(f)

    for key,val in data_dict['clips'].items():
        save_name = key+".mp4"
        ytb_id = val['ytb_id']
        time = val['duration']['start_sec'],val['duration']['end_sec']

        print(ytb_id)
        bbox = [val['bbox']['top'], val['bbox']['bottom'], val['bbox']['left'], val['bbox']['right']]
        yield ytb_id, save_name, time, bbox


if __name__ == '__main__':
    file_path = 'celebvhq_35666.json'
    raw_root = './video/raw/'
    processed_root = './video/processed/'

    proxy = "http://172.16.1.135:3128/"

    os.makedirs(raw_root, exist_ok=True)
    os.makedirs(processed_root, exist_ok=True)

    for vid_id, out_vid_name, time, box in load_data(file_path):
        raw_vid_path = download(vid_id, raw_root, proxy)
        process_ffmpeg(raw_vid_path, processed_root, out_vid_name, box, time)
