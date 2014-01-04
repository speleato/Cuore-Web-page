<%inherit file="base.mako"/>

<%
    # Values for testing permissions, I'd suggest combining confirmation variables into one variable. For example,
    #       0 means no one has confirmed anything, 1 means that leo has confirmed it, 3 means leo and user confirmed it
    admin=0
    registered=0
    awaitingConfirmation=0
    justConfirmed=0

    #get info from database to use as defaults
    ''' psuedocode:
    if user_exists:
        for each attribute:
            attribute=value_of_attribute
    '''
%>

%if awaitingConfirmation:
    <h2>Your registration has been submitted and is in the process of being approved.</h2>
%elif justConfirmed:
    <h2>Thank you for confirming your registration, you are now part of Cuore's system.</h2>
%else:
    <form action="/registration" method="post">
    %if admin:
        <h2>Confirm a User</h2>
            <input type="hidden" name="task" value="admin">
            Title:<input required type="text" name="title"><br/>
            Department:<select name="department">
                            <option value="Business">Business Team</option>
                            <option value="Applications">Applications Team</option>
                            <option value="Systems">Systems Team</option>
                            <option value="Hardware">Hardware Team</option>
                        </select>
            First Name:<input required type="text" name="firstName"><br/>
            Last Name:<input required type="text" name="lastName"><br/>
            Email:<input required type="email" name="email"><br/>
    %elif not registered:
        <h2>Register</h2>
            <input type="hidden" name="task" value="create">
            First Name:<input required type="text" name="firstName"><br/>
            Last Name:<input required type="text" name="lastName"><br/>
            Email:<input required type="email" name="email"><br/>
            Phone Number:<input required type="tel" name="phone"><br/>
            Address:<input required type="text" name="address"><br/>
            City:<input required type="text" name="city"><br/>
            State:<input required type="text" name="state"><br/>
            Zip Code:<input required type="text" name="zipcode" pattern="\d*"><br/>
            About:<textarea name="about"></textarea><br/>
    %else:
        <h2>Edit Profile</h2>
            <input type="hidden" name="task" value="edit">
            Phone Number:<input required type="tel" name="phone"><br/>
            Address:<input required type="text" name="address"><br/>
            City:<input required type="text" name="city"><br/>
            State:<input required type="text" name="state"><br/>
            Zip Code:<input required type="text" name="zipcode" pattern="\d*"><br/>
            About:<textarea name="about"></textarea><br/>
    %endif
        <input type="submit" value="submit">
    </form>
%endif

    <div id="main_container">
      <div class="row-fluid">
        <div class="span7">
          <div class="box paint color_4">
            <div class="title">
              <h4> <span>Registration</span> </h4>
            </div>
            <div class="content">
              <form class="form-horizontal cmxform" id="validateForm" method="get" action="" autocomplete="off">
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3" for="normal-field">First Name</label>
                  <div class="controls span9">
                    <input id="first_name" name="first_name" type="text" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3" for="normal-field">Last Name</label>
                  <div class="controls span9">
                    <input id="last_name" name="last_name" type="text" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Title</label>
                  <div class="controls span9">
                    <input id="job_title" name="job_title" type="text" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3" for="hint-field">Input with min characters <span class="help-block">Required min 3 characters</span> </label>
                  <div class="controls span9">
                    <input id="cname2" name="cname2" minlength="3" type="text" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Email Address <span class="help-block">Enter a valid email address</span> </label>
                  <div class="controls span9">
                    <input id="cemail" type="email" name="email" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">URL Address <span class="help-block">http://www.envato.com</span> </label>
                  <div class="controls span9">
                    <input id="curl" type="url" name="url" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Password</label>
                  <div class="controls span9 ">
                    <div class="input-prepend row-fluid"> <span class="add-on"><i class="icon-lock"></i></span>
                      <input class="row-fluid" type="password" id="password" name="password" placeholder="min 5 characters">
                    </div>
                  </div>
                </div>
                <div class="control-group row-fluid">
                  <label class="control-label span3">Confirm Password</label>
                  <div class="controls span9">
                    <div class="input-prepend row-fluid"> <span class="add-on"><i class="icon-lock"></i></span>
                      <input class="row-fluid" type="password" id="confirm_password" placeholder="confirm password" name="confirm_password">
                    </div>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Required Checkbox </label>
                  <div class="controls span9">
                    <label class="checkbox ">
                      <input type="checkbox" name="agree" id="agree" value="option1">
                      I did the 2 quotes under this message </label>
                    <label for="agree" class="error">Please check for validation</label>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Required Radio </label>
                  <div class="controls span9">
                    <fieldset>
                      <label class="radio ">
                        <input type="radio" name="radios" value="hi"/>
                        Saying hi </label>
                      <label class="radio ">
                        <input type="radio" name="radios" value="feedback"/>
                        Sending feedback </label>
                      <label class="radio ">
                        <input type="radio" name="radios" value="default"/>
                        Default Selected Radio </label>
                      <label for="radios" class="error">Please select your gender</label>
                    </fieldset>
                  </div>
                </div>
                <div class="form-actions row-fluid">
                  <div class="span7 offset3">
                    <button type="submit" class="btn btn-primary">Save changes</button>
                    <button type="button" class="btn btn-secondary">Cancel</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <!-- End .box --> 
        </div>
        <!-- End .span8 -->
        <div class="span5">
          <div class="box paint color_2">
            <div class="title">
              <h4> <i class="icon-calendar"></i> <span>Login form</span> </h4>
            </div>
            <div class="content ">
              <form class="bs-docs-example form-horizontal">
               
                <div class="control-group row-fluid">
                  <label class="control-label span3" for="inputPassword">Username</label>
                  <div class="controls span9 input-append">
                    <input type="password" id="inputUsername" placeholder="Username" class="row-fluid">
                    <span class="add-on"><i class="icon-user"></i></span> </div>
                </div>
                <div class="control-group row-fluid">
                  <label class="control-label span3" for="inputPassword">Password</label>
                  <div class="controls span9 input-append">
                    <input type="password" id="inputPassword" placeholder="Password" class="row-fluid">
                    <span class="add-on"><i class="icon-lock"></i></span> </div>
                </div>
               
                <div class="control-group row-fluid">
                 <div class="span3"></div>
                  <div class="controls span5">
                    <button type="submit" class="btn btn-primary">Sign in</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <!-- End .box --> 
        </div>
        <!-- End .span4 --> 
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
<script language="javascript" type="text/javascript" src="js/plugins/wysihtml5-0.3.0.min.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/bootstrap-wysihtml5.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/jquery.peity.min.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/jquery.uniform.min.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/textarea-autogrow.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/character-limit.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/jquery.maskedinput-1.3.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/chosen/chosen/chosen.jquery.min.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/bootstrap-datepicker.js"></script> 
<script language="javascript" type="text/javascript" src="js/plugins/bootstrap-colorpicker.js"></script> 

<!-- Validation plugin --> 
<script src="js/plugins/validation/dist/jquery.validate.min.js" type="text/javascript"></script> 

<!-- Custom made scripts for this template --> 
<script src="js/scripts.js" type="text/javascript"></script> 
<script type="text/javascript">
  /**** Specific JS for this page ****/

  //Validation things

$().ready(function() {
  // validate the comment form when it is submitted
  // validate signup form on keyup and submit
  $("#validateForm").validate({
    rules: {
      cname: {
        required: true,
      },
      cname2: {
        required: true,
        minlength: 3
      },
      email: {
        required: true,
        email: true
      },
      password: {
        required: true,
        minlength: 5
      },
      confirm_password: {
        required: true,
        minlength: 5,
        equalTo: "#password"
      },
      topic: {
        required: "#newsletter:checked",
        minlength: 2
      },
      agree: "required",
      radios: "required"
    },
    messages: {
      firstname: "Please enter your firstname",
      lastname: "Please enter your lastname",
      username: {
        required: "Please enter a username",
        minlength: "Your username must consist of at least 2 characters"
      },
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long"
      },
      confirm_password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long",
        equalTo: "Please enter the same password as above"
      },
      email: "Please enter a valid email address",
      agree: "Please accept our policy"
    }
  });
  // propose username by combining first- and lastname
  $("#username").focus(function() {
    var firstname = $("#firstname").val();
    var lastname = $("#lastname").val();
    if(firstname && lastname && !this.value) {
      this.value = firstname + "." + lastname;
    }
  });
  //code to hide topic selection, disable for demo
  var newsletter = $("#newsletter");
  // newsletter topics are optional, hide at first
  var inital = newsletter.is(":checked");
  var topics = $("#newsletter_topics")[inital ? "removeClass" : "addClass"]("gray");
  var topicInputs = topics.find("input").attr("disabled", !inital);
  // show when newsletter is checked
  newsletter.click(function() {
    topics[this.checked ? "removeClass" : "addClass"]("gray");
    topicInputs.attr("disabled", !this.checked);
  });
});

//Forms
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
