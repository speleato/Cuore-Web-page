<%inherit file="layout_sidebar_default.mako"/>
<% from datetime import datetime %>

<div id="main_container">
  <div class="row-fluid">
    <div class="span8">
      <div class="box color_13 paint_hover">
        <div class="title">
          <h4> <span> ${calendar.getName()} </span> </h4>
        </div>
        <div class="content top ">
          <div id='calendar'> </div>
        </div>
      </div>
      <!-- End .box -->
    </div>
    <!-- End .span8 -->
    <div class="span4">
      <div class="row-fluid box color_25 paint">
        <div class="title">
          <h4> <span>About</span> </h4>
        </div>
        <div class="content ">
          <p> ${calendar.getDescription()} </p>
        </div>
      </div>
      <!-- End .box -->
      <div class="row-fluid box color_24 paint">
        <div class="title">
          <h4> <span>Events</span> </h4>
        </div>
        <div class="content">
          <div id="external-events">
            %for event in events:
                % if event.getStartTime() > (datetime.now()-datetime(1970,1,1)).total_seconds():
                    <div class="external-event" style="position: relative; "> ${event.getName()} </div>
                % endif
            %endfor
          </div>
        </div>
      </div>
      <!-- End .box -->
      <div class="row-fluid box paint">
        <div class="title">
          <h4> <span>Tasks</span> </h4>
        </div>
        <div class="content top">
          <div id="external-events">
            %for task in tasks:
                <div class="external-event ui-draggable" style="position: relative; "> ${task.getName()}</div>
            %endfor
            <p> </p>
          </div>
            </p>
          </div>
        </div>
      </div>
      <!-- End .box -->
    </div>
    <!-- End .span4 -->
  </div>
</div>
<!-- End #container -->
</div>

<%block name="footer">
${parent.footer()}
<%include file="background_changer.mako"/>
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

<!-- Full Calendar -->
<script language="javascript" type="text/javascript" src="js/plugins/full-calendar/fullcalendar.min.js"></script>

<!-- Custom made scripts for this template -->
<script src="js/scripts.js" type="text/javascript"></script>
<script type="text/javascript">
  /**** Specific JS for this page ****/
$(document).ready(function() {
    /* initialize the external events
    -----------------------------------------------------------------*/
    $('#external-events div.external-event').each(function() {
      // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
      // it doesn't need to have a start or end
      var eventObject = {
        title: $.trim($(this).text()) // use the element's text as the event title
      };
      // store the Event Object in the DOM element so we can get to it later
      $(this).data('eventObject', eventObject);
      // make the event draggable using jQuery UI
      $(this).draggable({
        zIndex: 999,
        revert: true,      // will cause the event to go back to its
        revertDuration: 0  //  original position after the drag
      });
    });
    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();
    var calendar = $('#calendar').fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      selectable: true,
      selectHelper: true,
      select: function(start, end, allDay) {
        var title = prompt('Event Title:');
        if (title) {
          calendar.fullCalendar('renderEvent',
            {
              title: title,
              start: start,
              end: end,
              allDay: allDay
            },
            true // make the event "stick"
          );
          jQuery.ajax(
            {
                url       : '/calendar',
                data      : {'title':title,'sTime':start.getTime(), 'eTime':end.getTime()},
                type      : 'POST',
                success   : function(data)
            {
            /*
             when the mako template is rendered by your view then the result will
             be passed to this function in the variable data
            */
            }
            }
          );
        }
        calendar.fullCalendar('unselect');
      },
      editable: true,
      droppable:true,
      drop: function(date, allDay) { // this function is called when something is dropped
        // retrieve the dropped element's stored Event Object
        var originalEventObject = $(this).data('eventObject');
        // we need to copy it, so that multiple events don't have a reference to the same object
        var copiedEventObject = $.extend({}, originalEventObject);
        // assign it the date that was reported
        copiedEventObject.start = date;
        copiedEventObject.allDay = allDay;
        // render the event on the calendar
        // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
        $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);
        // is the "remove after drop" checkbox checked?
        if ($('#drop-remove').is(':checked')) {
          // if so, remove the element from the "Draggable Events" list
          $(this).remove();
        }
      },
      <% from datetime import datetime %>
      events: [
        <% counter = 0 %>
        % for event in events:
            <% sTime = datetime.fromtimestamp(event.getStartTime()) %>
            <% eTime = datetime.fromtimestamp(event.getEndTime()) %>
            {
            title: '${event.getName()}',
            start: new Date(${sTime.year}, ${sTime.month-1}, ${sTime.day})
            //end  : new Date(${eTime.year}, ${eTime.month-1}, ${eTime.day})
            % if counter == len(events)-1:
            }
            % else:
            },
            % endif
            <% counter+=1 %>
        % endfor
      ]
    });
  });




</script>
            </%block>
