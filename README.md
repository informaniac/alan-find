# Alan Find - Read missing Collectibles from save files
Alan Wake has 324 Collectibles:
* 106 Manuscript Pages
* 100 Coffee Thermoses
* 12 Can Pyramids
* 30 Chests
* 11 Radio Shows
* 14 TV Shows
* 25 Signs
* 10 Alarm Clocks
* 6 Cardboard Standees
* 10 Night Springs Video Games

Except for the manuscript pages, the statistics only tell you how many you have already found, but not **which**
collectibles you are missing or at least in which chapter they are.

Many fellow gamers have tried multiple times to make a playthrough with a Collectibles guide and are still
missing that one Coffee Thermos.

This little script shows you the internal IDs of Collectibles (except Manuscript pages) that you are missing.
You can then check their location in a collectibles guide. Note that the internal ID might be different from the number
in the Guides. More on this down below in the Section *Observations* and in the `mapping.md` file. Happy hunting!

## Usage
Find your Alan Wake `config` file and use its full path as Parameter in this Python Script.
The Script will print out which Collectibles you are missing.

e.g. if you have Alan Wake on Steam and Steam is installed on C:
```
python alan_find.py "C:\Program Files (x86)\Steam\userdata\<userid>\108710\remote\config"
```
Note: `<userid>` is a placeholder for a User-ID. 108710 is the Application-ID for Alan Wake on Steam. The `remote`
Folder might only be used if the save game is synced with the Steam-Cloud. For the Drive Letter, it is important that
you use the drive that Steam was installed to, not the Steam Library Alan Wake was installed to.

## How does it work?
Of course the game keeps track of the collectibles, but it does that "in secret". If you open the file _config_ in a
text editor, you will see strings like _RADIOSHOWS_. Opening the file in a hex editor reveals some more information
After the string of the collectible category follows a byte in which the game counts how many collectibles of this
category you have already found, followed by a list of the collectibles you have found in order. After the list there
is another byte which I have not figured out what it represents (I thought it might be the Number of the last one you
found, but that did not seem to be correct). The entries are then separated by the Bytes `00 00 00`.

e.g. if the hex editor shows the bytes
```
01 03 05 06
```
it would mean that you missed the second and fourth collectible of this category (if it had 6 collectibles)

## Observations
Note that the ID shown by this script is the internal ID of the collectible. It might not correspond to the one you
will find in the collectible guide. But it might guide you to the right one. Most of the time, considering a guide and
playing the episode that the Collectible should be in was enough to somehow find it.

As I was just missing around 20 Collectibles at the time of writing this code, I can not tell how many IDs are not in
order. However, someone could use this codebase to create a mapping from internal IDs to their Guide counterparts
(as most guides that I found list the collectibles in order that you will encounter them).

I have started to create a mapping from internal ID to sequence numbers in the `mapping.md` file in this repository.

Here are some other observations I made regarding the IDs:
#### Coffee Thermos Values
In my config File there was Coffee Thermos with the value of 101 present. The script also showed one more Thermos
missing than the game. It turned out that Thermos 90 is unobtainable.

#### TV Show Values
In my config File the TV values ended with decimals 172, 4, 0, 0 before the additional Byte and the Delimiter. If I had
not found TV Show 4, this script would have told me that I did. Because of this I decided to print the IDs of the found
Collectibles, too. In the case of the TV shows this is noticeable as the other found IDs are in order.

## Why no manuscript pages?
I would have added them, but it would have meant more work for something that the game mostly provides to you by itself.

When you take a look into the config file, you will see that the manuscript pages are not mentioned.
But they are actually there. Just more hidden than the other stuff.

The Manuscript page entries are just before the CANPYRAMIDS string, but twice. It could be that one of those lists
keeps track of the pages that have been read. For some reason, these Lists seem to start at `00`, but the other Lists
start at `01`.

To actually find them in any config file, I would have to know exactly how to find the hunk containing the information
by a pattern. As I have already found all Manuscript pages, and I only can find 100% save files on the internet, I
cannot be sure if the portion before this hunk might be different in other config files.

Also, regarding the Nightmare pages I am not sure if the number in that list corresponds well to the n-th collectible
in the game.

# Contribute
Feel free to contribute to this repository.

If you want to help add more mappings to the `mapping.md` while you complete your game, take additional notes of your
missing IDs. You can rerun the script after every found Collectible and deduct the ID of the Collectible you just found,
as it should now be missing from your missing collectible list. Then add the information to the table. You can also
add the information that the Collectible ID and sequence number are equal.

These are the Collectible guides I used when compiling the table:
* https://steamcommunity.com/sharedfiles/filedetails/?id=2754374785
* https://www.xboxachievements.com/forum/topic/205346-alan-wake-color-coded-collectibles-guide/
* https://platget.com/guides/alan-wake-episode-1-collectibles-guide/ (other episodes under Additional Guides in the
left hand menu)

Also, a more user-friendly approach to this script would be nice. I am not too familiar with GUI programming, it would
have just wasted more time. For me, this approach was good enough, but less tech-savvy users might benefit from a GUI
with a file-picker.

If you have fun in trying to understand the other information in the config file, feel free to open an issue to discuss
your findings, or ideas.
