<%inherit file="layout_sidebar_default.mako"/>

<div id="main_container">
  <div class="row-fluid">
    <div class="span8">
      <div class="box color_13 paint_hover">
        <div class="title">
          <h4> <span>Calendar</span> </h4>
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
          <p> FullCalendar is a jQuery plugin that provides a full-sized, drag & drop calendar like the one below. It uses AJAX to fetch events on-the-fly for each month and is easily configured to use your own feed format (an extension is provided for Google Calendar). It is visually customizable and exposes hooks for user-triggered events (like clicking or dragging an event). It is open source and dual licensed under the MIT or GPL Version 2 licenses. </p>
        </div>
      </div>
      <!-- End .box -->
      <div class="row-fluid box color_24 paint">
        <div class="title">
          <h4> <span>Draggable Events</span> </h4>
        </div>
        <div class="content">
          <div id="external-events">
            <div class="external-event ui-draggable" style="position: relative; "> Annual Conference </div>
            <div class="external-event ui-draggable" style="position: relative; "> Visit to Bender </div>
            <div class="external-event ui-draggable" style="position: relative; "> Dive & Travel Expo </div>
            <div class="external-event ui-draggable" style="position: relative; "> Envato Monthly Meetup </div>
            <div class="external-event ui-draggable" style="position: relative; "> <i class="icon-heart"></i> <strong>Buy Start Template</strong> </div>
            <p>
            <div class="controls">
              <label class="checkbox ">
                <input type="checkbox" id="drop-remove" checked>
                remove after drop
              </label>
            </div>
            </p>
          </div>
        </div>
      </div>
      <!-- End .box -->
      <div class="row-fluid box paint">
        <div class="title">
          <h4> <span>Other Events</span> </h4>
        </div>
        <div class="content top">
          <div id="external-events">
            <div class="external-event ui-draggable" style="position: relative; "> Have fun today </div>
            <div class="external-event ui-draggable" style="position: relative; "> Go to sleep </div>
            <div class="external-event ui-draggable" style="position: relative; "> Free day </div>
            <div class="external-event ui-draggable" style="position: relative; "> Meeting </div>
            <div class="external-event ui-draggable" style="position: relative; "> Birthday party </div>
            <p>
               <div class="controls">
                <label class="checkbox ">
                  <input type="checkbox" id="drop-remove">
                  remove after drop
                </label>
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
      events: [
        {
          title: 'All Day Event',
          start: new Date(y, m, 1)
        },
        {
          title: 'Long Event',
          start: new Date(y, m, d+5),
          end: new Date(y, m, d+7)
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: new Date(y, m, d-3, 16, 0),
          allDay: false
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: new Date(y, m, d+4, 16, 0),
          allDay: false
        },
        {
          title: 'Meeting',
          start: new Date(y, m, d, 10, 30),
          allDay: false
        },
        {
          title: 'Lunch',
          start: new Date(y, m, d, 12, 0),
          end: new Date(y, m, d, 14, 0),
          allDay: false
        },
        {
          title: 'Birthday Party',
          start: new Date(y, m, d+1, 19, 0),
          end: new Date(y, m, d+1, 22, 30),
          allDay: false
        },
        {
          title: 'Click for PixelGrade',
          start: new Date(y, m, 28),
          end: new Date(y, m, 29),
          url: 'http://pixelgrade.com/'
        }
      ]
    });
  });




</script>
            </%block>
