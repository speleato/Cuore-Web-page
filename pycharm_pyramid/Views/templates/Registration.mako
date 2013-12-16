<%
    #Values for testing permissions
    admin=1
    registered=0
%>
<form method="post">
    %if admin:
        Title:<input type="text" name="title"><br/>
        Department:<select name="department">
                        <option value="Business Team">(Taking Care of) Business Team</option>
                        <option value="Applications Team">Applications Team</option>
                        <option value="Systems Team">Systems Team</option>
                        <option value="Hardware Team">Hardware Team</option>
                    </select>
        First Name:<input type="text" name="firstName"><br/>
        Last Name:<input type="text" name="lastName"><br/>
        Email:<input type="email" name="email"><br/>
    %elif not registered:
        First Name:<input type="text" name="firstName"><br/>
        Last Name:<input type="text" name="lastName"><br/>
        Email:<input type="email" name="email"><br/>
    %endif
    Phone Number:<input type="tel" name="phone"><br/>
    Address:<input type="text" name="address"><br/>
    About:<textarea name="about"></textarea><br/>
    <input type="submit" value="submit">
</form>