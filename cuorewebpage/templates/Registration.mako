<%
    # Values for testing permissions, I'd suggest combining confirmation variables into one variable. For example,
    #       0 means no one has confirmed anything, 1 means that leo has confirmed it, 3 means leo and user confirmed it
    admin=0
    registered=0
    awaitingConfirmation=0
    justConfirmed=0
    debug=0

    #get info from database to use as defaults
    from py2neo import neo4j, ogm
    from database_config import db_config
    from cuorewebpage.Model.Person import Person

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    if request.POST:
        email = request.POST.getone("user")
        user=store.load_unique("People", "email", email, Person)
    elif debug:
        email = "kirby@cuore.io"
        user=store.load_unique("People", "email", email, Person)
    else:
        user=UNDEFINED

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
    <form action="/registration/submit" method="post">
    %if user is UNDEFINED:
        <h2>Register (if you're registered try logging in again)</h2>
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
    %elif admin:
        <h2>Confirm a User</h2>
            <input type="hidden" name="task" value="admin">
            Title:<input required type="text" name="title" value="${user.title}"><br/>
            Department:<select name="department" value="${user.department}">
                            <option value="Business">Business Team</option>
                            <option value="Applications">Applications Team</option>
                            <option value="Systems">Systems Team</option>
                            <option value="Hardware">Hardware Team</option>
                        </select>
            First Name:<input required type="text" name="firstName" value="${user.first_name}"><br/>
            Last Name:<input required type="text" name="lastName" value="${user.last_name}"><br/>
            Email:<input required type="email" name="email" value="${user.email}"><br/>
    %else:
        <h2>Edit Profile</h2>
            <input type="hidden" name="task" value="edit">
            Phone Number:<input required type="tel" name="phone" value="${user.phone}"><br/>
            Address:<input required type="text" name="address" value="${user.address}"><br/>
            City:<input required type="text" name="city" value="${user.city}"><br/>
            State:<input required type="text" name="state" value="${user.state}"><br/>
            Zip Code:<input required type="text" name="zipcode" value="${user.zipcode}" pattern="\d*"><br/>
            About:<textarea name="about" value="${user.about}"></textarea><br/>
    %endif
        <input type="submit" value="submit">
    </form>
%endif
