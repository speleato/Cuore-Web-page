  <%inherit file="layout_sidebar_default.mako"/>

  <div id="main_container">
      <div class="row-fluid">
        <div class="span7">
          <div class="box paint color_7">
            <div class="title">
              <h4> <i class="icon-book"></i><span>Blog Dashboard</span> </h4>
            </div>
            <div class="content">
              <form class="form-horizontal row-fluid" action="${request.route_url('Blog_Action',action='dashboard')}" method="post">
                  <div class="form-row control-group row-fluid">
                      <label class="control-label span3" for="max-length">Blog Title</label>
                      <div class="controls span9">
                          <input type="text" name="name" id="max-length" class="row-fluid" maxlength="50" placeholder="Max length 50 characters" rel="tooltip" data-placement="top" data-original-title="You cannot write more than 50 characters.">
                      </div>
                  </div>
<!--                <div class="form-row control-group row-fluid">
                  <label class="control-label span3" for="search-input">File upload</label>
                  <div class="controls span9">
                    <div class="input-append row-fluid">
                      <input type="file" class="spa1n6 fileinput" id="search-input">
                      </div>
                  </div>
                </div>
                -->
                  <div class="form-row control-group row-fluid">
                      <label class="control-label span3" for="default-textarea">Description</label>
                      <div class="controls span9">
                          <textarea name="description" rows="7" class="row-fluid" id="default-textarea"></textarea>
                      </div>
                  </div>
                  <!--
                  <div class="form-row control-group row-fluid">
                      <label class="control-label span3" for="elastic-textarea">Elastic textarea <span class="help-block">With autogrow feature</span> </label>
                      <div class="controls span9">
                          <textarea rows="3" class="row-fluid autogrow" id="elastic-textarea" placeholder="try to add new lines.."></textarea>
                      </div>
                  </div>
                  <div class="form-row control-group row-fluid">
                      <label class="control-label span3" for="text">With Characters Limit</label>
                      <div class="controls span9">
                          <textarea id="text" rows="3" class="row-fluid"></textarea>
                          <div id="bottom"> <span id="chars">100</span> characters remaining </div>
                      </div>
                  </div>
                  -->
                <div class="form-actions row-fluid">
                <div class="span3 visible-desktop"></div>
                  <div class="span7 ">
                    <button type="submit" class="btn btn-primary">Submit Post</button>
                    <button type="button" class="btn btn-secondary">Cancel</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      <!-- End .span7 -->
      </div>
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

<%block name="javascript">${parent.javascript()}
<script language="javascript" type="text/javascript" src="../js/plugins/wysihtml5-0.3.0.min.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/bootstrap-wysihtml5.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/jquery.peity.min.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/textarea-autogrow.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/character-limit.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/jquery.maskedinput-1.3.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/chosen/chosen/chosen.jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/bootstrap-datepicker.js"></script>
<script language="javascript" type="text/javascript" src="../js/plugins/bootstrap-colorpicker.js"></script>

<!-- Custom made scripts for this template -->
<script src="../js/scripts.js" type="text/javascript"></script>
<script type="text/javascript">
  /**** Specific JS for this page ****/
 $(document).ready(function () {

        $('textarea.autogrow').autogrow();
        var elem = $("#chars");
        $("#text").limiter(100, elem);
        // Mask plugin http://digitalbush.com/projects/masked-input-plugin/
        $("#mask-phone").mask("(999) 999-9999");
        $("#mask-date").mask("99-99-9999");
        $("#mask-int-phone").mask("+33 999 999 999");
        $("#mask-tax-id").mask("99-9999999");
        $("#mask-percent").mask("99%");
        // Editor plugin https://github.com/jhollingworth/bootstrap-wysihtml5/
        $('#editor1').wysihtml5({
          "image": false,
          "link": false
          });
        // Chosen select plugin
        $(".chzn-select").chosen({
          disable_search_threshold: 10
        });
        // Datepicker
        $('#datepicker1').datepicker({
          format: 'mm-dd-yyyy'
        });
        $('#datepicker2').datepicker();
        $('.colorpicker').colorpicker()
        $('#colorpicker3').colorpicker();
    });



</script>
</%block>
