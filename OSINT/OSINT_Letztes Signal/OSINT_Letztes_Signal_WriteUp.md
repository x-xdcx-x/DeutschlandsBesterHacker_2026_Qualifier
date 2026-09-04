# Letztes Signal

## Challenge description
```
Piep Piep Piep
```

## Available artifact
- Audio file: `signal.wav` 

## Solution
By playing the audio file, it quickly became clear that the recording contained some kind of code, more specifically a Morse code. After extracting the Morse code, the resulting string appeared to be `Base32`-encoded. Decoding it revealed a Tor address: `http://teftywlmggsmmfwb6qvvpokeati63l2lfdb3i2lcf4k6q2tmpuwv36ad.onion/`

When visiting the site using the Tor browser, it contained a video showing a man saying something. However, the actual message can be found behind him. A flag, `DBH{BLACKOUT}`, was written on a piece of paper!

## Flag
```
DBH{BLACKOUT}
```