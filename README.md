# lab: sorcery

In this lab you will do **true sorcery**.

<img src=img/magic.jpg width=300px align=right />

> **NOTE:**
> The English word "sorcery" derives from the Latin word [sortilegium](https://en.wiktionary.org/wiki/sortilegium) = sort + legere (Latin for to read),
> and so a sorcerer is literally someone who "reads sorted words".
> Sorting words allowed Medieval sorcerers to lookup information quickly
> (via binary search-like algorithms),
> which was a skill that other people thought was "magical".
>
> In English, we shifted the sound from t -> c because "sorcery" is easier to say than "sortery".
> But the etymological connection is more obvious in other Romance languages:
>
> | Language | Word for Sorcery |
> |---|---|
> | Spanish | [sortilegio](https://en.wiktionary.org/wiki/sortilegio) |
> | Italian | [sortilegio](https://en.wiktionary.org/wiki/sortilegio#Italian) |
> | Portuguese | [sortilégio](https://en.wiktionary.org/wiki/sortil%C3%A9gio) |
> | French | [sortilège](https://en.wiktionary.org/wiki/sortil%C3%A8ge) |
> | Catalan | [sortilegi](https://en.wiktionary.org/wiki/sortilegi) |
> | Romanian | [sortilegiu](https://en.wiktionary.org/wiki/sortilegiu) |
> | Galician | [sortilexio](https://en.wiktionary.org/wiki/sortilexio) |
> | Occitan | [sortilègi](https://en.wiktionary.org/wiki/sortil%C3%A8gi) |
> | Latin | [sortilegium](https://en.wiktionary.org/wiki/sortilegium) |

In this lab, you will **sort some words**.

You will:
1. measure much faster the built-in `sorted` function is than the functions you implemented on the last homework assignment.
1. learn about how to use git submodules to connect multiple git repos together.

You will need a partner for portions of this lab.
(And recall that you must do partner work either in class or the QCL.)

<img src=img/begins.jpg width=300px />

## Tasks

**Task 1: initialize the repo**

Do not clone this repository.
Instead:

1. Create a new empty repo.
    Ensure that the name of your repo is different than the name of your partner's repo (so that you can fork it later).

1. Copy the contents of this repo to your new repo with the following commands
    ```
    $ git clone https://github.com/mikeizbicki/lab-sorting-runtimes
    $ cd lab-sorting-runtimes
    $ git remote rm origin
    $ git remote add origin <URL>
    $ git push origin master
    ```
    where `<URL>` is the url to your newly created repo.

    > **NOTE:**
    > At this point you should ensure you understand what the `git remote` commands are doing fully.
    > I will stop giving these commands to you explicitly in the future.

**Task 2: setup the submodule**

Run the `runtimes.py` file.
You should get a `ModuleNotFoundError` that looks something like
```
$ python3 runtimes.py
Traceback (most recent call last):
  File "runtimes.py", line 9, in <module>
    from sorting.sorting import merge_sorted, quick_sorted
ModuleNotFoundError: No module named 'sorting'
```
> **NOTE:**
> In the code block above, I put both the command and the entire output of the command.
> Before the code block, I put a short summary of my steps using English intermixed with inline-code.
> When reporting error messages, it is standard to have a short English language summary and a full output of the error message in a code block.
> (Even if the output is hundreds of lines long, people will still include the full output, since all of those lines provide important information.)
> If you report your errors in this same way (e.g. on github issues/stackoverflow), you will be more likely to get good help from people.

The problem is that the `runtimes.py` file is trying to load the functions that you wrote in the sorting homework,
but it can't find those files.
The most obvious way to get access to those files is to clone your sorting homework into the repository.
BUT DON'T DO THIS!
It is never a good idea to clone one git repository inside another repository directly.
Instead, we will use something called a [git submodule](https://git-scm.com/docs/gitsubmodules) which will allow the two git repositories to "talk" to each other when needed.

<!--
> **NOTE:**
> Git has a semi-official tutorial website at <https://git-scm.com>.
> It has a (very long) tutorial on [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) that discusses all of their features, and much more than you'll need to know for this class.
-->

You can initialize a git submodule by running the command:
```
$ git submodule add <URL>
```
where `<URL>` is the url to your sorting homework.

If this command works successfully, then the command
```
$ ls -a
```
should have a new `sorting` directory in its output and a file `.gitmodules`.
If you run
```
$ ls sorting
```
then you should see all of the contents of your sorting repo.
Running the command 
```
$ python3 runtimes.py
```
should now generate no errors.
If you run
```
$ git status
```
you should see that the `sorting` repo and the `.gitmodules` file have has been added into the staging area.
You should commit theses changes and push them to github now.

If you visit the github website for your lab repo,
you should see that the `sorting` folder is now visible in the repo,
and it will have a symbol next to it that looks like `@ f43eacf` where the hash number after the `@` is the hash of the commit of the sorting repo and will be different.
Clicking on the folder should take you to the url for your sorting repo and away from this repo.
There will be no indication on your sorting repo that it is a git submodule in another repo.

**Task 3: runtimes of sorting algorithms on random lists**

Run the command
```
$ python3 runtimes.py --max_x=5
```
This will use the `timeit` module on 5 different lists of increasing size to measure the runtimes of the built-in `sort` function (which uses timsort) versus the sorting functions that you implemented in your last homework.
The output of this command, however, is currently not nicely formatted.
At the end of the file is a line labeled `FIXME 1`.
Follow the instructions so that the `runtimes.py` file generates output in markdown table format.

> **NOTE:**
> It is very common to write python code that generates code in another programming language, especially markdown or html.

After you've completed the FIXME, run the following command
```
$ python3 runtimes.py --max_x=22
```
and copy/paste the resulting table into this README file below this line.
| n | timsort | merge_sorted | quick_sorted |
|---:|---:|---:|---:|
| 2**0 | 2.100e-06 | 2.032e-06 | 1.412e-06 |
| 2**1 | 1.508e-06 | 6.253e-06 | 4.182e-06 |
| 2**2 | 1.103e-06 | 7.756e-06 | 4.919e-06 |
| 2**3 | 1.323e-06 | 1.191e-05 | 7.410e-06 |
| 2**4 | 1.821e-06 | 2.225e-05 | 1.315e-05 |
| 2**5 | 2.590e-06 | 4.483e-05 | 2.788e-05 |
| 2**6 | 5.590e-06 | 9.656e-05 | 6.283e-05 |
| 2**7 | 9.685e-06 | 2.085e-04 | 1.362e-04 |
| 2**8 | 2.094e-05 | 4.747e-04 | 3.037e-04 |
| 2**9 | 4.227e-05 | 9.361e-04 | 6.478e-04 |
| 2**10 | 1.008e-04 | 2.090e-03 | 1.433e-03 |
| 2**11 | 1.971e-04 | 4.325e-03 | 2.782e-03 |
| 2**12 | 4.285e-04 | 9.758e-03 | 5.921e-03 |
| 2**13 | 8.670e-04 | 1.969e-02 | 1.360e-02 |
| 2**14 | 1.877e-03 | 4.339e-02 | 2.887e-02 |
| 2**15 | 4.488e-03 | 9.062e-02 | 5.779e-02 |
| 2**16 | 9.178e-03 | 2.015e-01 | 1.315e-01 |
| 2**17 | 2.034e-02 | 4.159e-01 | 2.636e-01 |
| 2**18 | 4.355e-02 | 9.045e-01 | 6.010e-01 |
| 2**19 | 1.004e-01 | 1.980e+00 | 1.266e+00 |
| 2**20 | 2.358e-01 | 4.089e+00 | 2.855e+00 |
| 2**21 | 5.505e-01 | 9.158e+00 | 6.612e+00 |
| 2**22 | 1.218e+00 | 1.970e+01 | 1.609e+01 |

<!-- add the table here -->

You should observe that python's built-in sort function is 10-100x faster than yours.
All functions have the same wort-case asymptotic complexity (i.e. $\Theta(n \log n)$ ),
but python's built-in sorting function uses lots of optimization tricks to achieve this extra speedup.
Native python code is not very good at performing these types of optimizations,
and so the built-in function is written in the C programming language.
(You can find the [source code of the built-in function on github](https://github.com/python/cpython/blob/c1b1f51cd1632f0b77dacd43092fb44ed5e053a9/Python/bltinmodule.c#L2356)).
Functions that must be very fast are generally written in C instead of Python.

One of the differences between a *computer science* major and a *data science* major is that the CS major focuses on how to *write* these fast functions,
and the DS major focuses on how to *use* these fast functions to accomplish interesting tasks.
Writing fast C code is much harder than writing python,
and requires a deep understanding of computer architecture.

<img src=img/python-c.png width=300px />

<!--
For fun, compare the runtimes of your sorting algorithms to your partner's to see who has the fastest implementation.
-->

Push your changes to github and verify that the table is being displayed correctly.

**Task 4: cloning**

Fork your partner's repo and clone your partner's repo to the lambda server.
In this forked repo, re-run the command
```
$ python3 runtimes.py --max_x=22
```
You should get a `ModuleNotFoundError` again.

The problem is that when you clone a repo with submodules,
the submodules are by default not cloned as well.

> **ASIDE:**
> [Facebook announced in 2014 that the size of the git repo for facebook.com was 54GB](https://news.ycombinator.com/item?id=7648237),
> and it is undoubtably much larger today.
> This 54GB only includes the code directly responsible for facebook.com, and not any of the libraries that facebook.com depends on.
> Facebook's releases many public libraries on github at <https://github.com/facebook>,
> and most of these are going to be included in the main facebook.com repo as submodules.
> Some popular examples include the [react](https://github.com/facebook/react) web framework and [pytorch](https://github.com/pytorch/pytorch) machine learning library.
>
> Since these are their own separate git repos (and therefore submodules of facebook.com),
> developers can work on these libraries without needing access to the main facebook.com repo.
> Or if they are working at Facebook and do have access,
> they don't need to waste their time downloading all of the 54GB of code for facebook.com just to work on react or pytorch.
>
> The main repo for facebook.com is not public, and not even hosted with github.
> Recall that one of the advantages of git is that it is a *distributed version control system* not tied to any hosting provider.
> Facebook only uses github for its public repos,
> and uses an internal git service for storing its proprietary repos like the one for facebook.com.

Now run the command
```
$ ls
```
and notice that the `sorting` folder does exist in your forked repo.
The problem is that it is empty,
and you can verify that with the command
```
$ ls sorting
```
We need to *populate* or *hydrate* this folder, which is currently *unpopulated* or *dehydrated*.
You can do that with the following sequence of commands:
```
$ git submodule init
$ git submodule update
```
Now, you should be able to run the original command successfully
```
$ python3 runtimes.py --max_x=22
```

**Task 5: runtime of sorting an already sorted list**

Remain in the forked repo for this task.

We will now measure the runtime of the sort functions on data that has already been sorted.
Do this by adding the `--input=sorted` argument to get the following
```
$ python3 runtimes.py --max_x=23 --input=sorted
Traceback (most recent call last):
  File "runtimes.py", line 38, in <module>
    xs = FIXME
NameError: name 'FIXME' is not defined
```
You'll notice that you get a `NameError` because the word `FIXME` is undefined.

> **NOTE:**
> It is common practice in python to put the word FIXME as a variable in a code path that you haven't implemented yet.
> If that code path accidentally gets run, then python will raise the `NameError` to let you know that you are running code that you shouldn't be running.
> From python's perspective, there's nothing special about the word `FIXME`:
> it's just a variable name that has not been defined.

Follow the instructions in the comments to provide a proper definition of `xs`,
then rerun the command above to generate a markdown table of runtimes.
Copy/paste the table into the README file below this line.

<!-- add the table here -->

You should notice that the built-in `sorted` function ran much faster on this input,
but your `merge_sorted` and `quick_sorted` functions have essentially the same runtimes.
This is because TimSort is designed to not have to resort already sorted data,
and its best-case runtime is therefore $\Theta(n)$ instead of $\Theta(n\log n)$.
It turns out that in practice, data is often partially sorted,
and so TimSort is much faster than even highly optimized mergesort or quicksort implementations.

Add/commit your changes and push them to the forked github repo.
Issue a pull request to your partner with your changes,
and accept your partner's pull request when you receive it.

## Submission

Submit the link to both your and your partner's github repos to canvas.
