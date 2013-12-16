<%
    admin=1
    registered=0
%>
<form>
    %if admin:
        Title:<input type="text" name="title"></input><br/>
        Department:<select name="department">
                        <option value="Business Team">(taking care of) Business Team</option>
                        <option value="Applications Team">Applications Team</option>
                        <option value="Systems Team">Systems Team</option>
                        <option value="Hardware Team">Hardware Team</option>
                    </select>
        First Name:<input type="text" name="firstName"></input><br/>
        Last Name:<input type="text" name="lastName"></input><br/>
        Email:<input type="email" name="email"></input><br/>
    %elif !registered:
        First Name:<input type="text" name="firstName"></input><br/>
        Last Name:<input type="text" name="lastName"></input><br/>
        Email:<input type="email" name="email"></input><br/>
    %endif
    Phone Number:<input type="tel" name="phone"></input><br/>
    Address:<input type="text" name="address"></input><br/>
    About:<textarea name="about"></textarea><br/>
    <submit>Submit</submit>
</form>