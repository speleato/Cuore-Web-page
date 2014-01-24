<%inherit file="cuorewebpage:templates/layout_sidebar_default.mako"/>

<div id="main_container">
  <div class="row-fluid">
    <div class="span6 ">
    <div class="box color_3 title_big height_big paint_hover">
      <div class="title">
        <div class="row-fluid">
          <div class="span12">
            <h4> </i><span>Newsfeed</span> </h4>
          </div>
          <!-- End .span12 -->
        </div>
        <!-- End .row-fluid -->

      </div>
      <!-- End .title -->
      <div class="content"  style="padding-top:35px;">
        <div id="placeholder" style="width:100%;height:240px;"> </div>
      </div>
      </div>
    </div>
    <!-- End .box .span6-->
    <div class="span6">
      <div class="row-fluid fluid">
        <div class="span6">
          <div class=" box color_2 height_medium paint_hover">
            <div class="content numbers">
              <h3 class="value">219.103</h3>
              <div class="description mb5">Audience Reach</div>
              <h1 class="value">3.28<span class="percent">%</span></h1>
              <div class="description">Average CTR</div>
            </div>
          </div>
        </div>
        <!-- End .span6 -->
        <div class="span6">
          <div class="box color_25 height_medium paint_hover">
            <div class="content numbers">
              <h3 class="value">7.147</h3>
              <div class="description mb5">Total Clicks</div>
              <h1 class="value">718.862</h1>
              <div class="description">Total Impressions</div>
            </div>
          </div>
        </div>
        <!-- End .span6 -->
      </div>
      <!-- End .row-fluid -->
      <div class="row-fluid fluid">
        <div class="span6">
          <div class=" box  height_medium title_big paint_hover">
            <div class="title">
              <div class="row-fluid">
                <div class="span12">
                  <h5> </i><span>Fundraisers</span> </h5>
                </div>
                <!-- End .span12 -->
              </div>
              <!-- End .row-fluid -->
            </div>
            <!-- End .title -->
            <div class="content" style="padding-top:28px;">
              <div id="placeholder2" style="width:100%;height:85px;"></div>
              <div class="row-fluid description">
                <div class="pull-left">LAST 30 DAYS</div>
                <div class="pull-right">TODAY</div>
              </div>
            </div>
          </div>
        </div>
        <!-- End .span6 -->
        <div class="span6">
          <div class=" box color_26 height_medium paint_hover">
            <div class="content icon big_icon"> <a href="#" ><img align="center" src="img/general/contacts_icon.png" /></a>
              <div class="description">CONTACTS</div>
            </div>
          </div>
        </div>
        <!-- End .span6 -->
      </div>
      <!-- End .row-fluid -->

    </div>
    <!-- End.span6-->
  </div>
  <!-- End .row-fluid -->

  <div class="row-fluid">
    <div class="span8">
      <div class="box height_xxbig paint">
        <div class="title">
          <h4> <span>Distribution by Country</span> </h4>
        </div>
        <!-- End .title -->
        <div class="content full">
          <table id="datatable_example" class="responsive table table-hover full">
            <thead>
              <tr>
                <th class="jv no_sort"> No </th>
                <th class="ue"> Browser </th>
                <th class="ms no_sort "> Visits </th>
                <th class="Yy to_hide_phone"> % Visits </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td> 1 </td>
                <td> United States </td>
                <td class="ms"> 161.083 </td>
                <td class="to_hide_phone"> 45,73% <span class="bar1 no_ie">3,4,10,5,3,6,3</span></td>
              </tr>
              <tr>
                <td> 2 </td>
                <td> Canada </td>
                <td class="ms"> 93.966 </td>
                <td class="to_hide_phone"> 26,67% <span class="bar2 no_ie">1, 4, 6, 7,4, 2,4</span></td>
              </tr>
              <tr>
                <td> 3 </td>
                <td> Argentina </td>
                <td class="ms"> 69.640 </td>
                <td class="to_hide_phone"> 19,77% <span class="bar2 no_ie">1, 2, 2, 7,4, 2,2</span></td>
              </tr>
              <tr>
                <td> 4 </td>
                <td> Romania </td>
                <td class="ms"> 24.421 </td>
                <td class="to_hide_phone"> 6,93% &nbsp; <span class="bar2 no_ie">3, 5, 6, 9,10, 9,8</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- End .content -->
        <div class="description">Some explanation text here <i class="gicon-info-sign icon-white"></i></div>
      </div>

      <!-- End .box -->
    </div>
    <!-- End .span8 -->

    <div class="span4">
      <div class="box height_big paint">
        <div class="title">
          <h4> <span>Top Users</span> </h4>
        </div>
        <!-- End .title -->

        <ul class="users unstyled content">
          <li>
            <div class="info row-fluid"><span class="number pull-left text_color_0">1</span>
              <h2 class="pull-left">George</h2>
            </div>
            <div class="row-fluid">
              <div class="progress small" style="width: 60%;"></div>
              <div class="value">12k Reach</div>
            </div>
          </li>
          <li>
            <div class="info row-fluid"><span class="number pull-left text_color_0">2</span>
              <h2 class="pull-left">John</h2>
            </div>
            <div class="row-fluid">
              <div class="progress small" style="width: 40%;"></div>
              <div class="value">8.3k Reach</div>
            </div>
          </li>
          <li>
            <div class="info row-fluid"><span class="number pull-left text_color_0">3</span>
              <h2 class="pull-left">Michael</h2>
            </div>
            <div class="row-fluid">
              <div class="progress small" style="width: 25%;"></div>
              <div class="value">6.7k Reach</div>
            </div>
          </li>
        </ul>
        <!-- End .content -->
        <div class="description">Some explanation text here <i class="gicon-info-sign icon-white"></i> </div>
      </div>
      <!-- End .box -->
    </div>
    <!-- End .span4 -->
  </div>
  <!-- End .row-fluid -->



  <div class="row-fluid">
    <div class="span6">
      <div class="box gradient color_25 height_xbig paint_hover1">
        <div class="title row-fluid">
          <h4 class="pull-left"><span>Task List</span></h4>
          <div class="btn-toolbar pull-right ">
            <div class="btn-group"> <a class="btn">Add New +</a> <a class="btn change_color_outside"><i class="paint_bucket"></i></a> </div>
          </div>
        </div>
        <!-- End .title -->
        <div class="content row-fluid">
          <div id="todoapp" class="row-fluid">
            <div class="todos">
              <ul data-bind="foreach: tasks, visible: tasks().length > 0" id="todo-list" class="unstyled">
                <li>
                  <div class="todo" data-bind="css: { editing: isEditing }, event: { dblclick: startEdit }">
                    <div class="display" data-bind="css: { done: isDone }">
                      <input type="checkbox" class="check" data-bind="checked: isDone" />
                      <div class="todo-text" data-bind="html: title"></div>
                      <a href="#" class="todo-destroy" data-bind="click: $parent.removeTask">&times;</a> </div>
                    <div class="edit">
                      <form data-bind="submit: updateTask" class="full">
                        <input data-bind="value: title" class="row-fluid"/>
                      </form>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div id="credits" class="description"> *Double-click to edit tasks. Enter to finish. </div>
        </div>
        <!-- End .content -->
        <div class="description"> You have <b data-bind="text: incompleteTasks().length">&nbsp;</b> incomplete task(s) <span data-bind="visible: incompleteTasks().length == 0">- its beer time!</span> <a class="pull-right" data-bind="visible: completeTasks().length &gt; 0, click: removeCompleted" href="#" id="clear-completed">Clear Completed Tasks </a> </div>
      </div>
      <!-- End .box -->
    </div>
    <!-- End .span6 -->
    <div class="span6">
      <div class="box color_2 ">
        <div class="title row-fluid">
          <h4 class="pull-left"><span>Messages</span></h4>
          <div class="btn-toolbar pull-right ">
            <div class="btn-group"> <a class="btn">View All</a> <a class="btn change_color_outside"><i class="paint_bucket"></i></a> </div>
          </div>
        </div>
        <!-- End .title -->
        <div class="content row-fluid">
          <ul class="messages_layout">



            <li class="from_user left"> <a href="#" class="avatar"><img src="img/message_avatar2.png"/></a>
              <div class="message_wrap"> <span class="arrow"></span>
                <div class="info"> <a class="name" href="#">Celeste Holm</a> <span class="author"><a href="#">@celeste</a></span></div>
                <div class="text"> All I want is to be a monkey of moderate intelligence who wears a suit… that's why I'm transferring to business school! I had more, but you go ahead.  Dissect its brain! </div>
                <div class="footer">
                    <span class="time">1 hour ago</span>
                    <div class="actions pull-right hidden-phone">
                      <ul class="pull-right">
                        <li><a href="#"><i class=" gicon-share-alt icon-white"></i>Reply</a></li>
                        <li><a href="#"><i class=" gicon-share icon-white"></i>Share</a></li>
                        <li><a href="#"><i class=" gicon-star icon-white"></i>Favorite</a></li>
                      </ul>
                    </div>
                </div>
              </div>
            </li>

            <li class="by_myself right"> <a href="#" class="avatar"><img src="img/message_avatar4.png"/></a>
              <div class="message_wrap"> <span class="arrow"></span>
                <div class="info"> <a class="name" href="#">Bender (myself)</a> <span class="author"><a href="#">@bender</a></span></div>
                <div class="text"> Man, I'm sore all over.  I feel like I just went ten rounds with mighty Thor. File not found. </div>
                <div class="footer">
                    <span class="time">4 hours ago</span>
                    <div class="actions pull-right hidden-phone">
                      <ul class="pull-right">
                        <li><a href="#"><i class=" gicon-share-alt icon-white"></i>Reply</a></li>
                        <li><a href="#"><i class=" gicon-share icon-white"></i>Share</a></li>
                        <li><a href="#"><i class=" gicon-star icon-white"></i>Favorite</a></li>
                      </ul>
                    </div>
                </div>
              </div>
            </li>
            <li class="from_user left"> <a href="#" class="avatar"><img src="img/message_avatar2.png"/></a>
              <div class="message_wrap"> <span class="arrow"></span>
                <div class="info"> <a class="name" href="#">Celeste Holm</a> <span class="author"><a href="#">@celeste</a></span></div>
                <div class="text"> And I'd do it again! And perhaps a third time! But that would be it. Are you crazy? </div>
                <div class="footer">
                    <span class="time">1 hour ago</span>
                    <div class="actions pull-right hidden-phone">
                      <ul class="pull-right">
                        <li><a href="#"><i class=" gicon-share-alt icon-white"></i>Reply</a></li>
                        <li><a href="#"><i class=" gicon-share icon-white"></i>Share</a></li>
                        <li><a href="#"><i class=" gicon-star icon-white"></i>Favorite</a></li>
                      </ul>
                    </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <!-- End .content -->
      </div>
      <!-- End .box -->
    </div>
    <!-- End .span6 -->

  </div>
  <!-- End .row-fluid -->
</div>
<!-- End #container -->
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
<script src="js/jquery-ui-1.8.23.custom.min.js" type="text/javascript"></script>
<!--[if !IE]> -->
<!--[if !IE]> -->
<script src="js/plugins/enquire.min.js" type="text/javascript"></script>
<!-- <![endif]-->
<!-- <![endif]-->
<!--[if lt IE 7]>
<script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE7.js"></script>
<![endif]-->
<script language="javascript" type="text/javascript" src="js/plugins/jquery.sparkline.min.js"></script>
<script src="js/plugins/excanvas.compiled.js"></script>
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

<!-- Flot charts -->
<script language="javascript" type="text/javascript" src="js/plugins/flot/jquery.flot.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/flot/jquery.flot.resize.js"></script>

<!-- Data tables -->
<script type="text/javascript" language="javascript" src="js/plugins/datatables/js/jquery.dataTables.js"></script>

<!-- Task plugin -->
<script language="javascript" type="text/javascript" src="js/plugins/knockout-2.0.0.js"></script>

<!-- Custom made scripts for this template -->
<script src="js/scripts.js" type="text/javascript"></script>
<script type="text/javascript">
  /**** Specific JS for this page ****/
/* Todo Plugin */
var todo_data = [
{id: 1, title: "<i class='gicon-gift icon-white'><\/i>Have tea with the Queen", isDone: false},
{id: 2, title: "<i class='gicon-briefcase icon-white'><\/i>Steal  James Bond car", isDone: true},
{id: 3, title: "<i class='gicon-heart icon-white'><\/i>Confirm that this template is awesome", isDone: false},
{id: 4, title: "<i class='gicon-thumbs-up icon-white'><\/i>Nothing", isDone: false},
{id: 5, title: "<i class='gicon-fire icon-white'><\/i>Play solitaire", isDone: false}
];


function Task(data) {
  this.title = ko.observable(data.title);
  this.isDone = ko.observable(data.isDone);
  this.isEditing = ko.observable(data.isEditing);

  this.startEdit = function (event) {
      console.log("editing");
      this.isEditing(true);
  }

  this.updateTask = function (task) {
      this.isEditing(false);
  }
}

function TaskListViewModel() {
          // Data
          var self = this;
          self.tasks = ko.observableArray([]);
          self.newTaskText = ko.observable();
          self.incompleteTasks = ko.computed(function() {
              return ko.utils.arrayFilter(self.tasks(),
                function(task) {
                  return !task.isDone() && !task._destroy;
              });
          });

          self.completeTasks = ko.computed(function(){
              return ko.utils.arrayFilter(self.tasks(),
                function(task) {
                  return task.isDone() && !task._destroy;
              });
          });

          // Operations
          self.addTask = function() {
              self.tasks.push(new Task({ title: this.newTaskText(), isEditing: false }));

              self.newTaskText("");

          };
          self.removeTask = function(task) { self.tasks.destroy(task) };

          self.removeCompleted = function(){
              self.tasks.destroyAll(self.completeTasks());
          };

          /* Load the data */
          var mappedTasks = $.map(todo_data, function(item){
              return new Task(item);
          });

          self.tasks(mappedTasks);
      }

      ko.applyBindings(new TaskListViewModel());
      //End Todo Plugin

      </script><script type="text/javascript">

      //Chart - Campaigns
      $(function () {
        var data_campaigns = [[1,10], [2,9], [3,8], [4,6], [5,5], [6,3], [7,9], [8,10],[9,12],[10,14],[11,15],[12,13],[13,11],[14,10],[15,9],[16,8],[17,12],[18,14],[19,16],[20,19],[21,20],[22,20],[23,19],[24,17],[25,15],[25,14],[26,12],[27,10],[28,8],[29,10],[30,12],[31,10], [32,9], [33,8], [34,6], [35,5], [36,3], [37,9], [38,10],[39,12],[40,14],[41,15],[42,13],[43,11],[44,10],[45,9],[46,8],[47,12],[48,14],[49,16],[50,12],[51,10], [52,9], [53,8], [54,6], [55,5], [56,3], [57,9], [58,10],[59,12],[60,14],[61,15],[62,13],[63,11],[64,10],[65,9],[66,8],[67,12],[68,14],[69,16]];
        var data_campaigns2 = [[1,12], [2,10], [3,9], [4,8], [5,8], [6,8], [7,8], [8,8],[9,9],[10,9],[11,10],[12,11],[13,12],[14,11],[15,10],[16,10],[17,9],[18,10],[19,11],[20,11],[21,12],[22,13],[23,14],[24,13],[25,12],[25,12],[26,11],[27,10],[28,9],[29,8],[30,7],[31,7], [32,8], [33,8], [34,7], [35,6], [36,6], [37,7], [38,8],[39,8],[40,9],[41,10],[42,11],[43,11],[44,12],[45,12],[46,11],[47,10],[48,9],[49,8],[50,8],[51,9], [52,10], [53,11], [54,12], [55,12], [56,12], [57,13], [58,13],[59,12],[60,11],[61,10],[62,9],[63,8],[64,7],[65,7],[66,6],[67,5],[68,4],[69,3]];

        var plot = $.plot($("#placeholder"),
            [ { data: data_campaigns, color:"rgba(0,0,0,0.2)", shadowSize:0,
            bars: {
              show: true,
              lineWidth: 0,
              fill: true,

              fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
          }
      } ,
      { data: data_campaigns2,

          color:"rgba(255,255,255, 0.4)",
          shadowSize:0,
          lines: {show:true, fill:false}, points: {show:false},
          bars: {show:false}
      }
      ],
      {
        series: {
         bars: {show:true, barWidth: 0.6}
     },
     grid: { show:false, hoverable: true, clickable: false, autoHighlight: true, borderWidth:0   },
     yaxis: { min: 0, max: 20 }

 });

        function showTooltip(x, y, contents) {
            $('<div id="tooltip"><div class="date">12 Nov 2012<\/div><div class="title text_color_3">'+x/10+'%<\/div> <div class="description text_color_3">CTR<\/div><div class="title ">'+x*12+'<\/div><div class="description">Impressions<\/div><\/div>').css( {
                position: 'absolute',
                display: 'none',
                top: y - 125,
                left: x - 40,
                border: '0px solid #ccc',
                padding: '2px 6px',
                'background-color': '#fff',
                opacity: 10
            }).appendTo("body").fadeIn(200);
        }

        var previousPoint = null;
        $("#placeholder").bind("plothover", function (event, pos, item) {
            $("#x").text(pos.x.toFixed(2));
            $("#y").text(pos.y.toFixed(2));
            if (item) {
                if (previousPoint != item.dataIndex) {
                  previousPoint = item.dataIndex;
                  $("#tooltip").remove();
                  var x = item.datapoint[0].toFixed(2),
                  y = item.datapoint[1].toFixed(2);
                  showTooltip(item.pageX, item.pageY,
                    x);
              }
          }
      });

         //Fundraisers chart
         var data_fund = [[1,10], [2,9], [3,8], [4,6], [5,5], [6,3], [7,9], [8,10],[9,12],[10,14],[11,15],[12,13],[13,11],[14,10],[15,9],[16,8],[17,12],[18,14],[19,16],[20,19],[21,20],[22,20],[23,19],[24,17],[25,15],[25,14],[26,12],[27,10],[28,8],[29,10],[30,12],[31,10], [32,9], [33,8], [34,6], [35,5], [36,3], ];
         $.plot($("#placeholder2"),
           [ { data: data_fund, color:"#fff", shadowSize:0,
           bars: {
              show: true,
              lineWidth: 0,
              fill: true,
              highlight: {
                opacity: 0.3
            },
            fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
        }
    }
    ],
    {
       series: {
         bars: {show:true, barWidth: 0.6}
     },
     grid: { show:false, hoverable: true, clickable: false, autoHighlight: true, borderWidth:0   },
     yaxis: { min: 0, max: 23 }

 });

         function showTooltip2(x, y, contents) {
          $('<div id="tooltip"><div class="title ">'+x*2+'</div><div class="description">Impressions</div></div>').css( {
            position: 'absolute',
            display: 'none',
            top: y - 58,
            left: x - 40,
            border: '0px solid #ccc',
            padding: '2px 6px',
            'background-color': '#fff',
            opacity: 10
        }).appendTo("body").fadeIn(200);
      }

      var previousPoint = null;
      $("#placeholder2").bind("plothover", function (event, pos, item) {
          $("#x").text(pos.x.toFixed(2));
          $("#y").text(pos.y.toFixed(2));
          if (item) {
            if (previousPoint != item.dataIndex) {
              previousPoint = item.dataIndex;
              $("#tooltip").remove();
              var x = item.datapoint[0].toFixed(2),
              y = item.datapoint[1].toFixed(2);
              showTooltip2(item.pageX, item.pageY,
                x);
          }
      }
  });
    //Envato chart
    $.plot($("#placeholder3"),
       [ { data: data_fund, color:"rgba(0,0,0,0.2)", shadowSize:0,
       bars: {
          lineWidth: 0,
          fill: true,
          fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
      },
      lines: {show:false, fill:true}, points: {show:false} }
  ],
  {
   series: {
     bars: {show:true, barWidth: 0.6}
 },
 grid: { show:false, hoverable: true, clickable: false, autoHighlight: true, borderWidth:0   },
 yaxis: { min: 0, max: 23 }

});
    //Facebook chart
    $.plot($("#placeholder4"),
       [ { data: data_fund, color:"rgba(0,0,0,0.2)", shadowSize:0,
       bars: {

          lineWidth: 0,
          fill: true,

          fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
      },
      lines: {show:false, fill:true}, points: {show:false}
  }
  ],
  {
   series: {
     bars: {show:true, barWidth: 0.6}
 },
 grid: { show:false, hoverable: true, clickable: false, autoHighlight: true, borderWidth:0   },
 yaxis: { min: 0, max: 23 }
});
    // End Fundraiser chart
});




</script>
</body>
</html>


