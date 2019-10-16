# Make timelapse scripts
The python 3 script `pull_urls.py` will create a text file of just the URLs of images. This can be fed into `wget` to pull them down to the local machine. 

The `make_timelapse.sh` script has the commands to parse the camera URLs from the split data, and the calls to `wget` to pull the images, as well as the `ffmpeg` call to genearte the `timelapse.mp4`
