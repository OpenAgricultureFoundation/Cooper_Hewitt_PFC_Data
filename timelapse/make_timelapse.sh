#!/bin/bash
# Uncomment this to generate the image_urls list
# python3 pull_urls.py -i Camera-Top_URL.csv -o image_urls.txt

# Uncomment this to pull images
# wget -i image_urls.txt

ffmpeg -f image2 -r 15 -pattern_type glob -i '*.png' -threads 8 -vcodec libx264 -pix_fmt yuv420p timelapse.mp4
