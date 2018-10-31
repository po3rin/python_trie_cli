# tire

A Trie in computer science is a tree structure that allows you to do things such as very quick lookup of words within the english language. Typically if you were to write a word processor that did spell checks against words in a document, you would implement a trie and perform a very quick lookup to check whether or not the words in your word document are indeed valid words. This repository is trie example CLI searching "python" string.

## Quick Start

```bash
$ python3 setup.py develop
$ pytrie python pip pyenv
python
pip
pyenv
{'p': {'y': {'t': {'h': {'o': {'n': {'*': '*'}}}}, 'e': {'n': {'v': {'*': '*'}}}}, 'i': {'p': {'*': '*'}}}}
True
```
