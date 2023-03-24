This two scripts that allow me to easily convert `d["key"]` to `d.key` and vice versa in Pycharm.  
This section is written by me Olivier. The rest of the readme and the script were written by ChatGPT, I had to fix two bug in the code otherwise it was not working. This was originally intended as an exercice for me to test ChatGPT, but it ended with this pair of useful features that I wanted for a long time. Of course, you are only seeing here the finale state, and not the failed branch and experiments, so take the whole thing with a grain of salt, but it generated the instruction for Pycharm integration all by itself, and they work.

![Demo video](access_to_dict_demo.mp4)

Following by ChatGPT:
----
# dict_to_access.py

This Python script takes a Python code file and a selection of text within that file and replaces all dictionary accesses with attribute accesses within the selected text. The modified code is then written back to the file.

The script can be executed from the command line using the following arguments:

```
python dict_to_access.py <file_path> <start_line> <start_col> <end_line> <end_col>
```

- `<file_path>`: the path to the Python code file
- `<start_line>`: the line number where the selection starts
- `<start_col>`: the column number where the selection starts
- `<end_line>`: the line number where the selection ends
- `<end_col>`: the column number where the selection ends

This script was written by me, an AI language model called ChatGPT, based on the GPT-3.5 architecture. The user, Olivier, helped me write the initial version of the script and he corrected any bugs in it.

# access_to_dict.py

This Python script takes a Python code file and a selection of text within that file and replaces all attribute accesses with dictionary accesses within the selected text. The modified code is then written back to the file.

The script can be executed from the command line using the same arguments as the `dict_to_access.py` script:

```
python access_to_dict.py <file_path> <start_line> <start_col> <end_line> <end_col>
```

This script was also written by me, ChatGPT, with help from Olivier.

## Integrating the scripts in PyCharm as an external tool

To integrate the `dict_to_access.py` and `access_to_dict.py` scripts in PyCharm as an external tool, follow these steps:

1. Open PyCharm and go to `File > Settings`.
2. In the left-hand panel, click on `Tools > External Tools`.
3. Click the `+` button to add a new external tool.
4. Enter a name for the tool, such as "Convert dict access to attr access".
5. In the "Program" field, enter the path to your Python executable, such as `/usr/bin/python`.
6. In the "Parameters" field, enter the full path to the `dict_to_access.py` script, followed by the command line arguments you want to use. For example:

```
/path/to/dict_to_access.py $FilePath$ $SelectionStartLine$ $SelectionStartColumn$ $SelectionEndLine$ $SelectionEndColumn$
```

7. Check the "Open console" box to see the output of the script in the PyCharm console.
8. Click "OK" to save the tool.
9. Repeat these steps to create an external tool for the `access_to_dict.py` script, using the appropriate command line arguments.

Now you can run these scripts as external tools from within PyCharm, by right-clicking on a Python code file and selecting the appropriate tool from the "External Tools" submenu.


