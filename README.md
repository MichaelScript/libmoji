#libmoji
Currently a work in progress, some functionality is currently undocumented. Feel free to help out.
* Makes you hate variable character pixel width
* Provides a list of emojis and their unicode values.
* Randomly select emojis
* Create cool loading animations

### Installation
```bash
pip install libmoji
```
##Documentation
###random()
Returns a random emoji
```python
import libmoji
print(libmoji.random())
```
#####Positional Arguments: **None**
#####Keyword Arguments: **None**
###get_emoji_vals()
Returns a random emoji
```python
import libmoji
print(libmoji.get_emoji_vals())
```
#####Positional Arguments: **None**
#####Keyword Arguments: **None**
###load_moji()
Helps you distract how painstakingly slow your code is, with cool loading animations featuring emojis
```python
import libmoji
from time import sleep
# Displays randomly chosen emojis along with a loading "animation" for ten seconds.
libmoji.load_moji(sleep,args=[10],frames=["LOADING.","LOADING..","LOADING..."])
```
#####Positional Arguments:
* **func**
	- The function to run while the animation is playing.

#####Keyword Arguments:
* **args**
*(Default Value: [ ])*
	- Any arguments that the function takes
* **kwargs**
*(Default Value: { })*
	- Any keyword arguments that the function takes
* **frames**
*(Default Value: [ ])*
	- Text animation frames to be looped through
* **fixed_width**
*(Default Value: True)*
	- Pad animation frames to the same width
* **text_color**
*(Default Value: "green")*
	- Color of frame text (See termcolor for text options)
* **text_attrs**
*(Default Value: ["reverse","bold"])*
	- Frame text attributes (See termcolor for text options)
* **width**
*(Default Value: 10)*
	- How many emojis to display
* **delay**
*(Default Value: 0.1)*
	- Delay between frames in seconds.


