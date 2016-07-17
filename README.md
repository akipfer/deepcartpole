
# Cart-Pole Problem with Q-Learning

I am learning about how to apply TensorFlow to robotics. I am operating in the "copying the masters"-mode.

This experiment uses TensorFlow on the Cart-Pole problem.

This experiment is based on the results and code from "pong playing AI": https://github.com/DanielSlater/PyDataLondon2016


## Cart Pole implementation in PyGame

I found a cartpole simulation in PyGame here (lucky me):
http://www.cs.colostate.edu/~anderson/cs645/index.html/lib/exe/fetch.php?media=notes:cartpole.py

I just made it work with the lastest Box2D version (please use diff in case you need more details).


## Installing Box2D

I had some trouble installing the current version of Box2D on Ubuntu using virtualenv. This is what I ended up with:

```bash
$ . ./venv/bin/activate
$ sudo apt-get install build-essential python-dev swig python-pygame git
$ git clone https://github.com/pybox2d/pybox2d
$ cd pybox2d/
$ python setup.py build
$ python setup.py install
```



