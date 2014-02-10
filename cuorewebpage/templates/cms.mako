<%inherit file="cuorewebpage:templates/layout_sidebar_default.mako"/>

    <div id="main_container">
      <div class="row-fluid">
        <div class="box paint color_10">
          <div class="title">
            <div class="row-fluid">
              <h4> <span>What You See Is What You Get</span> </h4>
            </div>
            <!-- End .row-fluid -->
          </div>
          <!-- End .title -->
          <div class="content full">
            <form method="post" action="http://tinymce.moxiecode.com/dump.php?example=true">

              <!-- Gets replaced with TinyMCE, remember HTML in a textarea should be encoded -->
              <textarea id="elm3" name="elm3" rows="30" cols="80" style="width: 100%">

<h1><span style="font-size: large;">A philosophy</span></h1>
<p><span style="font-size: small;">A philosophy professor stood before his class with some items on the table in front of him. When the class began, wordlessly he picked up a very large and empty mayonnaise jar and proceeded to fill it with rocks, about 2 inches in diameter.</span></p>
<p><span style="font-size: small;">He then asked the students if the jar was full. They agreed that it was.</span></p>
<p><span style="font-size: small;">So the professor then picked up a box of pebbles and poured them into the jar. He shook the jar lightly. The pebbles, of course, rolled into the open areas between the rocks.</span></p>
<p><span style="font-size: small;">He then asked the students again if the jar was full. They agreed it was.</span></p>
<p><span style="font-size: small;">The professor picked up a box of sand and poured it into the jar. Of course, the sand filled up everything else. He then asked once more if the jar was full. The students responded with a unanimous &ldquo;Yes.&rdquo;</span></p>
<p><span style="font-size: small;">&ldquo;Now,&rdquo; said the professor, &ldquo;I want you to recognize that this jar represents your life. The rocks are the important things &ndash; your family, your partner, your health, your children &ndash; things that if everything else was lost and only they remained, your life would still be full.</span></p>
<p><span style="font-size: small;">The pebbles are the other things that matter &ndash; like your job, your house, your car.</span></p>
<p><span style="font-size: small;">The sand is everything else. The small stuff.&rdquo;</span></p>
<p><span style="font-size: small;">&ldquo;If you put the sand into the jar first,&rdquo; he continued &ldquo;there is no room for the pebbles or the rocks. The same goes for your life.</span></p>
<p><span style="font-size: small;">If you spend all your time and energy on the small stuff, you will never have room for the things that are important to you. Pay attention to the things that are critical to your happiness. Play with your children. Take your partner out dancing. There will always be time to go to work, clean the house, give a dinner party and fix the disposal.</span></p>
<p><span style="font-size: small;">Take care of the rocks first &ndash; the things that really matter. Set your priorities. The rest is just sand.&rdquo;</span></p>
</textarea>
            </form>
          </div>
        </div>
        <!-- End .box -->
      </div>
      <!-- End .row-fluid -->
    </div>
    <!-- End #container -->

<div class="background_changer dropdown">
  <div class="dropdown" id="colors_pallete"> <a data-toggle="dropdown" data-target="drop4" class="change_color"></a>
    <ul  class="dropdown-menu pull-left" role="menu" aria-labelledby="drop4">
      <li><a data-color="color_0" class="color_0" tabindex="-1">1</a></li>
      <li><a data-color="color_1" class="color_1" tabindex="-1">1</a></li>
      <li><a data-color="color_2" class="color_2" tabindex="-1">2</a></li>
      <li><a data-color="color_3" class="color_3" tabindex="-1">3</a></li>
      <li><a data-color="color_4" class="color_4" tabindex="-1">4</a></li>
      <li><a data-color="color_5" class="color_5" tabindex="-1">5</a></li>
      <li><a data-color="color_6" class="color_6" tabindex="-1">6</a></li>
      <li><a data-color="color_7" class="color_7" tabindex="-1">7</a></li>
      <li><a data-color="color_8" class="color_8" tabindex="-1">8</a></li>
      <li><a data-color="color_9" class="color_9" tabindex="-1">9</a></li>
      <li><a data-color="color_10" class="color_10" tabindex="-1">10</a></li>
      <li><a data-color="color_11" class="color_11" tabindex="-1">10</a></li>
      <li><a data-color="color_12" class="color_12" tabindex="-1">12</a></li>
      <li><a data-color="color_13" class="color_13" tabindex="-1">13</a></li>
      <li><a data-color="color_14" class="color_14" tabindex="-1">14</a></li>
      <li><a data-color="color_15" class="color_15" tabindex="-1">15</a></li>
      <li><a data-color="color_16" class="color_16" tabindex="-1">16</a></li>
      <li><a data-color="color_17" class="color_17" tabindex="-1">17</a></li>
      <li><a data-color="color_18" class="color_18" tabindex="-1">18</a></li>
      <li><a data-color="color_19" class="color_19" tabindex="-1">19</a></li>
      <li><a data-color="color_20" class="color_20" tabindex="-1">20</a></li>
      <li><a data-color="color_21" class="color_21" tabindex="-1">21</a></li>
      <li><a data-color="color_22" class="color_22" tabindex="-1">22</a></li>
      <li><a data-color="color_23" class="color_23" tabindex="-1">23</a></li>
      <li><a data-color="color_24" class="color_24" tabindex="-1">24</a></li>
      <li><a data-color="color_25" class="color_25" tabindex="-1">25</a></li>
    </ul>
  </div>
</div>
<!-- End .background_changer -->

<%block name="javascript">

<!-- Le javascript
    ================================================== -->
<!-- General scripts -->
<script src="js/jquery.js" type="text/javascript"> </script>
<script src="js/jquery-ui-1.8.23.custom.min.js" type="text/javascript"></script>
<!--[if !IE]> -->
<script src="js/plugins/enquire.min.js" type="text/javascript"></script>
<!-- <![endif]-->
<script language="javascript" type="text/javascript" src="js/plugins/jquery.sparkline.min.js"></script>
<script src="js/plugins/excanvas.compiled.js" type="text/javascript"></script>
<script src="js/bootstrap-transition.js" type="text/javascript"></script>
<script src="js/bootstrap-alert.js" type="text/javascript"></script>
<script src="js/bootstrap-modal.js" type="text/javascript"></script>
<script src="js/bootstrap-dropdown.js" type="text/javascript"></script>
<script src="js/bootstrap-scrollspy.js" type="text/javascript"></script>
<script src="js/bootstrap-tab.js" type="text/javascript"></script>
<script src="js/bootstrap-tooltip.js" type="text/javascript"></script>
<script src="js/bootstrap-popover.js" type="text/javascript"></script>
<script src="js/bootstrap-button.js" type="text/javascript"></script>
<script src="js/bootstrap-collapse.js" type="text/javascript"></script>
<script src="js/bootstrap-carousel.js" type="text/javascript"></script>
<script src="js/bootstrap-typeahead.js" type="text/javascript"></script>
<script src="js/bootstrap-affix.js" type="text/javascript"></script>
<script src="js/fileinput.jquery.js" type="text/javascript"></script>
<script src="js/jquery.touchdown.js" type="text/javascript"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.uniform.min.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.tinyscrollbar.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jnavigate.jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jquery.touchSwipe.min.js"></script>


<!-- TinyMCE Editor -->
<script type="text/javascript" src="js/plugins/tinymce/jscripts/tiny_mce/tiny_mce.js"></script>

<!-- Custom made scripts for this template -->
<script src="js/scripts.js" type="text/javascript"></script>
<script type="text/javascript">
  /**** Specific JS for this page ****/
 $(document).ready(function() {
  // TinyMCE
  tinyMCE.init({
    // General options
    mode : "exact",
    elements : "elm3",
    theme : "advanced",
    skin : "o2k7",
    skin_variant : "silver",
    plugins : "lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",
    // Theme options
    theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,restoredraft",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resizing : true,
    // Drop lists for link/image/media/template dialogs
    template_external_list_url : "lists/template_list.js",
    external_link_list_url : "lists/link_list.js",
    external_image_list_url : "lists/image_list.js",
    media_external_list_url : "lists/media_list.js",
  });
});




</script>
</%block>
