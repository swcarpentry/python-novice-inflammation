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
follow the guidelines for SVG. Maintainers will be happy to help you. Be sure,
however, that you allow maintainers to commit to the branch you used to submit
your contribution.
