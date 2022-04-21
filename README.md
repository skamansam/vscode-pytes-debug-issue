# Sample Repo for demonstrating the issue in https://github.com/microsoft/vscode-python/issues/18970
Code for demonstrating how debugging pytest in vscode renders vscode unusable

# Reproduction
1. Add the python extension to VSCode and open this repo
1. Open `test_lorem.py`
1. Open the Testing panel and then debug the tests
1. You can play around with the `number_lines_output` variable at the top to determine how much output will slow down your editor.