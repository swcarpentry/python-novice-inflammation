# Working with SVG figures

Feel free use any text editor or a third-party application to create new or modify existing figures.
However, please inspect the figures with a text editor making note of all comments. 
Be sure to add them back in (with appropriate changes) after you finish editing the figure. 


## Using third-party SVG editors

When using any third-party editor, please:

- save the figure as "plain" SVG rather than editor-specific SVG.
- don't group elements (`<g>`) unless necessary
- don't embed other SVG images using `<image>`
- don't use `version` attribute for the main `<svg>` element

Once you finish editing the figure, open it in a text
editor and follow these steps:

- Wrap lines to be under 100 characters (or less). For example, change this:

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

- Comment about the nature of each element using `<!--` and `-->`, for example:

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

- Avoid using "special" fonts
- Consider using: Ubuntu, Ubuntu Mono, sans-serif

**Note**:
Ubuntu font can be downloaded for free from here:
  <https://design.ubuntu.com/font/>


## Not an SVG expert

Please don't be discouraged by the guidelines above. If you can't follow
them, please submit your contribution "as is" and mention that you could not
follow the guidelines for SVG. Maintainers will be happy to help you. Make sure,
however, that maintainers can commit to the branch you used to submit
your contribution.

## "Cleaning up" SVG files

If you used an application like LibreOffice or OpenOffice to create your SVG artwork,
consider cleaning up produced files following these three steps:

1. Clean the file with [svgcleaner](https://github.com/RazrFalcon/svgcleaner):

   ```
   svgcleaner your-file.svg cleaned-01.svg
   ```

2. Clean the file with [svgo](https://github.com/svg/svgo):

   ```
   svgo -i cleaned-01.svg -o cleaned-02.svg
   ```

3. Clean/format the file with [scour](https://www.codedread.com/scour/):

   ```
   scour cleaned-02.svg cleaned-03.svg
   ```

Should any changes be necessary, it will by much easier for maintainers to work with "cleaned" SVG files.

