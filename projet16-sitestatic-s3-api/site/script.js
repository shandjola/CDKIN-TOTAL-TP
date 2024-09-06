// Login form submission
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  try {
    const response = await fetch('https://o1jk8a58wj.execute-api.us-east-1.amazonaws.com/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain',
      },
      body: JSON.stringify({ 'actiontype' : 'login' ,'username' : username, 'password' : password })
    });
    const responseData = await response.json() ;
    var rep = JSON.parse(responseData.body)
    if (response.ok && rep.authentification == 'junio') {
      // Redirect to the welcome page
      window.location.href = 'welcome.html';
    } else {
      alert('Invalid username or password');
    }
  } catch (error) {
    console.error('Error logging in:', error);
    alert('An error occurred. Please try again later.');
  }
});

// Register form submission
const registerForm = document.getElementById('registerForm');
registerForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const sexe = document.getElementById('sexe').value;
  console.log('entré');
  try {
    const response = await fetch('https://o1jk8a58wj.execute-api.us-east-1.amazonaws.com/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain'
      },
      body: JSON.stringify({ 'actiontype' : 'register' ,'username' : username, 'password' : password,'sexe': sexe})
    });
    //const responseData = await response.json() ;
    //console.log(responseData);
    //var rep = JSON.parse(responseData.body);
    //console.log(rep);
    if (response.ok) {
      alert('Registration successful! You can now log in.');
      window.location.href = 'login.html';
    } else {
      alert('Registration failed. Please try again.');
    }
  } catch (error) {
    console.error('Error registering:', error);
    alert('An error occurred. Please try again later.');
  }
});