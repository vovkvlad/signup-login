document.addEventListener("DOMContentLoaded", function() {
  const urlParams = new URLSearchParams(window.location.search);
  const loginSuccess = urlParams.get('loginSuccess');

  if(loginSuccess){
    const notification = document.querySelector('.notification');
    notification.style.visibility = 'visible';

    setTimeout(() => {
      notification.style.visibility = 'hidden';
    }, 5000)
  }
});