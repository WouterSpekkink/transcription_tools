import re
import argparse

def reformat_srt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    result = ""
    last_speaker = ""
    speech_line = ""
    current_timestamp_start = ""
    current_timestamp_end = ""
    last_timestamp_start = ""
    last_timestamp_end = ""

    for line in lines:
        # Save timestamp lines
        timestamp_match = re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line)
        if timestamp_match:
            last_timestamp_start = current_timestamp_start
            last_timestamp_end = current_timestamp_end
            current_timestamp_start = line.split(' --> ')[0]  # save the start timestamp
            current_timestamp_end = line.split(' --> ')[1]
            continue

        speaker_match = re.match(r'\[(SPEAKER_\d+)\]:', line)
        if speaker_match:
            current_speaker = speaker_match.group(1)
            if current_speaker != last_speaker:
                # New speaker, add previous speech line before their speech
                if result:
                    result += f' - {last_timestamp_end})]: ' + speech_line + "\n\n"
                result += f'[{current_speaker} ({current_timestamp_start}'
                last_speaker = current_speaker
                speech_line = ""  # clear the speech line
            # Same speaker, just continue their speech
            speech_line += line.replace(f'[{current_speaker}]:', '').strip() + ' '
        # add the rest lines
        elif line.isdigit():  # skip the srt sequence number
            continue
        else:
            speech_line += line.strip() # assuming lines from same speaker, add space before concatenating

    # add the last speech line to the result
    result += f' - {current_timestamp_end})]: ' + speech_line

    # print or return the result
    print(result)

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Name of the file to process")

# Parse command-line arguments
args = parser.parse_args()

# Call the function with the file name provided as a command-line argument
reformat_srt(args.filename)
