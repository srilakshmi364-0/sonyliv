import ffmpeg   
import subprocess

with open("tenali.csv", 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    for row in csv_reader:
        epno = row['Episode Number']
        epname = row['Episode Name']
        epurl = row['Video']

print("Starting...")
cmd = f'youtube-dl -f "bestvideo[height=720]+bestaudio" -o "{epno}. {epname}" worstvideo+worstaudio --geo-bypass-country IN {epurl}'
subprocess.call(cmd, shell=True)
