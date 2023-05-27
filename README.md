# Introduction
I have recently discovered the miracles of using free AI tools to solve transcription tasks.
I use these for transcribing interview recordings.

When I learned about OpenAI's [whisper](https://github.com/openai/whisper), I was impressed by how accurately it can transcribe recordings.
However, a major drawback is that it does not do any diarization to distinguish between different speakers.
I then came across [whisperX](https://github.com/m-bain/whisperX), which uses PyAnnotate to diarization.
Great! 
However, it produces great srt files, which can be imported in subtitle editors (useful for fixing errors in the transcript), as well as in Atlas.ti if you import it alongside the audio.
However, I found it quite annoying to have a timestamp and speaker tag in every single sentence.

With a bit of help of ChatGPT I therefore created a python script (called parse_srt.py) that can be used to parse a srt file produced by whisperX into something that looks a lot more useful as an interview transcript to be imported into QDA software.

I might feel the need to make additional tools in the future. 
That is why I made this repository.

# Using parse_srt.py
parse_srt.py can be used on the command line.
Just pass the filename of the srt-file that you wish to parse as an argument to the python script, like this:
`python parse_srt.py myfile.srt`

If you want to put the result in a text file, just do this (I guess this only works on linux): `python parse_srt.py myfile.srt > myfile.txt`


