<%inherit file="cuorewebpage:templates/layout_sidebar_default.mako"/>

<div id="main_container">
  <div class="row-fluid">
    <div class="box paint_hover color_3">
      <div id="elfinder"></div>
    </div>
    <!-- End .box -->
  </div>
  <!-- End .row-fluid -->
</div>
<!-- End #container -->
</div>
<div id="fileUploader">
    <form action="files/upload" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <label for="file">File</label>
        <input id="file" name="file" type="file" value="" />
        <input type="submit" value="submit" />
        <div style="margin-left:400px">
            <p>Which department does this file belong to?</p>
            %for i in range(0, len(department)):
                <input type="radio" name="department" value="${department[i]}">${department[i]}</i><br/>
            %endfor
        </div>
        <div style="margin-left:400px">
            <p>Which project does this file belong to?</p>
            %for i in range(0, len(projects)):
                <input type="radio" name="project" value="${projects[i]}">${projects[i]}</i><br/>
            %endfor
        </div>
        <div style="margin-left:400px">
            <p>Which task does this file belong to?</p>
            %for i in range(0, len(tasks)):
                <input type="radio" name="task" value="${tasks[i]}">${tasks[i]}</i><br/>
            %endfor
        </div>
    </form>
</div>
<%block name="footer">
${parent.footer()}
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
</%block>

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
<script language="javascript" type="text/javascript" src="js/plugins/jquery.peity.min.js"></script>


<!-- Custom made scripts for this template -->
<script src="${request.static_url('cuorewebpage:js/scripts.js')}" type="text/javascript"></script>

<!-- File Explorer - elFinder JS (REQUIRED) -->
<script type="text/javascript" src="${request.static_url('cuorewebpage:js/plugins/elfinder2.0/js/elfinder.min.js')}"></script>

<!-- elFinder translation (OPTIONAL) -->
<script type="text/javascript" src="${request.static_url('cuorewebpage:js/plugins/elfinder2.0/js/i18n/elfinder.ru.js')}"></script>

<!-- elFinder initialization (REQUIRED) -->
<script type="text/javascript" charset="utf-8">
      $(document).ready(function() {
          $('#sidebar').tinyscrollbar();
        var elf = $('#elfinder').elfinder({
          url : '${request.static_url('cuorewebpage:js/plugins/elfinder2.0/php/connector.php')}',  // connector URL (REQUIRED)
          height: 900
        }).elfinder('instance');
      });
    </script>
<script type="text/javascript">
  /**** Specific JS for this page ****/



</script>
</%block>
