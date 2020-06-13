
# mbox2eml

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

`-f, --file source_file.mbox`
The mbox file with your emails. Emails should start with `From<space>` and end with an empty line.

`-o, --output target_directory`
Directory you want the eml files to go. It will create a new directory in the target_directory with the name of the mbox file and a unix timestamp added to it.

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

# License

Do with it whatever you want.
