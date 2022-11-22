
# mbox2eml

**This project is no longer maintained. I don't use this anymore by myself and don't have the time to maintain it any further. Feel free to fork and modify as you like.**

---

Python Script to create .eml files for every email in an mbox file.

**Use at your own risk. Please make a backup before you run it.**

I am not a Python developer by any means. This is just a script I put together for a need I had. Maybe you have to modify it to work with your files.

I made it to create an eml file for every email in a mbox-file you get from your GMail Account via [Google Takeout](https://takeout.google.com/).

# Requirements

- Python 2.7+
- Tested only on Mac OS X 10.14

# Usage / Options

```
python mbox2eml.py [-f | --file] source_file.mbox [-o | --output] target_directory
```

`-h, --help`
Show the options documentation. (Optional. No arguments.)

`-f, --file source_file.mbox`
The mbox file with your emails. Emails should start with `From<space>` and end with an empty line.

`-o, --output target_directory`
Directory you want the eml files to go. It will create a new directory in the target_directory with the name of the mbox file and a unix timestamp added to it.

`-e, --ext extension_string`
File extension of the created email files. (Optional. Default: eml)

`-t, --hastimestamp 1|0`
Should the created folder for the emails inside of --file have an unix-timestamp added? To prevent name collisions. (Optional. Default: 1)

`-s, --silent`
If set the script will start immediately without asking the user first. (Optional. No argument.)

# Output

There will be a folder created in the given `target_directory` which then includes the eml files. The folder structure will look like this:
```
<target_directory>/<mbox-filename> <unix-timestamp>/<eml-files>.eml
```

The outputted .eml files will have a filename created from the `From ` lines of the mbox file and will be like this:
```
YYYY-MM-DD HHMMSS <Truncated_SHA-1_Hash_of_the_whole_`From `_line>.eml
```

# Example

```bash
python mbox2eml.py --file ~/Desktop/Emails.mbox --output ~/Desktop/output
```

The output will be as follows:
```
~/Desktop/
    Emails.mbox
    output/
        Emails 1234567890/
            2020-02-28 143259 a4678714c5.eml
            2020-05-13 094512 7b60083427.eml
            …
```

# Duplicate Handling

If the directory where the .eml files should go already exists, the existing directory will be used.

If there is already an .eml file at the destination, the creation of this .eml file is skipped. After the processing is finished there is a summary of how many files have been skipped.

# License

MIT License

Copyright (c) 2020 Florian Rehder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
