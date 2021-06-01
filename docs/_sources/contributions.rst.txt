============
Contributing
============

If you feel like making this documentation better there's several ways you can
go about it, but the first thing you'll need is a `GitHub Account`_. Once
you've got that, have a look at the following sections…


Suggestions
===========

If you don't feel up to writing new documents or editing existing ones, we'd
love to here your suggestions for what needs fixing or what new topics you'd
like to see covered. You can do this by `creating an issue`_ in the repository
containing these documents.

Please do search the issues first to make sure somebody hasn't already
requested what you want!


Small Edits
===========

Simple changes to existing documents (spelling, grammar, punctuation, or simple
re-wording) are probably easiest to do through GitHub's own web interface:

* Go to the topic you want to edit and find the "Edit this page on GitHub" link
  at the bottom of it. Clicking this link will take you straight to the source
  file for that topic.

* Click on the pencil icon at the top-right of the file and make your changes.
  If you want a (relatively crude) preview of what your changes will look like,
  select the "Preview" tab at the top of the editor.

* Once your changes are made, fill in the brief form at the bottom with a
  subject ("spelling correction", "grammar fix", etc.) and a brief description
  of the change you want to make.

* Click "Propose changes" and a new PR (Pull Request) will be opened proposing
  your changes.

* At this point, the developers of the documentation can review your proposal
  and merge them (or reject them).


Larger Edits on GitHub
======================

For changes involving multiple files, where you're happy to work within the
GitHub web interface, you can take a clone of the documentation repository and
work on multiple files before proposing the changes:

* Go to any topic and click the "Edit this page on GitHub" link at the bottom
  of it. Clicking this link will take you to the source file for that topic.

* Click on the "Fork" button at the top right of the page to make a clone of
  the repository under your account.

* Click on the "master" branch button just above the file list and enter a new
  branch name for your changes, e.g. "fix-links" or "new-foo-topic". Select the
  "Create branch: new-foo-topic" link that appears.

* Now edit all the files under :file:`source/` that you wish to.

  - For each file, just select it, click the pencil icon at the top-right and
    makes your changes. A (relatively crude) preview of what your changes in
    this file will look like can be shown by selecting the "Preview" tab at the
    top of the editor.

  - When you're done changing a file, enter a brief description of the changes
    in the form at the bottom, make sure "Commit directly to the
    "new-foo-topic" branch is selected, and click "Commit changes"

* When all your changes are made, click on the "Code" link at the top left to
  return to the root directory for your clone (while staying on the
  "new-foo-topic" branch).

* You may see a "new-foo-topic had recent pushes N minutes ago" message with a
  "Compare & pull request" button in which case you can just select that to
  propose your changes.

  - Alternatively, if the message doesn't appear (because you had a tea break
    after all that writing!) just pick "Contribute" and "Open pull request".
    If "Open pull request" isn't accessible under "Contribute", check you've
    got your "new-foo-topic" branch selected instead of "master".

* Review the changes you want to propose, write a quick description of them an
  hit "Create pull request" to propose all your changes as a batch.


Larger Edits Locally
====================

For more complex changes (new topics, or large changes covering multiple
files), it's easier to make the changes in a clone of the repository on your
machine, which allows you to use your favourite editor, and preview things
precisely. Obviously this requires a little more work to setup, but we've tried
to make things as easy as possible for you:

* On your machine, install the pre-requisites for building the documentation
  and dealing with git. For example, on Ubuntu::

    $ sudo apt install python3 python3-sphinx git make

* Go to the `Documentation repository`_ and select "Fork" at the top right to
  make a clone of the repository under your account.

* On your machine, clone your clone (!) with git::

    $ git clone git@github.com:my-github-username/documentation

* Start the development previewer so you can auto-build the docs as you make
  changes::

    $ cd documentation
    $ git checkout -b my-branch
    $ make preview

* Edit the files under :file:`documentation/source/` as you wish. As you save
  your changes, the previewer should auto-rebuild the documentation (watch for
  errors in the output!) and you can visit ``http://localhost:8000/`` to see
  what the documentation will look like.

* Commit your changes locally::

    $ git add source/files-you-have-changed.rst
    $ git commit -m "A description of the changes you have made"

* Update your clone on GitHub with the changes::

    $ git push origin my-branch

* The output of the :command:`git push` command should include a web link you
  can open to propose your changes back to the original repository.


.. _GitHub Account: https://github.com/join
.. _Documentation repository: https://github.com/waveform80/doctest
.. _creating an issue: https://github.com/waveform80/doctest/issues
