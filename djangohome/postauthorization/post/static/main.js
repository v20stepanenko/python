const user = {};
fetch('http://localhost/user-info/').then(d => d.json()).then(d => {
    user.name = d.name;
    user.id = d.id
});