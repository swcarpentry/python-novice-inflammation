## Why SVG?

The SVG format (for "Scalable Vector Graphics") has a number of advantages over standard "raster"
graphics formats such as JPG, PNG, etc. Most importantly, as the name suggests, SVG images scale
up or down without loss of visual clarity: they look equally good on a phone, a laptop computer,
or a 70-inch screen, and don't blur when scaled up.

Additionally, SVG is a text-based format (based on XML, if you care). As text files, SVG images
are thus human-readable (a trained eye makes sense of them) and maintainable: easy to manually
edit, and efficiently tracked by version control systems (VCSs) such as Git. By contrast, images
in raster formats, being binary files, are versioned as whole objects -- the slightest change
results in updating the entire file.

## Working with SVG figures

A number of tools can create or modify SVG images -- pick one you like!

Many tools, however, delete comments they don't deem useful, and insert extra information useful
to them, but unneeded for us, and unsuited to our highly collaborative lesson development process.

Below are some tips on keeping the information we need and removing the information we don't need
in SVG files before submitting them to our repository.

### Comments

Before modifying an existing figure, inspect it with a text editor, making note of all comments,
which in SVG files are enclosed between `<!--` and `-->`.  Be sure to add them back in (with
appropriate changes) after editing the figure, if the tool you use removed them.

### General tips

When using any SVG editor, please make sure to:

- save the figure as "plain" SVG rather than editor-specific SVG.
- not group elements (`<g>`) unless necessary or beneficial
- not embed other SVG images using `<image>`

After editing the figure, clean it up using the command-line tool
[svgcleaner](https://github.com/RazrFalcon/svgcleaner), by running the following in a terminal
(replace `SVG_figure` by the name of the SVG figure):

```
svgcleaner \
  --indent 2 \
  --ungroup-defs no \
  --multipass \
  --coordinates-precision 1 \
  --properties-precision 1 \
  --paths-coordinates-precision 1 \
  SVG_figure.svg SVG_figure_svgcleaner.svg
```

Alternatively, you can also use [svgo](https://github.com/svg/svgo) or
[scour](https://www.codedread.com/scour/).

**The following steps are optional.**

Open the file produced by `svgcleaner` (`SVG_figure_svgcleaner.svg` in the example above)
and follow these steps:

- Wrap lines to be under 100 characters (or less) if possible. For example, change this:

  ```xml
  <text x="42" y="36" font-family="sans-serif" font-size="19px" font-weight="bold" text-anchor="middle">65.0</text>
  ```
  to this:
  ```xml
     <text x="42" y="36"
           font-family="sans-serif"
           font-size="19px"
           font-weight="bold"
           text-anchor="middle">65.0</text>
  ```

- Comment on the nature of each element, using `<!--` and `-->`, where applicable and when
  feasible. For example:

  ```xml
   <!-- Text: "65.0" -->
   <text x="42" y="36"
   ...
  ```

- Remove editor-specific styles
- Make sure that elements' attributes appear before styles
- Add empty lines between SVG elements
- Remove `id` properties unless used to control elements (in interactive SVG figures)

## Fonts

- Avoid using "special" fonts.
- Consider using: Ubuntu, Ubuntu Mono, sans-serif

The Ubuntu font can be downloaded for free from:
  <https://design.ubuntu.com/font/>

## Not an SVG expert

Don't let the above guidelines discourage you. If needed, submit your contribution "as is" and
mention which steps you skipped. Maintainers will happily help -- make sure they can commit to the
branch you use to submit your contribution.
