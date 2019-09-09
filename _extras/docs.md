---
layout: base
title: "HTML Shared Workspace Template"
---
<blockquote><div style=' border:2px solid black; background:white;margin:10px;padding:5px;'><h1> Shared Workspace Exporter </h1><p>To use, click copy to clipboard, go to your Shared Workspace, and paste, or click save page to disk for Shared Workspace import, go to Shared Workspace, click the double-arrow button in the top right, choose the file just downloaded, and click import now.</p>
  <!-- <p>Workshop ID:<input id="workshop-id" name="workshop-id" value="WORKSHOP_ID_HERE"/></p> -->
  <button id="copy-button" data-clipboard-target="#data-copy-target"  style="">Copy to Clipboard</button><button id="save-button" onClick="save()"  style="margin-left:10px;">Save page to disk for Shared Workspace import</button></div></blockquote>

<div id="data-copy-target">
<blockquote >
<p>Welcome to The Carpentries Shared Workspace!</p>

<p>This pad is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents.</p>

<p>Use of this service is restricted to members of The Carpentries community; this is not for general purpose use (for that, try Shared Workspace.wikimedia.org).</p>

<p>Users are expected to follow our code of conduct: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html</p>

<p>All content is publicly available under the Creative Commons Attribution License: https://creativecommons.org/licenses/by/4.0/</p>
<br/> ____________________________________________________________________________________________________________
<br/>
<b>Sign in: Name, Institution, Email, Twitter (optional)</b><br/>
Please sign in so we can record your attendance.<br/>
<ul>
  <li>&nbsp;</li>
  <li>&nbsp;</li>
  <li>&nbsp;</li>
  <li>&nbsp;</li>
</ul>
<br/>

Please make sure you have filled out the pre-training survey.
 
</blockquote> 




{% comment %}
Create anchor for each one of the episodes.

Do not use the filter markdownify when specifying an <li> because otherwise firefox 68 adds extra bullets inside the included <p>.

{% endcomment %}

{% for episode in site.episodes %}
<h1>{{episode.title}} <br/><a href="{{site.url}}{{ relative_root_path }}{{episode.url}}">{{site.url}}{{ relative_root_path }}{{episode.url}}</a></h1>

<br/>
<blockquote>
<h2>Questions:</h2>
<ul>
{% for question in episode.questions %}
<li>{{question}}</li>
{% endfor %}
</ul>
</blockquote>

<blockquote>
<h2>Objectives:</h2>
<ul>
{% for objective in episode.objectives %}
<li>{{objective}}</li>
{% endfor %}
</ul>
</blockquote>



{{episode.content}}

<blockquote>
  <br/><br/>
<h2>Keypoints:</h2>
<ul>
{% for keypoint in episode.keypoints %}
<li>{{keypoint}}</li>
{% endfor %}
</ul>
<br/><br/>
-------------------------------------------------------<br/><br/><br/>

</blockquote>



{% endfor %}

<blockquote>
<p><b>BEFORE YOU LEAVE</b></p>
<p>Please fill out the post-training survey</p>


<p>Lesson content on this page released under a creative commons attribution license. Lesson Content &copy; 2018-2019 The Carpentries .</p>
</blockquote>
</div>
<script src='../assets/js/clipboard.min.js'></script>

<script>

//https://stackoverflow.com/a/29462236/263449
function save() {
  var htmlContent = [$("#data-copy-target").html()];
  var bl = new Blob(htmlContent, {type: "text/html"});
  var a = document.createElement("a");
  a.href = URL.createObjectURL(bl);
  a.download = "Shared Workspace-export-from-carpentries.html";
  a.hidden = true;
  document.body.appendChild(a);
  a.innerHTML = "download link";
  a.click();
}
</script>


<script>  window.onload = function() {

//Why paste workshop ID two places in the middle of the document when it can be highlighted front and centre and changed twice automatically?
// $("input#workshop-id").change(function(){
//   $("#preid").text($(this).val());
//   $("#postid").text($(this).val());
// })

// Find headers (h1..3), and add physical linebreaks around them, while trying to minimise the appearance of physical linebreaks, so that they render in the degraded html of Shared Workspace. 

// $( "h1, h2, h3" ).not("blockquote h2").before("<br style='line-height:0px'/><br/>").after("<br/>");

// Also wrap headers in bold, as headers do not transfer over to the Shared Workspace.
// $( "h1, h2, h3" ).not("blockquote h2").wrap("<b>");

// We want to differentiate level 2 and level 3 headers, so I'm progressively adding styling to them, while retaining the bold.
// $("h2").wrap("<i>");
// $("h3").wrap("<u>");


// //Also need to kill images. Not sure we need to keep images in blockquotes, but eh, might be useful some day if we print it off or something.
// //https://stackoverflow.com/a/19073240/263449


$("img").each(function(){
  $(this).after("<blockquote><p>Image: "+$(this).prop('alt')+" "+$(this).prop('src')+"</p></blockquote>")
})


// Remove all paragraph text which exists outside of a blockquote
$( "p").not('blockquote p').remove();

$( "pre").not('blockquote pre').parent().parent().remove();

// Also remove all unordered lists.
$( "ul").not('blockquote ul').remove();

// Can't forget ordered lists.
$( "ol").not('blockquote ol').remove();

// The navbar presents copying problems, so we need to clear that as well
$(".navbar").remove();

// Code should also not be copied over to the Shared Workspace. Code is indicated by the .source class on divs, rather than as a blockquote
$( "div.source").not('blockquote div.source').remove();

// Other divs need to be removed too
//$( "[class^='highlight']").not('blockquote [class^="highlight"]').remove();

//oops, forgot to clear out the footer.
$("footer").remove();


//Take all ordered lists and turn them into unordered lists, because ordered lists don't transfer well into the Shared Workspace.
//https://stackoverflow.com/a/12679823/263449
$($('ol').get().reverse()).each(function(){
  $(this).replaceWith($('<ul>'+$(this).html()+'</ul>'))
})


//Remove all solutions from the text
$("blockquote.solution").remove();


// I wanted to keep challenges, callouts, and discussion blocks. However, the icons don't transfer, so I need to add the calling-out word (exercise, etc) to the header (and then render the header as an h2) so that there is appropriate formatting transfered to the Shared Workspace, and that each of these has a useful label in the text-only zone.
$("blockquote.challenge h2").each(function(){
  var oldtext = $(this).text();
  $(this).text("Exercise: "+oldtext).before("<br/><br/>").wrap("<b>").wrap("<i>");
});
$("blockquote.callout h2").each(function(){
  var oldtext = $(this).text();
  $(this).text("Callout: "+oldtext).before("<br/><br/>").wrap("<b>").wrap("<i>");
  
});
$("blockquote.discussion h2").each(function(){
  var oldtext = $(this).text();
  $(this).text("Discussion: "+oldtext).before("<br/><br/>").wrap("<b>").wrap("<i>");
  
});


//Once we've cleaned out things, we need to unblockquote everything for best pasting.
//https://stackoverflow.com/a/17872365/263449
$("blockquote").contents().unwrap();



//To address @maxim-belkin's comments on code formatting and newlines being lost.
//$("*").removeAttr('id');

$("div[class^='language']").each(function(){
  if ($(this).hasClass("language-python") == true) {
    $(this).before("<h3>Python:</h3>");
  } 
  else {
    $(this).before("<h3>Code:</h3>");
  }

})
$("div[class^='output']").each(function(){
  $(this).before("<h3>Output:</h3>");
  

})

$("div").after("<br/>");

// $("pre").each(function(){
//   $(this).text($(this).text().replace("\n","\n\n")) ;
// })

//remove all non-essential formatting. (Specifically preserving the container.)
$("[class]").not(".container").removeClass();

// //This is just a check for me to make sure that execution has proceeded this far and I haven't messed something fundamental up.
// //console.log("hi");

//https://stackoverflow.com/a/22581382/263449
new ClipboardJS("#copy-button");

  }

</script>

