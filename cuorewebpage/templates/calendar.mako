<%inherit file="layout_sidebar_default.mako"/>
<% from datetime import datetime %>
<% EMAX = 5 %>
<% TMAX = 4 %>
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
            <% counter = 0 %>
            %for event in events:
                % if event.getStartTime() > (datetime.now()-datetime(1970,1,1)).total_seconds() and counter < EMAX:
                    <div class="external-event" style="position: relative; "> ${event.getName()} </div>
                    <% counter+=1 %>
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
          <% counter = 0 %>
            %for task in tasks:
                % if counter < TMAX:
                    <div class="external-event ui-draggable" style="position: relative; "> ${task.getName()}</div>
                    <% counter += 1 %>
                % endif
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

                //The event we will end up updating
                var event = {
                  title: title,
                  start: start,
                  id: -1,
                  end: end,
                  allDay: allDay
                }

                jQuery.ajax(
                    {
                        url       : '/calendar/event/create',
                        data      : {'title':title,'sTime':start.getTime(), 'eTime':end.getTime(), 'allDay':allDay},
                        type      : 'POST',
                        success   : function(data)
                        {
                            //The id of the node that was just created
                            event['id'] = data['id'];
                            console.log("Event id updated to: " + event['id']);
                            calendar.fullCalendar('updateEvent', event)
                        }
                    }
                );
                //Create the new Event in the calendar and assign it all the appropriate fields
                calendar.fullCalendar('renderEvent',
                    event,
                    true // make the event "stick"
                );
            }
            calendar.fullCalendar('unselect');
        },
        editable: true,
        droppable:false,
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
        eventResize: function(event,dayDelta,minuteDelta,revertFunc) {
            jQuery.ajax(
                {
                    url       : '/calendar/event/reschedule',
                    data      : {'action':1, 'id':event.id, 'sTime':event.start.getTime(), 'eTime':event.end.getTime()},
                    type      : 'POST',
                    success   : function(data)
                    {

                    }
                }
            );
        },

        eventDrop: function(event, dayDelta, minuteDelta, allDay, revertFunc, jsEvent, ui, view){
            var eTime = 0;
//            console.log("sTime  : " + event.start.getTime());

            if(event.allDay){
//                console.log("AllDay: Normal");
                eTime = event.start.getTime();
            }
            else if(event.end && !event.allDay){
//                console.log("AllDay: False");
                eTime = event.end.getTime();
            }
            else{
//                console.log("AllDay: Extended");
                eTime = event.start.getTime() + 1000*60*60*2;
            }


            jQuery.ajax(
                {
                    url     : '/calendar/event/reschedule',
                    data    : {'id': event.id, 'sTime':event.start.getTime(), 'eTime':eTime},
                    type    : 'POST',
                    success : function(data)
                    {

                    }
                }
            );
        },

        events: [
            <% counter = 0 %>
            % for event in events:
                <% sTime = datetime.fromtimestamp(event.getStartTime()) %>
            <% eTime = datetime.fromtimestamp(event.getEndTime()) %>
            {
            title: '${event.getName()}',
            id:  '${event.getNode()._id}',
            start: new Date(${sTime.year}, ${sTime.month-1}, ${sTime.day}, ${sTime.hour}, ${sTime.minute}),
            % if (sTime-eTime).total_seconds() != 0:
                end: new Date(${eTime.year}, ${eTime.month-1}, ${eTime.day}, ${eTime.hour}, ${eTime.minute}),
                allDay: false
            % else:
                allDay: true
            % endif
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
