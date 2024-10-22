# Majority

Convert media files and turn 'em like it's from a 2000s YouTube Poop!

Usually, you'd need a program such as Sony Vegas or Audacity to achieve this,
but with this silly program written in Python and with most of the heavy lifting done
by FFmpeg, you can convert any video/audio to "G Major" in a matter of seconds!

## What is "G Major"?

"G Major" is fad stemming from the YouTube Poop genre, this effect is
usually achieved by duplicating audio channels and offsetting its
pitch, causing it to sound dissonant and demonic; accompanied by
applying an invert effect on the video.

[See video examples from Know Your Meme](https://knowyourmeme.com/memes/in-g-major/videos)

## Development

Prerequisites:

- FFmpeg
- Python 3.10+ or higher

### Installing FFmpeg

For Windows, the easiest way to install FFmpeg is through `winget`:

```console
winget install -e --id Gyan.FFmpeg
```

For macOS, use Homebrew to install FFmpeg in your terminal:

```console
brew install ffmpeg
```

Likewise, you can install FFmpeg directly from their [Download page](https://ffmpeg.org/download.html).

### Setup

Once cloned, install project dependencies with:

```console
pip install -r requirements.txt
```

## Why is there no web version?

While there's a convienience when hosted this project as a web app, it's not worth
setting up the infrastructure, not to mention storing the temporary media files
uploaded by a user.

And God knows what any files are uploaded to a storage bucket,
be it confidential or whatnot. So, it'd be a whole lot easier to run it as a
native cross-platform app instead, even without an internet connection!
