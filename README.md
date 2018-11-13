### [Where to put argparse?](https://www.reddit.com/r/learnpython/comments/3do2wr/where_to_put_argparse/)

> I generally go with #3, though with one difference - I tend to pass through the actual args, rather than have argparse get the values itself. Ie:
>
> ```python
> def parse_args(args):
>     parser = argparse.ArgumentParser(description='This.')
>     # ...
>     return parser.parse_args(args)  # Rather than leaving args out, and letting argparse grab them from sys.argv itself
>
> def main(args)
>     args = parse_args(args)
>
> if __name__ == '__main__':
>     import sys
>     main(sys.argv[1:])
> ```
> The reason is that it lets you use the program as a module, and call the whole thing from within python, which can be useful for things like testing. Ie. you can just > do:
> ```python
> import myprog
> myprog.main(["--option1", "opt1val", "required_arg"])
> ```
> and have it do the same as if you'd called it with those options from the commandline. It also feels cleaner to me that the only time this global state is accessed is > at the very top level.
>

- Our example
  - `train.py` is main script
  - `other.py` import `run` from `train.py` and manually pass args rather than `sys.argv`


credits:
- [Brian](https://www.reddit.com/r/learnpython/comments/3do2wr/where_to_put_argparse/ct7n98v)
- [keras-retinanet/keras_retinanet/bin/train.py](https://github.com/fizyr/keras-retinanet/blob/615688a0c13edcfb4aa994e52e6c12c5be3167a0/keras_retinanet/bin/train.py#L326-L493)
