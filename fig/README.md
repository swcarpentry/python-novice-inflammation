## Why SVG?

SVG stands for Scalable Vector Graphics. Images in SVG format have a number of advantages over the
standard raster graphics formats, such as JPG, PNG, etc. The most important one is that SVG images
can be scaled up or down without any loss of visual clarity. This means that these images look the
same on a phone, a laptop computer, or a 70-inch TV.

The other advantage is that SVG images are, in fact, text-based files (in an XML format, but this
is an unnecessary detail). This means that SVG images are readable (by trained maintaners) and
maintainable: version control systems (VCS) such as Git can easily track changes in them.
Images in raster formats, on the other hand, are binary files, and, as all binary files,
are treated by VCSs as whole objects. This means that even a small change to an image in a binary
format forces VCS to update the entire file.


## Working with SVG figures

There is a number of third-party tools that can be used to create new of modify existing SVG images
-- feel free use any of them!  Many (if not all) of them, however, insert additional
information into the files they produce. While this information might be practical for
these tools, it is superfluous and unnecessary in our case due to the highly-collaborative nature of
the lesson development process.

Below, we provide some tips on how to remove that unnecessary information from the generated SVG
files in preparation for submitting them to our repository.

### Comments

If you're modifying an existing figure, inspect it with a text editor making note of all comments.
Comments in SVG files are eclosed between `<!--` and `-->`.  Be sure to add them back in (with
appropriate changes) after you finish editing the figure if the tool that you use removes them.

### General tips

When using any third-party editor, please make sure to:

- save the figure as "plain" SVG rather than editor-specific SVG.
- don't group elements (`<g>`) unless necessary or beneficial
- don't embed other SVG images using `<image>`

Once you finish editing the figure, clean up the figure using the tool called
[svgcleaner](https://github.com/RazrFalcon/svgcleaner):

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

- Comment about the nature of each element using `<!--` and `-->`, where applicable and when
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

Ubuntu font can be downloaded for free from:
  <https://design.ubuntu.com/font/>


## Not an SVG expert

Please don't be discouraged by the guidelines above. If you can't follow
them, please submit your contribution "as is" and mention that you could not
follow the guidelines for SVG. Maintainers will be happy to help you. Make sure,
however, that maintainers can commit to the branch you used to submit
your contribution.
