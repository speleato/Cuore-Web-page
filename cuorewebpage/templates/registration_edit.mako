<%inherit file="cuorewebpage:templates/layout_sidebar_default.mako"/>

<div id="main_container">
  <div class="row-fluid">

    <div class="span12">
      <div class="box color_3 title_big paint">
        <div class="title row-fluid fluid">
            <h4> <span>SETTINGS</span> </h4>
        </div>
      <!-- End .title -->

      <div class="content row-fluid" style="padding-top:115px;">
                      %if view=="edit":
                <form class="form-horizontal cmxform" id="validateForm" method="post"
                      action="${request.route_url('Registration_Action', action='submit')}" accept-charset="utf-8"
                      enctype="multipart/form-data" autocomplete="off">
                    <input id="task" name="task" type="hidden" required class="span12" value="${view}"/>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Email Address</label>
                  <div class="controls span9">
                    <input id="email" type="email" name="email" value="${user.getEmail()}" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3" for="mask-phone">Phone <span class="help-block">(999) 999-9999</span> </label>
                  <div class="controls span9">
                    <input id="mask-phone" name="phone" type="text" tabindex="3" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Address</label>
                  <div class="controls span9">
                    <input id="street_address" name="street_address" type="text" value="${user.getAddress()}" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">City</label>
                  <div class="controls span9">
                    <input id="city" name="city" type="text" value="${user.getCity()}" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">State</label>
                  <div class="controls span9">
                    <input id="state" name="state" type="text" value="${user.getState()}" required class="span12"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Zip Code</label>
                  <div class="controls span9">
                    <input id="zip_code" name="zip_code" minlength="5" type="text" value="${user.getZipcode()}" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-row control-group row-fluid">
                    <label class="control-label span3">Profile Image</label>
                    <div class="controls span9">
                        <div class="input-append row-fluid">
                        <input id="profile_image" name="profile_image" type="file" class="spa1n6 fileinput"/>
                        </div>
                    </div>
                </div>
                <div class="form-row control-group row-fluid">
                    <label class="control-label span3" for="elastic-textarea">About</label>
                    <div class="controls span9">
                        <textarea rows="5" class="row-fluid autogrow" id="elastic-textarea" name="about" placeholder="Write a little bit about yourself">${user.getAbout()}</textarea>
                    </div>
                </div>
                <div class="form-actions row-fluid">
                  <div class="span7 offset3">
                    <button type="submit" class="btn btn-primary">Save changes</button>
                    <button type="button" class="btn btn-secondary">Cancel</button>
                  </div>
                </div>
                </form>
            %elif view=="admin":
                <form class="form-horizontal cmxform" id="validateForm" method="post"
                      action="${request.route_url('Registration_Action', action='submit')}" accept-charset="utf-8"
                      enctype="multipart/form-data" autocomplete="off">

                <input id="task" name="task" type="hidden" required class="span12" value="${view}"/>
                <input id="uid" name="uid" value=${user.getUID()} type="hidden"/>
                <h1>${user.getFullName()}</h1>
                <%doc>
                        This is currently a kludgy solution to assign titles. Ideally it should be done with AJAX so that
                    the admin can hit a button that says add title, or remove title. This should then pop up a department
                    and title select box where the contents of the title select box are dynamically rendered based on which
                    department is selected.
                </%doc>
                %for i in departments:
                    <div class="form-row control-group row-fluid">
                    <label class="control-label span3" for="inputEmail">Titles in ${i['department']}</label>
                        <div class="controls span9">
                            <select data-placeholder="None" class="chzn-select" multiple="" tabindex="3" name="titles[]">
                                %if (user.getReqDept() != i['department']) and not user.getDepartment(i['department']):
                                    <option value="None" selected="selected">None</option>
                                    %for j in i['titles']:
                                        <option value="${i['department']},${j['name']}">${j['name']}</option>
                                    %endfor
                                %else:
                                    <option value="None">None</option>
                                    %for j in i['titles']:
                                        %if (j['name'] == user.getReqTitle()) or (user.getTitle(j['name'])):
                                            <option value="${i['department']},${j['name']}" selected="selected">${j['name']}</option>
                                        %else:
                                            <option value="${i['department']},${j['name']}">${j['name']}</option>
                                        %endif
                                    %endfor
                                %endif
                            </select>
                        </div>
                    </div>
                %endfor
                <div class="form-row control-group row-fluid">
                  <label class="control-label span3">Equity Rate</label>
                  <div class="controls span9">
                    <input id="equity_rate" name="equity_rate" type="text" value="${user.getEquityRate()}" required class="row-fluid"/>
                  </div>
                </div>
                <div class="form-actions row-fluid">
                  <div class="span7 offset3">
                    <button type="submit" class="btn btn-primary">Confirm</button>
                    <button type="button" class="btn btn-secondary">Cancel</button>
                  </div>
                </div>
                </form>
            %endif
        </div>
        <!-- End .content -->
      </div>
      <!-- End .box -->
      </div>
      <!-- End .span12-->
    </div>
    <!-- End .row-fluid-->
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
</div>
<!-- /container -->

<%block name="javascript">${parent.javascript}
<!-- Custom made scripts for this template -->
</%block>


