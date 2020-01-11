document.addEventListener("DOMContentLoaded", function (event) {
  const emailInput = document.getElementById('email');
  const passwordIput = document.getElementById('password');
  const submitButton = document.getElementById('submit');

  submitButton.addEventListener('click', async () => {
    const email = emailInput.value;
    const password = passwordIput.value;
    const response = await axios.post('/user/create', {
      email,
      password,
    });

    debugger;
    if(response.status === 200) {
      window.location.assign('login?loginSuccess=true');
    }
  });
});