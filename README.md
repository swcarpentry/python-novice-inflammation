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
[https://swcarpentry.github.io/python-novice-inflammation/](https://swcarpentry.github.io/python-novice-inflammation/).

This lesson is also available in [R] and [MATLAB].

## Episodes

| \#   | Episode | Time | Question(s)                                                                  |
| --: | :------ | :--: | :--------------------------------------------------------------------------- |
| 1   | [Python Fundamentals][episode01]        | 30   | What basic data types can I work with in Python?<br>How can I create a new variable in Python?<br>Can I change the value associated with a variable after I create it?                             |
| 2   | [Analyzing Patient Data][episode02]        | 60   | How can I process tabular data files in Python?                              |
| 3   | [Visualizing Tabular Data][episode03]        | 50   | How can I visualize tabular data in Python?<br>How can I group several plots together?                                  |
| 4   | [Storing Multiple Values in Lists][episode04]        | 30   | How can I store many values together?                                        |
| 5   | [Repeating Actions with Loops][episode05]        | 30   | How can I do the same operations on many different values?                   |
| 6   | [Analyzing Data from Multiple Files][episode06]        | 20   | How can I do the same operations on many different files?                    |
| 7   | [Making Choices][episode07]        | 30   | How can my programs do different things based on data values?                |
| 8   | [Creating Functions][episode08]        | 30   | How can I define new functions?<br>What's the difference between defining and calling a function?<br>What happens when I call a function?                                              |
| 9   | [Errors and Exceptions][episode09]        | 30   | How does Python report errors?<br>How can I handle errors in Python programs?                                               |
| 10  | [Defensive Programming][episode10]        | 30   | How can I make my programs more reliable?                                    |
| 11  | [Debugging][episode11]        | 30   | How can I debug my program?                                                  |
| 12  | [Command-Line Programs][episode12]        | 30   | How can I write Python programs that will work like Unix command-line tools? |

## Contributing

[![Travis Build Status][travis_svg]][travis_url]

We welcome all contributions to improve the lesson!
Maintainers will do their best to help you if you have any questions, concerns,
or experience any difficulties along the way.

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md)
and have a look at the [more detailed guidelines][lesson-example] on proper formatting,
ways to render the lesson locally, and even how to write new episodes!

## Maintainers

Lesson maintainers are [Toan Phung][noatgnu] and [Indraneel Chakraborty][ineelhere].

## Authors

A list of contributors to the lesson can be found in [AUTHORS](AUTHORS).

## License

Instructional material from this lesson is made available under the
[Creative Commons Attribution][cc-by-human] ([CC BY 4.0][cc-by-legal]) license. Except where
otherwise noted, example programs and software included as part of this lesson are made available
under the [MIT license][mit-license]. For more information, see [LICENSE.md](LICENSE.md).

## Citation

To cite this lesson, please consult with [CITATION](CITATION).

## About Software Carpentry

Software Carpentry is a volunteer project that teaches basic computing skills to researchers since
1998\. More information about Software Carpentry can be found [here][swc-about].

## About The Carpentries

The Carpentries is a fiscally sponsored project of [Community Initiatives][community-initiatives],
a registered 501(c)3 non-profit organisation based in California, USA. We are a global community
teaching foundational computational and data science skills to researchers in academia,
industry and government. More information can be found [here][cp-about].

[swc_py_releases]: https://github.com/swcarpentry/python-novice-inflammation/releases
[shields_release]: https://img.shields.io/github/release/swcarpentry/python-novice-inflammation.svg
[slack_heroku_invite]: https://slack-invite.carpentries.org/
[create_slack_svg]: https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg
[slack_channel_url]: https://carpentries.slack.com/messages/C9Y0L6MF0
[slack_channel_status]: https://img.shields.io/badge/Slack_Channel-swc--py--inflammation-E01563.svg
[best-practices]: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
[good-practices]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510
[R]: https://github.com/swcarpentry/r-novice-inflammation
[MATLAB]: https://github.com/swcarpentry/matlab-novice-inflammation
[episode01]: https://swcarpentry.github.io/python-novice-inflammation/01-intro.html
[episode02]: https://swcarpentry.github.io/python-novice-inflammation/02-numpy.html
[episode03]: https://swcarpentry.github.io/python-novice-inflammation/03-matplotlib.html
[episode04]: https://swcarpentry.github.io/python-novice-inflammation/04-lists.html
[episode05]: https://swcarpentry.github.io/python-novice-inflammation/05-loop.html
[episode06]: https://swcarpentry.github.io/python-novice-inflammation/06-files.html
[episode07]: https://swcarpentry.github.io/python-novice-inflammation/07-cond.html
[episode08]: https://swcarpentry.github.io/python-novice-inflammation/08-func.html
[episode09]: https://swcarpentry.github.io/python-novice-inflammation/09-errors.html
[episode10]: https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html
[episode11]: https://swcarpentry.github.io/python-novice-inflammation/11-debugging.html
[episode12]: https://swcarpentry.github.io/python-novice-inflammation/12-cmdline.html
[travis_url]: https://travis-ci.org/swcarpentry/python-novice-inflammation
[travis_svg]: https://travis-ci.org/swcarpentry/python-novice-inflammation.svg?branch=gh-pages
[lesson-example]: https://carpentries.github.io/lesson-example
[noatgnu]: https://github.com/noatgnu
[ineelhere]: https://github.com/ineelhere
[valentina_staneva]: https://software-carpentry.org/team/#staneva_valentina
[swc_history]: https://software-carpentry.org/scf/history/
[cc-by-human]: https://creativecommons.org/licenses/by/4.0/
[cc-by-legal]: https://creativecommons.org/licenses/by/4.0/legalcode
[mit-license]: https://opensource.org/licenses/mit-license.html
[swc-about]: https://software-carpentry.org/about/
[community-initiatives]: https://communityin.org
[cp-about]: https://carpentries.org/about



