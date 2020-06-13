
import argparse
import os
import time
import calendar
import hashlib

#
# Get arguments
#
parser = argparse.ArgumentParser(description='Read MBOX file and create EML file from every email in it.')
parser.add_argument("--file", "-f", type=str, required=True, help='Input .mbox file.')
parser.add_argument("--output", "-o", type=str, required=True, help='Output directory, where the .eml files should go.')
parser.add_argument("--ext", "-e", type=str, required=False, default='eml', help='File extension of the created email files. (Optional. Default: eml)')
parser.add_argument("--hastimestamp", "-t", type=int, required=False, default=1, help='Should the created folder for the emails inside of --file have an unix-timestamp added? To prevent name collisions. (Optional. Default: 1)')
args = parser.parse_args()

output_file_ext = 'eml' if args.ext is None else args.ext
# print ("output_file_ext: %s") % output_file_ext

has_output_folder_timestamp = True if args.hastimestamp is 1 else False
# print ("has_output_folder_timestamp: %s") % has_output_folder_timestamp

#
# Create output folder
#
folder_suffix = " {}".format(int(time.time())) if has_output_folder_timestamp == True else ""
folder_name = os.path.basename(args.file).replace(".mbox", folder_suffix)
# print ("folder_name: %s") % folder_name

output_dir = os.path.join(args.output, folder_name)
# print ("output_dir: %s") % output_dir

try:
    os.mkdir(output_dir)
except OSError:
    print ("ERR Creation of the directory '%s' failed" % output_dir)

#
# Create mapping of month-abbr -> month-numbers
#
month_abbr_to_int = {name: num for num, name in enumerate(calendar.month_abbr) if num}

#
# Loop lines of given file
#
blank_lines_count = 2
file_count = 0

with open(args.file, "r") as mbox_file:
    for line in mbox_file:
        line_stripped = line.strip()
        line_parts = line_stripped.split(' ')

        #
        # New file starts at 'From ' string
        #
        if blank_lines_count >= 1 and line_stripped.startswith('From '):
            # NOTE: The with in 'with open() as file:' handles closing (?)
            # if 'new_file' in locals():
            #     new_file.close()

            #
            # Create file name
            #
            msg_year = line_parts[7]
            month_int = month_abbr_to_int[line_parts[3]]
            msg_month = "0{}".format(month_int) if month_int < 10 else "{}".format(month_int)
            msg_day = line_parts[4]
            msg_time = line_parts[5].replace(':', '')
            msg_hash = hashlib.sha1(line_stripped.encode("UTF-8")).hexdigest()

            file_name = "{year}-{month}-{day} {time} {unique}.{ext}".format(year = msg_year, month = msg_month, day = msg_day, time = msg_time, unique = msg_hash[:10], ext = output_file_ext)
            # print ("file_name: %s") % file_name

            file_output = os.path.join(output_dir, file_name)
            # print ("file_output: %s") % file_output

            #
            # Create file
            #
            new_file = open(file_output, "a")
            file_count += 1

            #
            #  Write line to file
            #
            new_file.write("%s" % line)

        else:
            #
            # Open file
            #
            new_file = open(file_output, "a")

            #
            # Write line to file
            #
            new_file.write("%s" % line)

        #
        # Count blank lines to locate new file starts
        #
        if line_stripped == '':
            blank_lines_count += 1
        else:
            blank_lines_count = 0

print ("Saved %d files." % file_count)
