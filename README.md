# hemAutomation
Automating simple tasks/operations not only saves a lot of our time but it may lead to accomplish many perplexing problems. Those pieces or snippets can be worthwhile when we automate these tasks into action. For those that are Python fans already, you know how friendly Python is for interacting with just about anything. From sending HTTP requests, interacting with APIs, to administering system operations. Even if you're not a fan of Python, these ideas can be summed.

**filesystem**

| Name | Short Description | Key Packages/Utilities |
| --- | --- | --- |
| [Automatic Filesystem Monitoring][file_monitoring] | Monitors filesystem looking for any changes (creation, change or deletion of a file or of a directory). `usage: filesystem_monitoring.py [-h] [--path PATH]` | `watchdog` |
| [Search for Large Files][large_files] | Walking through a folder tree and searching for large files or folders and printing the files with their absolute path with their size in MB. `usage: search_for_large_files.py [-h] [--path PATH] [-p PREVIEW] [-d DISPLAY] [-s {asc,dsc}]` | `functools, tabulate` |
| [Manage Files into Folders][manage_files] | Manages files and stores into their respective folders. `usage: manage_files_into_folders.py [-h] [--path PATH]`| `shutil` |
| [Check Downloadable][check_downloadable] | Check if provided URL is downloadable or not | `requests` |




[repo_root]: https://github.com/sangamsyabil/hemAutomation/
[file_monitoring]: https://github.com/sangamsyabil/hemAutomation/blob/main/filesystem/filesystem_monitoring.py
[check_downloadable]: https://github.com/sangamsyabil/hemAutomation/blob/main/filesystem/check_downloadable.py
[large_files]: https://github.com/sangamsyabil/hemAutomation/blob/main/filesystem/search_for_large_files.py
[manage_files]: https://github.com/sangamsyabil/hemAutomation/blob/main/filesystem/manage_files_into_folders.py