function renderPasswordCheckResult(data) {
  const alertContainer = document.getElementById('alert-container');
  const summaryCard = document.getElementById('summary-card');
  var health_status = ''
  var health_color = ''

  // Clear previous content
  alertContainer.innerHTML = '';
  summaryCard.innerHTML = '';

  // Render alert
  if (data && typeof data === 'object' && data.count !== undefined) {
    if (data.count > 0) {
      alertMessage = `⚠️ ${data.warning}`;
      health_status = 'Pwned';
      health_color = 'text-danger'
      alertType = 'danger'
    } else {
      alertMessage = '✅ This password has not been found in any known breaches.';
      health_status = 'Healthy';
      health_color = 'text-success'
      alertType = 'success'
    }
  } else {
    alertMessage = `⚠️ ${data.warning}`;
    health_status = 'Unknown';
    health_color = 'text-warning';
    alertType = 'warning'
  }

  alertContainer.innerHTML = `
    <div class="alert alert-${alertType} mt-4" role="alert">
      ${alertMessage}
    </div>
  `;

  // Render summary card 
  summaryCard.innerHTML = `
      <div class="card mt-3">
        <div class="card-header custom_color">Password Analysis Summary</div>
        <div class="card-body ">
          <h5 class="card-title">Status: <span class="${health_color}">${health_status}</span></h5>
          <p class="card-text">This password appeared <strong>${data.count.toLocaleString()}</strong> times in known breaches.</p>
        </div>
      </div>
    `;
}


document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('password-form');
  const spinner = document.getElementById('spinner');
  const alertcontainer = document.getElementById('alert-container');
  const summarycard = document.getElementById('summary-card');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const password = document.getElementById('password').value;
    spinner.style.display = 'inline-block';
    alertcontainer.style.display = 'none';
    summarycard.style.display = 'none';

    fetch('/pwned/check-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ password })
    })
      .then(res => res.json())
      .then(data => {
        spinner.style.display = 'none';
        alertcontainer.style.display = '';
        summarycard.style.display = '';
        renderPasswordCheckResult(data);
      });
  });
});