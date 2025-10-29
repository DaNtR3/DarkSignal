const successful_message = "Welcome!"

document.getElementById('login-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  try {
    const response = await fetch('/auth/login', {
      method: 'POST',
      body: formData
    });

    if (response.headers.get('content-type')?.includes('application/json')) {
      const result = await response.json();

      if (!result.success) {
        showLoginNotification(result.message);
      } else {
        window.location.reload();
      }
    } else {
      showLoginNotification(successful_message)
      setTimeout(() => {
        window.location.reload();
      }, 1500);

    }
  } catch (error) {
    showLoginNotification(error);
  }
});

function showLoginNotification(message) {
  const notification = document.getElementById('login-notification');

  notification.innerHTML = `
    <div id="login_toast" class="toast-container position-fixed bottom-0 end-0 p-3">
      <div class="toast show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header header_login_toast">
          <strong class="me-auto">Login Alert</strong>
          <small>Just now</small>
          <button type="button" class="btn-close close_button_color" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body body_login_toast">
          ${message}
        </div>
      </div>
    </div>
  `;

  notification.style.display = 'block';

  setTimeout(() => {
    notification.style.display = 'none';
  }, 3000);
}
