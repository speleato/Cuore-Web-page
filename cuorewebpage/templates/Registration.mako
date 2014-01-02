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
            Title:<input required=required type="text" name="title"><br/>
            Department:<select name="department">
                            <option value="Business">Business Team</option>
                            <option value="Applications">Applications Team</option>
                            <option value="Systems">Systems Team</option>
                            <option value="Hardware">Hardware Team</option>
                        </select>
            First Name:<input required=required type="text" name="firstName"><br/>
            Last Name:<input required=required type="text" name="lastName"><br/>
            Email:<input required=required type="email" name="email"><br/>
    %elif not registered:
        <h2>Register</h2>
            <input type="hidden" name="task" value="create">
            First Name:<input required=required type="text" name="firstName"><br/>
            Last Name:<input required=required type="text" name="lastName"><br/>
            Email:<input required=required type="email" name="email"><br/>
            Phone Number:<input required=required type="tel" name="phone"><br/>
            Address:<input required=required type="text" name="address"><br/>
            About:<textarea name="about"></textarea><br/>
    %else:
        <h2>Edit Profile</h2>
            <input type="hidden" name="task" value="edit">
            Phone Number:<input required=required type="tel" name="phone"><br/>
            Address:<input required=required type="text" name="address"><br/>
            About:<textarea name="about"></textarea><br/>
    %endif
        <input type="submit" value="submit">
    </form>
%endif
