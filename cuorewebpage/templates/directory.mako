<%inherit file="base.mako"/>

<%
    from py2neo import neo4j, ogm
    from database_config import db_config
    from cuorewebpage.Model.Person import Company, Department, Title, Person

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    departments = store.load_unique("Company", "name", "Cuore", Company).getAllDepartments()
%>

<div id="main_container">
  <div class="row-fluid">
    <div class="span3">
      <div class="title">
        <div class="row-fluid legend">
          <h1>Directory</h1>
            </div>
          </div>
          <!-- End .title -->

          <div class="content">
          <!-- End .content -->
        </div>
        <!-- End .span3 -->

<!-- span8 box for each department -->

%for i in departments:
    <%
        job_titles = i.getAllTitles()
    %>
    <div class="row-fluid">
    <div class="span8">
      <div class="box height_big paint">
        <div class="title">
          <h4> <span>${i.name}</span> </h4>
        </div>
        <!-- End .title -->
        <div class="content full">
          <table id="datatable_example" class="responsive table table-hover full">
            <thead>
              <tr>
                <th class="ue"> Name </th>
                <th class="ue"> Title </th>
                <th class="Yy to_hide_phone"> Email </th>
              </tr>
            </thead>
            <tbody>
    %for j in job_titles:
        <%
        persons = j.getAllPersons()
        %>
        %for k in persons:
            <%doc>add link to person's profile, i think can be done using get
                  and then rendering the profile with the name as a parameter</%doc>
              <tr>
                <td><a href="/profile?email=${k.email}"><strong>${k.first_name} ${k.last_name}</strong></a></td>
                <td>${j.name}</td>
                <td><a href="mailto:${k.email}">${k.email}</a></td>
              </tr>
        %endfor <!-- end person's row -->
    %endfor <!-- end of members under same job_title -->
            </tbody>
          </table>
        </div>
        <!-- End .content -->
<!--        <div class="description">Some explanation text here <i class="gicon-info-sign icon-white"></i></div>-->
      </div>
      <!-- End .box -->
%endfor <!-- end of department -->

    </div>
    <!-- End .span8 -->

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


