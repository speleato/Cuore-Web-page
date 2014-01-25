<%inherit file="layout_sidebar_default.mako"/>
<% from datetime import datetime %>
<% EMAX = 5 %>
<% TMAX = 4 %>

    <div id="main_container">
      <div class="row-fluid ">
        <div class="span12">
          <div class="box paint color_18">
            <div class="title">
              <h4> <i class=" icon-bar-chart"></i><span>Tasks</span> </h4>
            </div>
            <!-- End .title -->
            <div class="content top">
              <table id="datatable_example" class="responsive table table-striped table-bordered" style="width:100%;margin-bottom:0; ">
                <thead>
                  <tr>
                    <th class="no_sort"> <label class="checkbox ">
                        <input type="checkbox">
                      </label>
                    </th>
                    <th class="no_sort"> Image </th>
                    <th class="no_sort to_hide_phone"> Description </th>
                    <th class="no_sort to_hide_phone"> Info </th>
                    <th class="no_sort"> Author </th>
                    <th class="to_hide_phone ue no_sort"> Views </th>
                    <th class="ue no_sort"> <i class="icon-comments big"></i> </th>

                    <th class="ms no_sort "> Actions </th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar4.png"></td>
                    <td class="to_hide_phone"> Full price for gum?! </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 196 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .png </div>
                        </small> </div></td>
                    <td> Fry </td>
                    <td class="to_hide_phone"> 46,67% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 14 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar1.png"></td>
                    <td class="to_hide_phone"> Surrender your mysteries to Zoidberg! </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 82 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .jpg </div>
                        </small> </div></td>
                    <td> Zoidberg </td>
                    <td class="to_hide_phone"> 16,67% <span class="line">1,1,2,-1,-3,-2,2,4,5,2</span></td>
                    <td> 21 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar2.png"></td>
                    <td class="to_hide_phone"> The point is, by my standards, I won fair and square. </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 392 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .png </div>
                        </small> </div></td>
                    <td> Bender </td>
                    <td class="to_hide_phone"> 26,67% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 12 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar3.png"></td>
                    <td class="to_hide_phone"> File not found?! </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 403 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .gif </div>
                        </small> </div></td>
                    <td> Fry </td>
                    <td class="to_hide_phone"> 7,32% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 2 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar5.png"></td>
                    <td class="to_hide_phone"> I'm Santa Claus! </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 546 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .jpg </div>
                        </small> </div></td>
                    <td> Simpson </td>
                    <td class="to_hide_phone"> 48,33% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 17 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar6.png"></td>
                    <td class="to_hide_phone"> And I'd do it again! And perhaps a third time!! </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 294 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .png </div>
                        </small> </div></td>
                    <td> Fry </td>
                    <td class="to_hide_phone"> 88,22% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 0 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                  <tr>
                    <td><label class="checkbox ">
                        <input type="checkbox">
                      </label></td>
                    <td><img class="thumbnail small" src="img/message_avatar7.png"></td>
                    <td class="to_hide_phone"> Perfectly symmetrical violence never solved anything. </td>
                    <td class="to_hide_phone"><div class="row-fluid"> <small>
                        <div class="span12"> <strong>Size:</strong> 9.996 Kb </div>
                        </small> </div>
                      <div class="row-fluid"> <small>
                        <div class="span12"> <strong>Format:</strong> .psd </div>
                        </small> </div></td>
                    <td> Leela </td>
                    <td class="to_hide_phone"> 99,67% <span class="line">5,3,2,-1,-3,-2,2,3,5,2</span></td>
                    <td> 93 </td>

                    <td class="ms"><div class="btn-group"> <a class="btn btn-small" rel="tooltip" data-placement="left" data-original-title=" edit "><i class="gicon-edit"></i></a> <a class="btn btn-small" rel="tooltip" data-placement="top" data-original-title="View"><i class="gicon-eye-open"></i></a> <a class="btn  btn-small" rel="tooltip" data-placement="bottom" data-original-title="Remove"><i class="gicon-remove "></i></a> </div></td>
                  </tr>
                </tbody>
              </table>
              <div class="row-fluid  control-group mt15">

                <div class="pull-left span6 visible-desktop" action="#">
                  <div class="row-fluid fluid ">
                    <div class="controls inline input-large pull-left ">
                      <select data-placeholder="Bulk actions: " class="chzn-select " id="default-select">
                        <option value=""></option>
                        <option value="Bender">Edit</option>
                        <option value="Zoidberg">Regenerate thumbnails</option>
                        <option value="Kif Kroker">Delete Permanently</option>
                      </select>
                    </div>
                    <button type="button" class="btn btn-inverse inline">Apply</button>
                  </div>
                </div>
                <div class="span6">
                  <div class="pagination pull-right ">
                    <ul>
                      <li><a href="#">Prev</a></li>
                      <li><a href="#">1</a></li>
                      <li><a href="#">2</a></li>
                      <li><a href="#">3</a></li>
                      <li><a href="#">4</a></li>
                      <li><a href="#">Next</a></li>
                    </ul>
                  </div >
                </div>
              </div>
            </div>
            <!-- End row-fluid -->
          </div>
          <!-- End .content -->
        </div>
        <!-- End box -->
      </div>
      <!-- End .span12 -->
    </div>
    <!-- End .row-fluid -->
    <div class="row-fluid">
      <div class="span6">
        <div class="box paint color_12">
          <div class="title">
            <h4> <i class=" icon-bar-chart"></i><span>Default Style</span> </h4>
          </div>
          <!-- End .title -->
          <div class="content">
            <p> For basic styling—light padding and only horizontal dividers—add the base class <code>.table</code> to any <code>&lt;table&gt;</code>. </p>
            <table class="table">
              <thead>
                <tr>
                  <th> # </th>
                  <th> First Name </th>
                  <th> Last Name </th>
                  <th> Username </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 1 </td>
                  <td> Mark </td>
                  <td> Otto </td>
                  <td> @mdo </td>
                </tr>
                <tr>
                  <td> 2 </td>
                  <td> Jacob </td>
                  <td> Thornton </td>
                  <td> @fat </td>
                </tr>
                <tr>
                  <td> 3 </td>
                  <td> Larry </td>
                  <td> the Bird </td>
                  <td> @twitter </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- End .box .span6 -->
      <div class="span6">
        <div class="box paint color_25">
          <div class="title">
            <h4> <i class=" icon-bar-chart"></i><span>Striped Table</span> </h4>
          </div>
          <!-- End .title -->
          <div class="content">
            <p> Add <code>.table-striped</code> to the <code>.table</code> base class. </p>
            <table class="table table-striped">
              <thead>
                <tr>
                  <th> # </th>
                  <th> First Name </th>
                  <th> Last Name </th>
                  <th> Username </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 1 </td>
                  <td> Mark </td>
                  <td> Otto </td>
                  <td> @mdo </td>
                </tr>
                <tr>
                  <td> 2 </td>
                  <td> Jacob </td>
                  <td> Thornton </td>
                  <td> @fat </td>
                </tr>
                <tr>
                  <td> 3 </td>
                  <td> Larry </td>
                  <td> the Bird </td>
                  <td> @twitter </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- End .box .span6 -->
    </div>
    <!-- End .row-fluid -->
    <div class="row-fluid">
      <div class="span6">
        <div class="box paint color_12">
          <div class="title">
            <h4> <i class=" icon-bar-chart"></i><span>Bordered Table</span> </h4>
          </div>
          <!-- End .title -->
          <div class="content">
            <p> Add <code>.table-bordered</code> to the <code>.table</code> base class. </p>
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th> # </th>
                  <th> First Name </th>
                  <th> Last Name </th>
                  <th> Username </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 1 </td>
                  <td> Mark </td>
                  <td> Otto </td>
                  <td> @mdo </td>
                </tr>
                <tr>
                  <td> 2 </td>
                  <td> Jacob </td>
                  <td> Thornton </td>
                  <td> @fat </td>
                </tr>
                <tr>
                  <td> 3 </td>
                  <td> Larry </td>
                  <td> the Bird </td>
                  <td> @twitter </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- End .box .span6 -->
      <div class="span6">
        <div class=" box paint color_25">
          <div class="title">
            <h4> <i class=" icon-bar-chart"></i><span>Hover state enabled</span> </h4>
          </div>
          <!-- End .title -->
          <div class="content">
            <p> Add <code>.table-hover</code> to the <code>.table</code> base class to enable a hover state on table rows. </p>
            <table class="table table-striped">
              <thead>
                <tr>
                  <th> # </th>
                  <th> First Name </th>
                  <th> Last Name </th>
                  <th> Username </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 1 </td>
                  <td> Mark </td>
                  <td> Otto </td>
                  <td> @mdo </td>
                </tr>
                <tr>
                  <td> 2 </td>
                  <td> Jacob </td>
                  <td> Thornton </td>
                  <td> @fat </td>
                </tr>
                <tr>
                  <td> 3 </td>
                  <td> Larry </td>
                  <td> the Bird </td>
                  <td> @twitter </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- End .box .span6 -->
    </div>
    <!-- End .row-fluid -->
  </div>
  <!-- End .row-fluid -->
  <div class="row-fluid">
    <div class="span6">
      <div class=" box paint color_12">
        <div class="title">
          <h4> <i class=" icon-bar-chart"></i><span>Condensed Table</span> </h4>
        </div>
        <!-- End .title -->
        <div class="content">
          <p> Add <code>.table-condensed</code> to the <code>.table</code> base class. Makes tables more compact by cutting cell padding in half. </p>
          <table class="table table-condensed table-striped">
            <thead>
              <tr>
                <th> # </th>
                <th> First Name </th>
                <th> Last Name </th>
                <th> Username </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td> 1 </td>
                <td> Mark </td>
                <td> Otto </td>
                <td> @mdo </td>
              </tr>
              <tr>
                <td> 2 </td>
                <td> Jacob </td>
                <td> Thornton </td>
                <td> @fat </td>
              </tr>
              <tr>
                <td> 3 </td>
                <td> Larry </td>
                <td> the Bird </td>
                <td> @twitter </td>
              </tr>
              <tr>
                <td> 4 </td>
                <td> Larry </td>
                <td> the Bird </td>
                <td> @twitter </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- End .box .span6 -->
    <div class="span6">
      <div class="box paint">
        <div class="title">
          <h4> <i class=" icon-bar-chart"></i><span>Table with row class</span> </h4>
        </div>
        <!-- End .title -->
        <div class="content">
          <table class="table">
            <thead>
              <tr>
                <th> # </th>
                <th> Product </th>
                <th> Payment Taken </th>
                <th> Status </th>
              </tr>
            </thead>
            <tbody>
              <tr class="success">
                <td> 1 </td>
                <td> Success </td>
                <td> 01/04/2012 </td>
                <td> Approved </td>
              </tr>
              <tr class="error">
                <td> 2 </td>
                <td> Error </td>
                <td> 02/04/2012 </td>
                <td> Declined </td>
              </tr>
              <tr class="warning">
                <td> 3 </td>
                <td> Warning </td>
                <td> 03/04/2012 </td>
                <td> Pending </td>
              </tr>
              <tr class="info">
                <td> 4 </td>
                <td> Info </td>
                <td> 03/04/2012 </td>
                <td> Call in to confirm </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- End .box .span6 -->
  </div>
  <!-- End .row-fluid -->

</div>
<!-- End #container -->
</div>
<div id="footer">
  <p> &copy; Cuore 2011 </p>
  <span class="company_logo"><a href="http://www.cuoretechnology.com"></a></span> </div>
</div>
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
</div>
<!-- /container -->

<!-- Le javascript
    ================================================== -->
<!-- General scripts -->
<script src="js/jquery.js" type="text/javascript"> </script>
<!--[if !IE]> -->
<script src="js/plugins/enquire.min.js" type="text/javascript"></script>
<!-- <![endif]-->
<script language="javascript" type="text/javascript" src="js/plugins/jquery.sparkline.min.js"></script>
<script src="js/plugins/excanvas.compiled.js" type="text/javascript"></script>

<!-- Modal Concept -->
<script language="javascript" type="text/javascript" src="js/plugins/avgrund.js"></script>
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
<script src="js/jquery-ui-1.8.23.custom.min.js" type="text/javascript"></script>
<script src="js/jquery.touchdown.js" type="text/javascript"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.uniform.min.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.tinyscrollbar.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jnavigate.jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jquery.touchSwipe.min.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.peity.min.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/chosen/chosen/chosen.jquery.min.js"></script>

<!-- Custom made scripts for this template -->
<script src="js/scripts.js" type="text/javascript"></script>
<script type="text/javascript">
  /**** Specific JS for this page ****/

      $(document).ready(function() {
      // Chosen select plugin
        $(".chzn-select").chosen({
          disable_search_threshold: 10
        });
     });


</script>
</body>
</html>
