# Programming with Python

[![GitHub release][shields_release]][swc_py_releases]
[![Create a Slack Account with us][create_slack_svg]][slack_heroku_invite]
[![Slack Status][slack_channel_status]][slack_channel_url]

An introduction to Python for non-programmers using inflammation data.

## About the Lesson

This lesson teaches novice programmers to write modular code to perform data analysis
using Python. The emphasis, however, is on teaching language-agnostic principles of
programming such as automation with loops and encapsulation with functions,
see [Best Practices for Scientific Computing][best-practices] and
[Good enough practices in scientific computing][good-practices] to learn more.

The example used in this lesson analyses a set of 12 files with simulated inflammation
data collected from a trial for a new treatment for arthritis. Learners are shown
how it is better to automate analysis using functions instead of repeating analysis
steps manually.

The rendered version of the lesson is available at:
<https://swcarpentry.github.io/python-novice-inflammation/>.

This lesson is also available in [R][R] and [MATLAB][MATLAB].

## Episodes

| # |  Episode | Time | Question(s) |
|--:|:---------|:----:|:------------|
| 1 | [Analyzing Patient Data][episode01] | 90 | How can I process tabular data files in Python? |
| 2 | [Repeating Actions with Loops][episode02] | 30 | How can I do the same operations on many different values? |
| 3 | [Storing Multiple Values in Lists][episode03] | 30 | How can I store many values together? |
| 4 | [Analyzing Data from Multiple Files][episode04] | 20 | How can I do the same operations on many different files? |
| 5 | [Making Choices][episode05] | 30 | How can my programs do different things based on data values? |
| 6 | [Creating Functions][episode06] | 30 | How can I define new functions?<br>What’s the difference between defining and calling a function?<br>What happens when I call a function? |
| 7 | [Errors and Exceptions][episode07] | 30 | How does Python report errors?<br>How can I handle errors in Python programs? |
| 8 | [Defensive Programming][episode08] | 30 | How can I make my programs more reliable? |
| 9 | [Debugging][episode09] | 30 | How can I debug my program? |
|10 | [Command-Line Programs][episode10] | 30 | How can I write Python programs that will work like Unix command-line tools? |


## Contributing
[![Travis Build Status][travis_svg]][travis_url]

We welcome all contributions to improve the lesson!
Maintainers will do their best to help you if you have any questions, concerns,
or experience any difficulties along the way.

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md)
and have a look at the [more detailed guidelines][lesson-example] on proper formatting,
ways to render the lesson locally, and even how to write new episodes!

## Maintainers

Lesson maintainers are [Trevor Bekolay][trevor_bekolay], [Maxim Belkin][maxim_belkin],
[Anne Fouilloux][anne_fouilloux], [Valentina Staneva][valentina_staneva],
[Mike Trizna][mike_trizna], and [creator][swc_history] of Software Carpentry:
[Greg Wilson][greg_wilson]

## Authors
A list of contributors to the lesson can be found in [AUTHORS](AUTHORS)

## License
Instructional material from this lesson is made available under the Creative
Commons Attribution (CC BY 4.0) license. Except where otherwise noted, example
programs and software included as part of this lesson are made available under
the MIT license. For more information, see [LICENSE.md](LICENSE.md).

## Citation
To cite this lesson, please consult with [CITATION](CITATION)

[lesson-example]: https://carpentries.github.io/lesson-example
[anne_fouilloux]: https://github.com/annefou
[maxim_belkin]: https://github.com/maxim-belkin
[mike_trizna]: https://github.com/MikeTrizna
[trevor_bekolay]: http://software-carpentry.org/team/#bekolay_trevor
[valentina_staneva]: http://software-carpentry.org/team/#staneva_valentina
[greg_wilson]: https://github.com/gvwilson
[swc_history]: https://software-carpentry.org/scf/history/
[best-practices]: http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
[good-practices]: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510
[R]: https://github.com/swcarpentry/r-novice-inflammation
[MATLAB]: https://github.com/swcarpentry/matlab-novice-inflammation
[shields_release]: https://img.shields.io/github/release/swcarpentry/python-novice-inflammation.svg
[swc_py_releases]: https://github.com/swcarpentry/python-novice-inflammation/releases
[create_slack_svg]: https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg
[slack_heroku_invite]: https://swc-slack-invite.herokuapp.com
[slack_channel_status]: https://img.shields.io/badge/Slack_Channel-swc--py--inflammation-E01563.svg
[slack_channel_url]: https://swcarpentry.slack.com/messages/C9Y0L6MF0
[travis_svg]: https://travis-ci.org/swcarpentry/python-novice-inflammation.svg?branch=gh-pages
[travis_url]: https://travis-ci.org/swcarpentry/python-novice-inflammation
[episode01]: https://swcarpentry.github.io/python-novice-inflammation/01-numpy/index.html
[episode02]: https://swcarpentry.github.io/python-novice-inflammation/02-loop/index.html
[episode03]: https://swcarpentry.github.io/python-novice-inflammation/03-lists/index.html
[episode04]: https://swcarpentry.github.io/python-novice-inflammation/04-files/index.html
[episode05]: https://swcarpentry.github.io/python-novice-inflammation/05-cond/index.html
[episode06]: https://swcarpentry.github.io/python-novice-inflammation/06-func/index.html
[episode07]: https://swcarpentry.github.io/python-novice-inflammation/07-errors/index.html
[episode08]: https://swcarpentry.github.io/python-novice-inflammation/08-defensive/index.html
[episode09]: https://swcarpentry.github.io/python-novice-inflammation/09-debugging/index.html
[episode10]: https://swcarpentry.github.io/python-novice-inflammation/10-cmdline/index.html
